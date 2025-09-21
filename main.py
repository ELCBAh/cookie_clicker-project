import tkinter as tk

# Functions
def main_character_click():
    "Handling character clicks"
    global production
    production += multiplier
    production_label.config(text=f"Production: {production}")

def upgrade_click():
    "Handling upgrade clicks"
    global score, multiplier, multiplier_cost
    if score >= multiplier_cost:
        score -= 10
        multiplier += 1
        multiplier_cost = multiplier_cost * 1.25
        upgrade_button.config(text=f"Upgrade ({multiplier}x) {multiplier_cost:.2f} for points")
        score_label.config(text=f"Score: {score}")
    else:
        upgrade_button.config(text=f"You need {score - multiplier_cost:.2f} more points to upgrade")

def sell_production():
    "Handles production and sell to score"
    global production, score
    if production > 0:
        score += product_value
        production -= sell_quantity
        production_label.config(text=f"Production: {production}")
        score_label.config(text=f"Score: {score}")
        sell_button.config(text=f"Sell for {product_value}")
    else:
        sell_button.config(text="Not enough products to sell")

def upgrade_sell():
    "Handles sell button upgrade"
    global score
    score -= 20


# Variables
# Production variables
product_value = 5
production = 0
production_modifier = 1
# Sell variables
sell_quantity = 1
# Score variables
score = 0
multiplier = 1
multiplier_cost = 10

# Main window
root = tk.Tk()
root.title("Cookie Clicker")
root.geometry("600x400")

# Objects
main_character_img = tk.PhotoImage(file="imgs/main_character2.png")

# Widgets

# Label to show production
production_label = tk.Label(root, text="Production: 0", font=("Arial", 20))
production_label.pack(pady=10)

# Label to show score
score_label = tk.Label(root, text="Score: 0", font=("Arial", 20))
score_label.pack(pady=10)

# Button to click on to increase production
main_character = tk.Button(root, image=main_character_img, width=150, height=200, command=main_character_click)
main_character.pack(pady=20)

# Button to upgrade the main character production generation 2x per click
upgrade_button = tk.Button(root, text=f"Upgrade for {multiplier_cost}", command=upgrade_click)
upgrade_button.pack(pady=10)

# Button to sell production
sell_button = tk.Button(root, text=f"Sell for {product_value}", command=sell_production)
sell_button.pack(pady=20)

# Button to upgrade sell capacity
upgrade_sell_button = tk.Button(root, text="Upgrade sell", command=upgrade_sell)
upgrade_sell_button.pack(pady=10)

root.mainloop()
