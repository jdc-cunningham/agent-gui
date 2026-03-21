from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import tkinter as tk

main_window = None
add_agent_modal_visible = False
add_agent_modal = None

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
    models = ['gpt-4.1-mini', 'mistarl-medium-2508', 'claude-sonnet-4-6', 'gemini-2.5-flash']
    label = tk.Label(add_agent_modal, text="Select model", bg="#ccc")
    label.pack(padx=5, pady=5)
    combo_box = ttk.Combobox(add_agent_modal, values=models, state="readonly")
    combo_box.pack(padx=5, pady=5)
    combo_box.set("gpt-4.1-mini")

    # agent prompt
    label = tk.Label(add_agent_modal, text="Agent instructions", bg="#ccc")
    label.pack(padx=0, pady=5)
    prompt_input = ScrolledText(add_agent_modal, height=5, width=40, wrap=tk.WORD)
    prompt_input.pack(expand=False, fill="none", padx=0, pady=0)

    # tools
    label = tk.Label(add_agent_modal, text="Agent tools", bg="#ccc")
    label.pack(padx=0, pady=5)
    tools_input = tk.Text(add_agent_modal, height=1, width=22)
    tools_input.pack(padx=0, pady=0)

    # definining these button functions here so they have reference to elements of this modal
    def cancel_agent_add():
        add_agent_modal.destroy()

    # buttons
    cancel_button = tk.Button(add_agent_modal, text="Cancel", command=cancel_agent_add)
    cancel_button.place(relx=0.87, rely=0.01)
    add_button = tk.Button(add_agent_modal, text="Add", command=add_agent)
    add_button.pack(pady=5)

def add_agent():
    global add_agent_modal_visible

    if add_agent_modal_visible:
        add_agent_modal.destroy()
    else:
        show_add_agent_modal()

def setup_left_panel(window, frame, db):
    global main_window
    main_window = window
    add_agent_button = tk.Button(frame, text="Add agent", command=add_agent)
    add_agent_button.pack(pady=(520, 0))

    # load agents from db
