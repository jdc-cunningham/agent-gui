from tkinter import ttk
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
        width="400",
        height="300"
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

    # build inputs
    models = ['gpt-4.1-mini', 'mistarl-medium-2508', 'claude-sonnet-4-6', 'gemini-2.5-flash']

    label = tk.Label(add_agent_modal, text="Select model", bg="#ccc")
    label.pack(padx=5, pady=5)

    combo_box = ttk.Combobox(add_agent_modal, values=models, state="readonly")
    combo_box.pack(padx=5, pady=5)
    combo_box.set("gpt-4.1-mini")

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
