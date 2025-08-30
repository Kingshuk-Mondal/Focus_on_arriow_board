import tkinter as tk
import time
from threading import Thread

class FocusBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Focus Target Board")
        self.root.geometry("620x750")

        # Canvas for target board
        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack(pady=10)

        # Info label
        self.info_label = tk.Label(root, text="Press Start to begin 3 min focus", font=("Arial", 16))
        self.info_label.pack(pady=10)

        # Countdown clock below board
        self.time_label = tk.Label(root, text="Timer: 03:00", font=("Arial", 20, "bold"), fg="black")
        self.time_label.pack()

        # Start button
        self.start_button = tk.Button(root, text="Start", font=("Arial", 14), command=self.start_focus)
        self.start_button.pack(pady=10)

        self.focus_running = False

        # Draw target board (7 rings + red bullseye)
        self.draw_target_board()

    def draw_target_board(self):
        """Draw 7 concentric colored circles + red bullseye"""
        colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "white"]  # 7 rings
        radius = 280
        for color in colors:
            self.canvas.create_oval(
                300 - radius, 300 - radius,
                300 + radius, 300 + radius,
                fill=color, outline="black", width=2
            )
            radius -= 40

        # Red bullseye
        self.canvas.create_oval(
            300 - 15, 300 - 15,
            300 + 15, 300 + 15,
            fill="red", outline="black"
        )

    def start_focus(self):
        """Start the 3-minute focus timer"""
        self.start_button.config(state="disabled")
        self.info_label.config(text="Focus on the red dot...")
        self.focus_running = True

        def countdown():
            total_time = 180  # 3 minutes
            while total_time >= 0 and self.focus_running:
                mins, secs = divmod(total_time, 60)
                self.time_label.config(text=f"Timer: {mins:02}:{secs:02}")
                time.sleep(1)
                total_time -= 1

            self.time_label.config(text="Time Over")
            self.info_label.config(text="Well done! 🎯 Focus complete")

        Thread(target=countdown, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusBoard(root)
    root.mainloop()
