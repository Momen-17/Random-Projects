import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass


# Human player class
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    # Prompt player for a move
    def get_move(self, game):
        while True:
            try:
                square = int(input(f'{self.letter}\'s turn Input move (0-8): '))
                # Check move is a valid move
                if square not in game.available_moves():
                    raise ValueError
                return square
            except ValueError:
                print('Invalid square. Try again.')


# Computer player class
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    # Pick a random available spot
    def get_move(self, game):
        return random.choice(game.available_moves())