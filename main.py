# Game main menu

import tkinter as tk
from start_game import GameFrame

class CookieClickerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cookie Clicker")
        self.geometry("1280x720")

        # Container to hold all frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to keep track of frames
        self.frames = {}

        # Initialize frames
        for F in (self.MainMenu, GameFrame):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(self.MainMenu)

    def show_frame(self, frame_class):
        "Show a frame for the given class"
        frame = self.frames[frame_class]
        frame.tkraise()

    def reset_frames(self, frame_class):
        "Clear current frame and create new frame"
        for widget in self.container.winfo_children():
            widget.destroy()
        self.show_frame(frame_class)

    def show_main_menu(self):
        self.show_frame(self.MainMenu)

    class MainMenu(tk.Frame):
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

    def handle_start_click(self):
        "Calling start_game function and passes main window as a new game"
        self.reset_frames(GameFrame)

    def handle_exit_click(self):
        "Closes the main window"
        self.destroy()

    def handle_continue_click(self):
        "Calling continue_game function and passes main window and continues game"
        self.show_frame(GameFrame)

if __name__ == "__main__":
    app = CookieClickerApp()
    app.mainloop()
