import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        # Game State
        self.options = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.comp_score = 0

        # UI Components
        self.setup_ui()

    def setup_ui(self):
        # Title
        tk.Label(self.root, text="Rock Paper Scissors", font=("Arial", 20, "bold")).pack(pady=20)

        # Score Display
        self.score_label = tk.Label(self.root, text="You: 0  |  CPU: 0", font=("Arial", 12))
        self.score_label.pack()

        # Result Display
        self.result_label = tk.Label(self.root, text="Choose your weapon!", font=("Arial", 14, "italic"), fg="blue")
        self.result_label.pack(pady=30)

        # Buttons Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        for option in self.options:
            btn = tk.Button(btn_frame, text=option, width=10, height=2,
                            command=lambda opt=option: self.play(opt))
            btn.pack(side=tk.LEFT, padx=5)

        # Reset Button
        tk.Button(self.root, text="Reset Game", command=self.reset_game, fg="red").pack(pady=20)

    def play(self, user_choice):
        comp_choice = random.choice(self.options)
        
        # Logic to determine winner
        if user_choice == comp_choice:
            result = f"It's a Tie! Both chose {user_choice}"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = f"You Win! {user_choice} beats {comp_choice}"
            self.user_score += 1
        else:
            result = f"You Lose! {comp_choice} beats {user_choice}"
            self.comp_score += 1

        # Update UI
        self.result_label.config(text=result)
        self.score_label.config(text=f"You: {self.user_score}  |  CPU: {self.comp_score}")

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.score_label.config(text="You: 0  |  CPU: 0")
        self.result_label.config(text="Choose your weapon!", fg="blue")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
