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
        self.container.pack(fill="both", expand=True)

        # Dictionary to keep track of frames
        self.frames = {}
        # Initialize game frames at startup
        self.initialize_frames(self.MainMenu)
        self.is_new_game = False

    def initialize_frames(self, frame_class):
        "Clear and initialize frames"
        self.container.destroy()
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.frames[frame_class] = frame_class(self.container, self.controller)
        self.frame_class = frame_class
        self.frames[frame_class].grid(row=0, column=0, sticky="nsew")
    
    def return_to_menu(self):
        "Returns to main menu frame without destroying GameFrame"
        if self.frame_class == GameFrame:
            self.initialize_frames(self.MainMenu)
        else:
            self.show_frame(self.MainMenu)

    def show_frame(self, frame_class):
        "Show a frame for the given class"
        frame = self.frames[frame_class]
        frame.tkraise()

    def handle_start_click(self):
        "Calling start_game function and passes main window as a new game"
        self.initialize_frames(GameFrame)
        self.is_new_game = True

    def handle_exit_click(self):
        "Closes the main window"
        self.destroy()

    def handle_continue_click(self):
        "Show last game frame, if there is none then create a new game"
        if self.is_new_game:
            self.initialize_frames(GameFrame)
        else:
            self.show_frame(self.frame_class)

    class MainMenu(tk.Frame):
        """Frame containing main menu widgets"""
        def __init__(self, parent, controller):
            super().__init__(parent)
            self.controller = controller

            # Widgets
            title_label = tk.Label(self, text="Basic cookie clicker", font=("Arial", 18))
            title_label.pack(pady=20)

            continue_button = tk.Button(self, text="Continue", font=("Arial", 14), command=self.controller.handle_continue_click)
            continue_button.pack(pady=10)

            start_button = tk.Button(self, text="New Game", font=("Arial", 14), command=self.controller.handle_start_click)
            start_button.pack(pady=10)

            exit_button = tk.Button(self, text="Exit", font=("Arial", 14), command=self.controller.handle_exit_click)
            exit_button.pack(pady=10)

if __name__ == "__main__":
    app = CookieClickerApp()
    app.mainloop()
