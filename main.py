from db_service import Database
from manage_agents import setup_left_panel
import tkinter as tk

# db
db = Database()

# setup window
main_window = tk.Tk()
main_window.configure(background="black")
main_window.geometry("1024x600")
main_window.title("Agent GUI")

# setup left panel
leftPane = tk.Frame(
    main_window,
    bg="#000",
    highlightbackground="black",
    highlightcolor="white",
    bd=0,
    relief="flat",
    width=300
)

leftPane.pack_propagate(False)
leftPane.pack(side="left", fill="both")

# populate left panel
left_label = tk.Label(
    leftPane,
    text="View and create agents",
    bg="#000",
    fg="white"
)

left_label.pack(padx=5, pady=5, side="top", anchor="nw")
setup_left_panel(main_window, leftPane, db)

# setup right panel
rightPane = tk.Frame(
    main_window,
    bg="#222",
    highlightbackground="black",
    highlightcolor="white",
    bd=0,
    relief="flat",
    width=724
)

rightPane.pack_propagate(False)
rightPane.pack(side="right", fill="both")

# populate right panel
right_label = tk.Label(
    rightPane,
    text="Running agents",
    bg="#222",
    fg="white"
)

right_label.pack(padx=5, pady=5, side="top", anchor="nw")
main_window.mainloop()
