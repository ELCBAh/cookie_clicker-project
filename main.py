# Game main menu

import tkinter as tk
from start_game import GameFrame

class CookieClickerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = self
        self.title("Cookie Clicker")
        self.geometry("1280x720")

        # Container to hold all frames
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to keep track of frames
        self.frames = {}

        # Showing main menu frame intially
        menu_frame = self.MainMenu(self.container, self.controller)
        self.frames[self.MainMenu] = menu_frame
        menu_frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(self.MainMenu)

    def initialize_frames(self, frame_class):
        "Clear and initialize frames"
        # self.container.grid_forget() # .destroy() is destroying all frames, trying a different approach to keep frames
        game_frame = frame_class(self.container, self.controller)
        self.frames[frame_class] = game_frame
        self.container.grid(row=0, column=0, sticky="nsew")
        game_frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(frame_class)

    def return_to_menu(self):
        "Returns to main menu frame without destroying GameFrame"
        self.show_frame(self.MainMenu)

    def show_frame(self, frame_class):
        "Show a frame for the given class"
        self.frames[frame_class].tkraise()

    def handle_start_click(self):
        "Calling start_game function and passes main window as a new game"
        self.initialize_frames(GameFrame)

    def handle_exit_click(self):
        "Closes the main window"
        self.destroy()

    def handle_continue_click(self):
        "Show last game frame, if there is none then create a new game"
        if GameFrame in self.frames:
            self.show_frame(GameFrame)
        else:
            self.handle_start_click()

    class MainMenu(tk.Frame):
        """Frame containing main menu widgets"""
        def __init__(self, parent, controller):
            super().__init__(parent)
            self.controller = controller

            # Widgets
            title_label = tk.Label(self, text="Basic cookie clicker", font=("Arial", 18))
            title_label.grid(row=0, column=0, pady=20)

            continue_button = tk.Button(self, text="Continue", font=("Arial", 14), command=self.controller.handle_continue_click)
            continue_button.grid(row=1, column=0, pady=10)

            start_button = tk.Button(self, text="New Game", font=("Arial", 14), command=self.controller.handle_start_click)
            start_button.grid(row=2, column=0, pady=10)

            exit_button = tk.Button(self, text="Exit", font=("Arial", 14), command=self.controller.handle_exit_click)
            exit_button.grid(row=3, column=0, pady=10)

if __name__ == "__main__":
    app = CookieClickerApp()
    app.mainloop()
