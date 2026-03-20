from manage_agents import add_agent
import tkinter as tk

# setup window
main_window = tk.Tk()
main_window.configure(background="black")
main_window.geometry("1024x600")
main_window.title("Agent GUI")

# setup left and right panels
leftPane = tk.Frame(main_window, bg="red", highlightbackground="black", highlightcolor="white", bd=0, relief="flat", width=300)
leftPane.pack_propagate(False)
leftPane.pack(side="left", fill="both")
rightPane = tk.Frame(main_window, bg="blue", highlightbackground="black", highlightcolor="white", bd=0, relief="flat", width=724)
rightPane.pack_propagate(False)
rightPane.pack(side="right", fill="both")

# populate left panel
left_label = tk.Label(leftPane, text="View and create agents")
left_label.pack(pady=0)

# populate right panel
right_label = tk.Label(rightPane, text="Running agents")
right_label.pack(pady=0)

main_window.mainloop()
