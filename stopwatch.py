import tkinter as tk
import time
import math

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Stopwatch")
        self.root.geometry("400x500")
        self.root.configure(bg="#1e1e1e")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Create Canvas for 3D Stopwatch
        self.canvas = tk.Canvas(root, width=300, height=300, bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(pady=20)

        # Draw 3D Stopwatch Frame
        self.draw_stopwatch_frame()

        # Timer Display
        self.label = tk.Label(root, text="00:00:00", font=("Courier", 30, "bold"), fg="cyan", bg="#1e1e1e")
        self.label.pack(pady=10)

        # Button Frame (To align buttons side by side)
        button_frame = tk.Frame(root, bg="#1e1e1e")
        button_frame.pack(pady=10)

        # Buttons with Styling
        self.start_button = tk.Button(button_frame, text="Start", command=self.start, font=("Arial", 12, "bold"),
                                      bg="#0f9d58", fg="white", width=8, height=2, relief="raised", bd=4)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop, font=("Arial", 12, "bold"),
                                     bg="#d32f2f", fg="white", width=8, height=2, relief="raised", bd=4)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset, font=("Arial", 12, "bold"),
                                      bg="#fbc02d", fg="black", width=8, height=2, relief="raised", bd=4)
        self.reset_button.grid(row=0, column=2, padx=5)

        self.update_display()

    def draw_stopwatch_frame(self):
        """Draws a 3D Circular Stopwatch"""
        self.canvas.create_oval(50, 50, 250, 250, fill="#222", outline="gray", width=8)  # Outer Ring
        self.canvas.create_oval(90, 90, 210, 210, fill="#333", outline="#777", width=4)  # Inner Circle

        # Create Stopwatch Needle
        self.needle = self.canvas.create_line(150, 150, 150, 80, width=4, fill="red")

    def update_needle(self):
        """Rotates the stopwatch needle dynamically"""
        if self.running:
            angle = (self.elapsed_time % 60) * 6  # 6 degrees per second
            x = 150 + 70 * math.cos(math.radians(270 + angle))
            y = 150 + 70 * math.sin(math.radians(270 + angle))
            self.canvas.coords(self.needle, 150, 150, x, y)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.label.config(text="00:00:00")
        self.canvas.coords(self.needle, 150, 150, 150, 80)  # Reset Needle

    def update(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            minutes = int(self.elapsed_time // 60)
            seconds = int(self.elapsed_time % 60)
            milliseconds = int((self.elapsed_time * 100) % 100)
            self.label.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:02}")
            self.update_needle()
            self.root.after(10, self.update)

    def update_display(self):
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
