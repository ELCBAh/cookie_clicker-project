# All the necessary base game components

import tkinter as tk

# Variables

# Production variables
product_value = 5
production = 0
production_modifier = 1
production_stock = production

# Sell variables
sell_multiplier = 1

# Score variables
score = 0
multiplier_cost = 10
multiplier = 1

def start_game(main_menu_window):
    "Used for running the game"
    main_menu_window.withdraw()

    # Main window
    game_window = tk.Toplevel(main_menu_window)
    game_window.title("Cookie Clicker")
    game_window.geometry("1280x720")

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
            score -= multiplier_cost
            multiplier += 1
            multiplier_cost = multiplier_cost * 1.25
            upgrade_button.config(text=f"Upgrade ({multiplier}x) for {multiplier_cost:.2f} points")
            score_label.config(text=f"Score: {score:.2f}")
        else:
            upgrade_button.config(text=f"You need {score - multiplier_cost:.2f} more points to upgrade")
            upgrade_button.after(3000, lambda: upgrade_button.config(text=f"Upgrade ({multiplier}x) for {multiplier_cost:.2f} points"))

    def sell_production():
        "Handles production and sell to score"
        global score, production
        if production > 0:
            score += product_value * min(production, sell_multiplier)
            production -= min(production, sell_multiplier)
            production_label.config(text=f"Production: {production}")
            score_label.config(text=f"Score: {score:.2f}")
            sell_button.config(text=f"Sell for {product_value}")
        else:
            sell_button.config(text="Not enough products to sell")
            sell_button.after(3000, lambda: sell_button.config(text=f"Sell for {product_value}"))

    def upgrade_sell():
        "Handles sell button upgrade"
        global score, sell_multiplier
        if score >= 20:
            score -= 20
            sell_multiplier += 1
            score_label.config(text=f"Score: {score:.2f}")
            upgrade_sell_button.config(text=f"Upgrade sell ({sell_multiplier}x) for 20 points")
        else:
            upgrade_sell_button.config(text=f"You need {score - 20:.2f} more points to upgrade")
            upgrade_sell_button.after(3000, lambda: upgrade_sell_button.config(text=f"Upgrade sell ({sell_multiplier}x) for 20 points"))

    def toggle_production_box():
        "Switching visibility of content_frame"
        if content_frame.winfo_viewable():
            content_frame.pack_forget()
            toggle_button.config(text="+ Production")
        else:
            content_frame.pack(pady=20)
            toggle_button.config(text="- Production")

    def toggle_economy_box():
        "Switching visibility of economy_frame"
        if economy_frame.winfo_viewable():
            economy_frame.pack_forget()
            toggle_economy_button.config(text="+ Economy")
        else:
            economy_frame.pack(pady=20)
            toggle_economy_button.config(text="- Economy")

    def return_to_menu():
        game_window.destroy()
        main_menu_window.deiconify()

    def on_game_close():
        game_window.destroy()
        main_menu_window.deiconify()

    # Objects
    main_character_img = tk.PhotoImage(file="imgs/main_character2.png")

    # Widgets

    # Bottom main menu bar
    bottom_main_menu_bar = tk.Frame(game_window)
    bottom_main_menu_bar.pack(side="bottom", pady=20)

    # Top collapsibles bar
    top_collapsibles_bar = tk.Frame(game_window)
    top_collapsibles_bar.pack(side="top", pady=20)

    # Button to toggle production box
    toggle_button = tk.Button(top_collapsibles_bar, text="+ Production", command=toggle_production_box)
    toggle_button.pack(pady=10)

    # Button to toggle economy box
    toggle_economy_button = tk.Button(top_collapsibles_bar, text="+ Economy", command=toggle_economy_box)
    toggle_economy_button.pack(pady=10)

    # Frame to contain production widgets
    content_frame = tk.Frame(game_window)
    content_frame.pack(pady=20)

    # Label to show production
    production_label = tk.Label(content_frame, text="Production: 0", font=("Arial", 20))
    production_label.pack(pady=10)

    # Label to show score
    score_label = tk.Label(content_frame, text="Score: 0", font=("Arial", 20))
    score_label.pack(pady=10)

    # Button to click on to increase production
    main_character = tk.Button(content_frame, image=main_character_img, width=150, height=200, command=main_character_click)
    main_character.img = main_character_img
    main_character.pack(pady=20)

    # Button to upgrade the main character production generation 2x per click
    upgrade_button = tk.Button(content_frame, text=f"Upgrade for {multiplier_cost}", command=upgrade_click)
    upgrade_button.pack(pady=10)

    # Button to sell production
    sell_button = tk.Button(content_frame, text=f"Sell for {product_value}", command=sell_production)
    sell_button.pack(pady=20)

    # Button to upgrade sell capacity
    upgrade_sell_button = tk.Button(content_frame, text="Upgrade sell for 20", command=upgrade_sell)
    upgrade_sell_button.pack(pady=10)

    # Button to return to main menu
    main_menu_button = tk.Button(bottom_main_menu_bar, text="Main Menu", command=return_to_menu)
    main_menu_button.pack(side="bottom", padx=20)

    game_window.protocol("WM_DELETE_WINDOW", on_game_close)
    game_window.protocol("WM_DELETE_WINDOW", return_to_menu)
