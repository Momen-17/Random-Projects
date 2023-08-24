import math
import random
from copy import deepcopy


class Player:
    def __init__(self, letter):
        self.letter = letter


class HumanPlayer(Player):
    def get_move(self, game):
        # Loop until a valid move is given
        while True:
            try:
                # Prompt player for move
                square = int(input(f'{self.letter}\'s turn. input move (0-8): '))
                # Validate input
                if square not in game.available_squares():
                    raise ValueError
                return square
            # Handle invalid input
            except:
                print('Invalid square. Try again.')


class EasyAIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.other_letter = 'X' if letter == 'O' else 'O'
    
    def get_move(self, game):
        winning_squares, blocking_squares = [], []
        available_squares = game.available_squares()
        
        
        if len(available_squares) in [1, 7, 8, 9]:
            return random.choice(available_squares)
        
        # Check for winning squares
        for square in available_squares:
            board = deepcopy(game.board)
            board[square] = self.letter
            if game.winner(square, self.letter, board):
                winning_squares.append(square)
        
        # Check for blocking squares:
        for square in available_squares:
            board = deepcopy(game.board)
            board[square] = self.other_letter
            if game.winner(square, self.other_letter, board):
                blocking_squares.append(square)
        
        filtered_squares = [square for square in available_squares
        if square not in winning_squares and square not in blocking_squares]
        
        if filtered_squares:
            return random.choice(filtered_squares)
        elif blocking_squares:
            blocking_not_winning = [square for square in blocking_squares if square not in winning_squares] 
            return random.choice(blocking_not_winning) if blocking_not_winning else random.choice(blocking_squares)
        else:
            return random.choice(winning_squares)


class RandomAIPlayer(Player):
    def get_move(self, game):
        return random.choice(game.available_squares())


class MediumAIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.other_letter = 'X' if letter == 'O' else 'O'
    
    def get_move(self, game):
        winning_squares, blocking_squares = [], []
        available_squares = game.available_squares()
        
        
        if len(available_squares) in [1, 7, 8, 9]:
            return random.choice(available_squares)
        
        # Check for winning squares
        for square in available_squares:
            board = deepcopy(game.board)
            board[square] = self.letter
            if game.winner(square, self.letter, board):
                winning_squares.append(square)
        
        # Check for blocking squares:
        for square in available_squares:
            board = deepcopy(game.board)
            board[square] = self.other_letter
            if game.winner(square, self.other_letter, board):
                blocking_squares.append(square)
        
        if winning_squares:
            return random.choice(winning_squares)
        elif blocking_squares:
            return random.choice(blocking_squares)
        else:
            return random.choice(available_squares)


class UnbeatableAIPlayer(Player):
    def get_move(self, game):
        if len(game.available_squares()) == 9:
            probablities = [1/6, 1/10, 1/6, 1/10, 1/10, 1/10, 1/6, 1/10, 1/6]
            return random.choices(game.available_squares(), probablities)[0]
        else:
            return self.minimax(game, self.letter)['position']
    
    def minimax(self, game, player):
        maximizer = self.letter
        other_player = 'X' if player == 'O' else 'O'
        
        # Terminal case
        if game.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (len(game.available_squares()) + 1) if other_player == maximizer
                    else -1 * (len(game.available_squares()) + 1)}
        elif not game.still_running():
            return {'position': None, 'score': 0}
        
        best = {'position': None, 'score': -math.inf if player == maximizer else math.inf}
        
        for square in game.available_squares():
            game.make_move(square, player)
            sim_score = self.minimax(game, other_player)
            
            # Undo move
            game.board[square] = ' '
            game.current_winner = None
            sim_score['position'] = square
            
            if player == maximizer:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best


class ChallengingAIPlayer(Player):
    def get_move(self, game):
        players = [EasyAIPlayer(self.letter).get_move(game),
                RandomAIPlayer(self.letter).get_move(game),
                MediumAIPlayer(self.letter).get_move(game),
                UnbeatableAIPlayer(self.letter).get_move(game)]
        probabilities = [0.1, 0.1, 0.2, 0.6]
        
        return random.choices(players, probabilities)[0]
