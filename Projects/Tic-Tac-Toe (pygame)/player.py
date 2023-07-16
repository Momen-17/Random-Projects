import random


# Create a parent Player class
class Player:
    def __init__(self, letter):
        self.letter = letter # X or O
    
    def get_move(self, game):
        pass


# Create a child HumanPlayer class
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Loop until valid input is provided
        while True:
            try:
                # Prompt user for move
                square = int(input(f'{self.letter}\'s turn. Input move (0-8): '))
                # Validate move
                if square not in game.available_squares():
                    raise ValueError
                return square
            # Handle invalid input
            except ValueError:
                print('Invalid move. Try again.')


# Create a child RandomComputerPlayer class
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    # Pick a random valid move
    def get_move(self, game):
        return random.choice(game.available_squares())
