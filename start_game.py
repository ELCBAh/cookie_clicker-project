import tkinter as tk

class GameFrame(tk.Frame):
    "Used for running the game"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # --- Variables ---
        # Production variables
        self.product_value = 5
        self.production = 0
        self.production_modifier = 1
        self.production_stock = self.production

        # Sell variables
        self.sell_multiplier = 1

        # Score variables
        self.score = 0
        self.multiplier_cost = 10
        self.multiplier = 1

        # --- Objects ---
        self.main_character_img = tk.PhotoImage(file="imgs/main_character2.png")

        # --- Widgets ---

        # Bottom main menu bar
        self.bottom_main_menu_bar = tk.Frame(self)
        self.bottom_main_menu_bar.pack(side="bottom", pady=20, anchor="sw")

        # Top collapsibles bar
        self.top_collapsibles_bar = tk.Frame(self)
        self.top_collapsibles_bar.pack(side="top", pady=20, anchor="nw")

        # Content container
        self.content_container = tk.Frame(self)
        self.content_container.pack(pady=10, anchor="nw")

        # Button to toggle production box
        self.toggle_button = tk.Button(self.top_collapsibles_bar, text="+ Production", command=self.toggle_production_box)
        self.toggle_button.pack(side="left", padx=10)

        # Button to toggle economy box
        self.toggle_economy_button = tk.Button(self.top_collapsibles_bar, text="+ Economy", command=self.toggle_economy_box)
        self.toggle_economy_button.pack(side="right", padx=10)

        # Future boxes should pack to the right side of the content container

        # Frame to contain production widgets
        self.production_frame = tk.Frame(self.content_container, bg="lightgreen", padx=10, pady=10)
        self.production_frame.pack(side="left", padx=10, anchor="n")

        # Frame to contain economy widgets
        self.economy_frame = tk.Frame(self.content_container, bg="lightblue", padx=10, pady=10)
        self.economy_frame.pack(side="right", padx=10, anchor="n")

        # Label to show production
        self.production_label = tk.Label(self.economy_frame, text="Production: 0", font=("Arial", 20), bg="lightblue")
        self.production_label.pack(pady=10)

        # Label to show score
        self.score_label = tk.Label(self.economy_frame, text="Score: 0", font=("Arial", 20), bg="lightblue")
        self.score_label.pack(pady=10)

        # Button to click on to increase production
        self.main_character = tk.Button(self.production_frame, image=self.main_character_img, width=150, height=200, command=self.main_character_click)
        self.main_character.pack(pady=20)

        # Button to upgrade the main character production generation 2x per click
        self.upgrade_button = tk.Button(self.production_frame, text=f"Upgrade production for {self.multiplier_cost}", command=self.upgrade_click)
        self.upgrade_button.pack(pady=10)

        # Button to upgrade sell capacity
        self.upgrade_sell_button = tk.Button(self.production_frame, text="Upgrade sell capacity for 20", command=self.upgrade_sell)
        self.upgrade_sell_button.pack(pady=10)

        # Button to sell production
        self.sell_button = tk.Button(self.production_frame, text=f"Sell production for {self.product_value}", command=self.sell_production)
        self.sell_button.pack(pady=10)

        # Button to return to main menu
        self.main_menu_button = tk.Button(self.bottom_main_menu_bar, text="Main Menu", command=self.controller.return_to_menu)
        self.main_menu_button.pack(padx=10, pady=20, anchor="sw")

    # --- Functions ---

    def main_character_click(self):
        "Handling character clicks"
        self.production += self.multiplier
        self.production_label.config(text=f"Production: {self.production}")

    def upgrade_click(self):
        "Handling upgrade clicks"
        if self.score >= self.multiplier_cost:
            self.score -= self.multiplier_cost
            self.multiplier += 1
            self.multiplier_cost = self.multiplier_cost * 1.25
            self.upgrade_button.config(text=f"Upgrade production ({self.multiplier}x) for {self.multiplier_cost:.2f} points")
            self.score_label.config(text=f"Score: {self.score:.2f}")
        else:
            self.upgrade_button.config(text=f"You need {self.score - self.multiplier_cost:.2f} more points to upgrade")
            self.upgrade_button.after(3000, lambda: self.upgrade_button.config(text=f"Upgrade production ({self.multiplier}x) for {self.multiplier_cost:.2f} points"))

    def sell_production(self):
        "Handles production and sell to score"
        if self.production > 0:
            self.score += self.product_value * min(self.production, self.sell_multiplier)
            self.production -= min(self.production, self.sell_multiplier)
            self.production_label.config(text=f"Production: {self.production}")
            self.score_label.config(text=f"Score: {self.score:.2f}")
            self.sell_button.config(text=f"Sell production for {self.product_value}")
        else:
            self.sell_button.config(text="Not enough products to sell")
            self.sell_button.after(3000, lambda: self.sell_button.config(text=f"Sell production for {self.product_value}"))

    def upgrade_sell(self):
        "Handles sell button upgrade"
        if self.score >= 20:
            self.score -= 20
            self.sell_multiplier += 1
            self.score_label.config(text=f"Score: {self.score:.2f}")
            self.upgrade_sell_button.config(text=f"Upgrade sell capacity ({self.sell_multiplier}x) for 20 points")
        else:
            self.upgrade_sell_button.config(text=f"You need {self.score - 20:.2f} more points to upgrade")
            self.upgrade_sell_button.after(3000, lambda: self.upgrade_sell_button.config(text=f"Upgrade sell capacity ({self.sell_multiplier}x) for 20 points"))

    def toggle_production_box(self):
        "Switching visibility of production_frame"
        if self.production_frame.winfo_viewable():
            self.production_frame.pack_forget()
            self.toggle_button.config(text="+ Production")
        else:
            self.production_frame.pack(side="left", padx=10)
            self.toggle_button.config(text="- Production")

    def toggle_economy_box(self):
        "Switching visibility of economy_frame"
        if self.economy_frame.winfo_viewable():
            self.economy_frame.pack_forget()
            self.toggle_economy_button.config(text="+ Economy")
        else:
            self.economy_frame.pack(side="right", padx=10)
            self.toggle_economy_button.config(text="- Economy")
