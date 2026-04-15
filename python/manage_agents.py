from datetime import datetime
from run_agents import Agent
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import threading
import tkinter as tk

db = None
main_window = None
add_agent_modal_visible = False
add_agent_modal = None
available_agents = {}

def show_add_agent_modal(db, left_panel, available_agents, main):
    global add_agent_modal # possibly bad, can use class instead

    # setup frame and label
    add_agent_modal = tk.Frame(
        main_window,
        bg="#ccc",
        width="600",
        height="400"
    )

    add_agent_modal.pack_propagate(False)
    add_agent_modal.place(relx=0.5, rely=0.5, anchor="center")

    add_agent_label = tk.Label(
        add_agent_modal,
        text="Agent details",
        bg="#ccc",
        fg="#282828"
    )

    add_agent_label.pack(padx=5, pady=5, side="top", anchor="nw")

    # agent name input
    label = tk.Label(add_agent_modal, text="Agent name", bg="#ccc")
    label.pack(padx=0, pady=0)
    name_input = tk.Text(add_agent_modal, height=1, width=22)
    name_input.pack(padx=0, pady=0)

    # agent model selection
    models = ['gpt-4.1-mini', 'mistral-medium-2508', 'claude-sonnet-4-6', 'gemini-2.5-flash']
    label = tk.Label(add_agent_modal, text="Select model", bg="#ccc")
    label.pack(padx=5, pady=5)
    combo_box = ttk.Combobox(add_agent_modal, values=models, state="readonly")
    combo_box.pack(padx=5, pady=5)
    combo_box.set("gpt-4.1-mini")

    # agent prompt
    label = tk.Label(add_agent_modal, text="Agent instructions", bg="#ccc")
    label.pack(padx=0, pady=5)
    prompt_input = ScrolledText(add_agent_modal, height=6, width=60, wrap=tk.WORD)
    prompt_input.pack(expand=False, fill="none", padx=0, pady=0)

    # tools
    label = tk.Label(add_agent_modal, text="Agent tools", bg="#ccc")
    label.pack(padx=0, pady=5)
    tools_input = tk.Text(add_agent_modal, height=1, width=22)
    tools_input.pack(padx=0, pady=0)

    # definining these button functions here so they have reference to elements of this modal
    def cancel_agent_add():
        add_agent_modal.destroy()

    def add_agent():
        # get field values
        agent_name = name_input.get("1.0", "end-1c")
        agent_model = combo_box.get()
        agent_prompt = prompt_input.get("1.0", "end-1c")
        agent_tools = tools_input.get("1.0", "end-1c")

        # insert into db
        db.add_agent(
            name=agent_name,
            model_name=agent_model,
            prompt=agent_prompt,
            tools=agent_tools,
            created=datetime.now(),
            last_used=""
        )

        cancel_agent_add()
        render_agent_list(db, left_panel, available_agents, main)

    # buttons
    cancel_button = tk.Button(add_agent_modal, text="Cancel", command=cancel_agent_add)
    cancel_button.place(relx=0.865, rely=0.02)
    add_button = tk.Button(add_agent_modal, text="Add", command=add_agent)
    add_button.pack(pady=7)

# side panel
def render_agent_list(db, left_panel, available_agents, main):
    for agent in available_agents:
        available_agents[agent]["frame"].destroy()

    agents = db.get_agents()

    for index, agent in enumerate(agents):
        agent_frame = tk.Frame(
            left_panel,
            bg="#222",
            width="280",
            height="70"
        )

        available_agents[agent[0]] = {
            "name": agent[0],
            "model": agent[1],
            "prompt": agent[2],
            "tools": agent[3],
            "frame": agent_frame
        }

        agent_frame.pack_propagate(False)
        agent_frame.pack(padx=0, pady=(0 if index == 0 else 4, 0))

        agent_name = tk.Label(
            agent_frame,
            text=agent[0],
            bg="#222",
            fg="white"
        )

        agent_name.pack(padx=(5, 0), pady=(2, 0), side="top", anchor="nw")

        agent_delete = tk.Button(
            agent_frame,
            text="Delete",
            command=lambda x=agent[0]: delete_agent(x, main),
            bg="#222",
            fg="white"
        )

        agent_delete.place(x=5, y=32)

        def start(x):
            start_agent(x, main)

        def run_start(x):
            threading.Thread(target=start, args=(x,)).start()

        agent_start = tk.Button(
            agent_frame,
            text="Start",
            command=lambda x=agent[0]: run_start(x),
            bg="#222",
            fg="white"
        )

        agent_start.place(x=82, y=32)

def add_agent(db, left_panel, available_agents, main):
    global add_agent_modal_visible

    if add_agent_modal_visible:
        add_agent_modal.destroy()
    else:
        show_add_agent_modal(db, left_panel, available_agents, main)

def delete_agent(name, main):
    global available_agents

    agent_info = available_agents[name]

    if name in main.running_agents:
        main.running_agents[name].ui_body.destroy()
        del main.running_agents[name]

    db.delete_agent(name)
    agent_info["frame"].destroy()

    if name in available_agents:
        del available_agents[name]

    for agent in available_agents:
        if agent in main.running_agents:
            y_offset = 30 if len(main.running_agents) == 1 else (((len(main.running_agents) - 1) * 200) + 56)
            main.running_agents[agent].ui_body.place(x=5, y=y_offset)

def render_agent_ui(agent, main):
    agent_ui = tk.Frame(
        main.right_panel,
        bg="#444",
        width="714",
        height="220"
    )

    agent.ui_body = agent_ui

    y_offset = 30 if len(main.running_agents) == 1 else (((len(main.running_agents) - 1) * 200) + 56)
    agent_ui.place(x=5, y=y_offset)

    add_agent_label = tk.Label(
        agent_ui,
        text=f"Agent: {agent.name}",
        bg="#444",
        fg="white"
    )

    add_agent_label.place(x=5, y=5)

    # messages
    label = tk.Label(agent_ui, text="Conversation history", bg="#444", fg="#FFD700")
    label.place(x=5, y=30)
    messages = ScrolledText(agent_ui, height=5, width=85, wrap=tk.WORD, bg="#666", fg="white")
    messages.place(x=5, y=55)
    agent.msg_frame = messages

    # send message to agent
    label = tk.Label(agent_ui, text="Query", bg="#444", fg="#FFD700")
    label.place(x=5, y=160)
    query_input = tk.Text(agent_ui, height=1, width=78, bg="#666", fg="white")
    query_input.place(x=5, y=180)

    # this 2-step thing seems dumb
    def query_agent():
        agent.query_agent(query_input.get("1.0", "end-1c"))
        query_input.delete("1.0", tk.END)

    def run_query():
        threading.Thread(target=query_agent).start()

    # send button
    agent_start = tk.Button(
        agent_ui,
        text="Send",
        command=run_query,
        bg="#444",
        fg="white"
    )

    agent_start.place(x=650, y=180)

def start_agent(name, main):
    if name not in main.running_agents:
        agent_info = available_agents[name]

        agent = Agent(
            agent_info["name"],
            agent_info["model"],
            agent_info["prompt"],
            agent_info["tools"]
        )

        agent.root = main.root
        agent.start_agent()
        main.running_agents[agent.name] = agent
        render_agent_ui(agent, main)

def setup_left_panel(window, left_panel, sqlite_db, main):
    global main_window, db, available_agents
    main_window = window
    db = sqlite_db
    render_agent_list(db, left_panel, available_agents, main)

    # Add agent button
    add_agent_button = tk.Button(
        left_panel,
        text="Add agent",
        command=lambda: add_agent(db, left_panel, available_agents, main),
        bg="#000",
        fg="white"
    )

    add_agent_button.place(x=100, y=510)
