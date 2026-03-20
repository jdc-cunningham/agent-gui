import tkinter as tk

def add_agent():
    print("add clicked")

def setup_left_panel(frame, db):
    add_agent_button = tk.Button(frame, text="Add agent", command=add_agent)
    add_agent_button.pack(pady=(520, 0))

    # load agents from db
