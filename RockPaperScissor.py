import tkinter as tk
from random import choice

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")

        self.choices = ["Rock", "Paper", "Scissors"]

        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:")
        self.info_label.pack()

        self.player_choice = tk.StringVar()
        self.player_choice.set(self.choices[0])  # Default choice
        self.choice_menu = tk.OptionMenu(self.root, self.player_choice, *self.choices)
        self.choice_menu.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play_game)
        self.play_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def play_game(self):
        player_choice = self.player_choice.get()
        computer_choice = choice(self.choices)

        result = self.determine_winner(player_choice, computer_choice)

        self.result_label.config(text=f"Computer chose {computer_choice}. {result}")

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors")
            or (player_choice == "Paper" and computer_choice == "Rock")
            or (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            return "You win!"
        else:
            return "Computer wins!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
