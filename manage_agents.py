from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import tkinter as tk

db = None
main_window = None
add_agent_modal_visible = False
add_agent_modal = None
available_agents = {}

def show_add_agent_modal():
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

    # buttons
    cancel_button = tk.Button(add_agent_modal, text="Cancel", command=cancel_agent_add)
    cancel_button.place(relx=0.865, rely=0.02)
    add_button = tk.Button(add_agent_modal, text="Add", command=add_agent)
    add_button.pack(pady=7)

def add_agent():
    global add_agent_modal_visible

    if add_agent_modal_visible:
        add_agent_modal.destroy()
    else:
        show_add_agent_modal()

def start_agent(name, main):
    global running_agents

    if name not in running_agents:
        agent_info = available_agents[name]

        agent = Agent(
            agent_info["name"],
            agent_info["model"],
            agent_info["prompt"],
            agent_info["tools"]
        )

        agent.start_agent()
        main.running_agents.append(agent)

def setup_left_panel(window, left_panel, sqlite_db, main):
    global main_window, db, available_agents
    main_window = window
    db = sqlite_db

    # load agents from db
    agents = db.get_agents()

    for agent in agents:
        available_agents[agent[0]] = {
            "name": agent[0],
            "model": agent[1],
            "prompt": agent[2],
            "tools": agent[3]
        }

        agent_frame = tk.Frame(
            left_panel,
            bg="#222",
            width="280",
            height="70"
        )

        agent_frame.pack_propagate(False)
        agent_frame.pack(padx=0, pady=(2, 0))

        agent_name = tk.Label(
            agent_frame,
            text=f"Agent: {agent[0]}",
            bg="#222",
            fg="white"
        )

        agent_name.pack(padx=(5, 0), pady=(2, 0), side="top", anchor="nw")

        agent_start = tk.Button(
            agent_frame,
            text="Start",
            command=lambda: start_agent(agent[0], main),
            bg="#222",
            fg="white"
        )

        agent_start.pack(padx=5, pady=5)

    # Add agent button
    add_agent_button = tk.Button(
        left_panel,
        text="Add agent",
        command=add_agent,
        bg="#000",
        fg="white"
    )

    add_agent_button.place(x=100, y=530)
