import math
import random


# Create base Player class
class Player:
    def __init__(self, letter):
        self.letter = letter # X or O
    
    def get_move(self, game):
        pass


# Create child HumanPlayer class
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Loop until valid input is given
        while True:
            try:
                # Prompt user for move
                square = int(input(f'{self.letter}\'s turn. Input move (0-8): '))
                # Validate input
                if square not in game.available_squares():
                    raise ValueError
                return square
            # Handle invalid input
            except ValueError:
                print('Invalid move. Try again.')

# Create child RandomComputerPlayer class
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Pick a random valid move
        return random.choice(game.available_squares())


# Create child SmartComputerPlayer class
class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Pick a corner square if board is empty
        if game.num_empty_squares() == 9:
            return random.choice([0, 2, 6, 8])
        
        # Pick the optimal move using minimax algorithm
        return self.minimax(game, self.letter)['position']
    
    # Implement the minimax algorithm
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'X' if player == 'O' else 'O'
        
        # Base condition
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player
                    else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        for possible_move in state.available_squares():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)
            
            # Undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best