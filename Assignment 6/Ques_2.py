import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.total_rounds = 0
        self.current_round = 0
        self.player_wins = 0
        self.computer_wins = 0
    
    def get_computer_choice(self):
        # Randomly select a choice for the computer
        return random.choice(self.choices)
    
    def find_winner(self, player_choice, computer_choice):
        # Determine the winner of a round
        if player_choice == computer_choice:
            return "draw"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            self.player_wins += 1
            return "player"
        else:
            self.computer_wins += 1
            return "computer"
    
    def check_game_winner(self):
        # Check if anyone has won the game
        if self.player_wins > self.computer_wins:
            return "Player wins the game!"
        elif self.computer_wins > self.player_wins:
            return "Computer wins the game!"
        else:
            return "The game is a draw!"
    
    def play_round(self, player_choice):
        # Play one round of the game
        if self.current_round < self.total_rounds:
            computer_choice = self.get_computer_choice()
            result = self.find_winner(player_choice, computer_choice)
            self.current_round += 1
            print(f"Round {self.current_round}: You chose {player_choice}, Computer chose {computer_choice}.")
            if result == "draw":
                print("It's a draw!")
            else:
                print(f"{result.capitalize()} wins the round!")
        else:
            print("The game has ended.")
    
    def start_game(self):
        # Get total rounds from the user
        self.total_rounds = int(input("Enter the number of rounds you want to play: "))
        
        while self.current_round < self.total_rounds:
            # Get the player's choice
            player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if player_choice not in self.choices:
                print("Invalid choice! Please choose rock, paper, or scissors.")
                continue
            
            self.play_round(player_choice)
        
        print(self.check_game_winner())

# Example usage:
game = RockPaperScissors()
game.start_game()
