from db_service import Database
from manage_agents import setup_left_panel
from run_agents import *
import tkinter as tk

class Main():
    def __init__(self):
        self.root = None
        self.db = Database()
        self.running_agents = {}
        self.left_panel = None
        self.right_panel = None
        self.setup_gui()

    def setup_gui(self):
        # setup window
        main_window = tk.Tk()
        self.root = main_window
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

        self.left_panel = leftPane
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
        setup_left_panel(main_window, leftPane, self.db, self)

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

        self.right_panel = rightPane
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

main = Main()
