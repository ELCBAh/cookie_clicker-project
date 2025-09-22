# Game main menu

import tkinter as tk
import imgs
from start_game import start_game

def handle_start_click():
    "Calling start_game funciton and passes main window"
    start_game(root)

def handle_exit_click():
    "Closes the main window"
    root.destroy()

# Setting up main window
root = tk.Tk()
root.title("Main Menu")
root.geometry("1280x720")

# Widgets
title_label = tk.Label(root, text="Production clicker", font=("Arial", 18))
title_label.pack(pady=20)

start_button = tk.Button(root, text="Start Game", font=("Arial", 14), command=handle_start_click)
start_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=handle_exit_click)
exit_button.pack(pady=10)

root.mainloop()
