import tkinter as tk

# Functions
def main_character_click():
    "Handling character clicks"
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

# Variables
score = 0

# Main window
root = tk.Tk()
root.title("Cookie Clicker")
root.geometry("600x400")

# Widgets

# Label to show score
score_label = tk.Label(root, text="Score: 0", font=("Arial", 20))
score_label.pack(pady=10)

# Button to click on to increase score
main_character = tk.Button(root, text="Main Character", width=10, height=5, command=main_character_click)
main_character.pack(pady=20)

root.mainloop()
