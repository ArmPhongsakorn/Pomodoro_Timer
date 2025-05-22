import tkinter as tk
import time

WORK_MIN = 25  # 25 for work time
BREAK_MIN = 5  # 5 for break (stand up, walk and stretching)

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Work Break Timer")
        self.root.geometry("500x400")
        
        self.timer_running = False
        self.time_left = 0
        self.is_work_time = True
        self.session = 1
        self.timer_id = None  # use for .after_cancel

        # Message label
        self.label_message = tk.Label(root, text="Press Start to begin", font=("Arial", 14), fg='#000000')
        self.label_message.pack(pady=10)

        # Timer label
        self.label_timer = tk.Label(root, text="", font=("Arial", 28))
        self.label_timer.pack(pady=10)

        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        # Pause button
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(pady=5)
        
        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=10)

    def reset_timer(self):
        if self.timer_running and self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.timer_running = False
        self.time_left = 0
        self.is_work_time = True
        self.session = 1
        self.timer_id = None
        
        self.label_message.config(text="Press Start to begin", fg='#000000')
        self.label_timer.config(text="")
    
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            if self.time_left == 0:  # start
                self.is_work_time = True
                self.time_left = WORK_MIN * 60
                self.label_message.config(text=f"Session {self.session} - Work time:", fg='#e00202')
            self.countdown()

    def pause_timer(self):
        if self.timer_running:
            self.timer_running = False
            if self.timer_id:
                self.root.after_cancel(self.timer_id)

    def countdown(self):
        if self.timer_running:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.label_timer.config(text=f"{minutes:02d}:{seconds:02d}")
            if self.time_left > 0:
                self.time_left -= 1
                self.timer_id = self.root.after(1000, self.countdown)
            else:
                if self.is_work_time:
                    # Sound to notify
                    self.root.bell()
                    time.sleep(0.5)
                    self.root.bell()
                    # Switch to break
                    self.is_work_time = False
                    self.time_left = BREAK_MIN * 60
                    self.label_message.config(text=f"Session {self.session} - Break time:", fg='#06d602')
                    self.timer_id = self.root.after(1000, self.countdown)
                else:
                    self.root.bell()
                    time.sleep(0.5)
                    self.root.bell()
                    # begin the next session
                    self.session += 1
                    self.time_left = WORK_MIN * 60
                    self.is_work_time = True
                    self.label_message.config(text=f"Session {self.session} - Work time:", fg='#e00202')
                    self.timer_id = self.root.after(1000, self.countdown)

# Run GUI
root = tk.Tk()
app = PomodoroTimer(root)
root.mainloop()
