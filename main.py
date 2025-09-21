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

# Objects
main_character_img = tk.PhotoImage(file="imgs/main_character.png")

# Widgets

# Label to show score
score_label = tk.Label(root, text="Score: 0", font=("Arial", 20))
score_label.pack(pady=10)

# Button to click on to increase score
main_character = tk.Button(root, image=main_character_img, width=200, height=252, command=main_character_click)
main_character.pack(pady=20)

root.mainloop()
