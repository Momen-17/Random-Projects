import sys
import math
import pygame
import random
import numpy as np

from constants import *
from copy import deepcopy

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC-TAC-TOE')


# Create Board class
class Board:
    def __init__(self):
        self.draw = Draw()
        self.marked_squares = 0
        self.squares = np.zeros((ROWS, COLS))
    
    # Create final state method
    def final_state(self, show=False):
        if self.marked_squares >= 5:
            # Vertical win
            for col in range(COLS):
                if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                    if show:
                        self.draw.vertical_winning_line(col, self.squares[0][col])
                    return self.squares[0][col]
            
            # Horizontal win
            for row in range(ROWS):
                if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                    if show:
                        self.draw.horizontal_winning_line(row, self.squares[row][0])
                    return self.squares[row][0]
            
            # Descending diagonal win
            if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
                if show:
                    self.draw.descending_diagonal(self.squares[1][1])
                return self.squares[1][1]
            
            # Ascending diagonal win
            if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
                if show:
                    self.draw.ascending_diagonal(self.squares[1][1])
                return self.squares[1][1]
        
        # If all checks fail then we don't yet have a winner
        return 0
    
    # Create mark square method
    def mark_square(self, row, col, player):
        self.marked_squares += 1
        self.squares[row][col] = player
    
    # Create empty square method
    def empty_square(self, row, col):
        return self.squares[row][col] == 0
    
    # Create available squares method
    def available_squares(self):
        return [(row, col) for row in range(3) for col in range(3) if self.empty_square(row, col)]


# Create AI class
class AI:
    def __init__(self, level=1, player=-1):
        self.level = level
        self.player = player
    
    # Create easy mode
    def easy(self, board):
        return random.choice(board.available_squares()) if board.available_squares() else None
    
    # Create impossible mode
    def minimax(self, board, maximizing):
        case = board.final_state()
        
        if case == 1: # Cross win
            return 1, None
        if case == -1: # Circle win
            return -1, None
        if not board.available_squares(): # Draw
            return 0, None
        
        # Shuffle the list of available moves before evaluating
        available_moves = board.available_squares()
        random.shuffle(available_moves)
        
        if maximizing:
            best_move = None
            max_eval = -math.inf
            
            for row, col in available_moves:
                temp_board = deepcopy(board)
                temp_board.mark_square(row, col, 1)
                eval, _ = self.minimax(temp_board, False)
                # Prioritize winning moves
                if eval == 1:
                    return eval, (row, col)
                
                if eval > max_eval:
                    max_eval = eval
                    best_move = row, col
            return max_eval, best_move
        
        else:
            best_move = None
            min_eval = math.inf
            
            for row, col in available_moves:
                temp_board = deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                eval, _ = self.minimax(temp_board, True)
                # Prioritize blocking winning moves
                if eval == -1:
                    return eval, (row, col)
                
                if eval < min_eval:
                    min_eval = eval
                    best_move = row, col
                    
            return min_eval, best_move
    
    def eval(self, board):
        if self.level == 1:
            eval, move = 'random', self.easy(board)
        else:
            eval, move = self.minimax(board, False)
        
        print(f'AI played the move {move} with and eval of: {eval}')
        
        return move


# Create TicTacToe class
class TicTacToe:
    def __init__(self):
        self.ai = AI()
        self.player = 1
        self.board = Board()
        self.draw = Draw()
        self.draw.lines()
        self.over = False
        self.mode = 'ai'
    
    # Create make move method
    def make_move(self, row, col):
        if self.board.empty_square(row, col):
            self.board.mark_square(row, col, self.player)
            self.draw.figures(row, col, self.player)
            if self.is_over():
                self.over = True
            self.next_turn()
    
    # Create next turn method
    def next_turn(self):
        self.player = 1 if self.player == -1 else -1
    
    # Create change mode method
    def change_mode(self):
        self.mode = 'ai' if self.mode == 'pvp' else 'pvp'
    
    # Create is over method
    def is_over(self):
        return self.board.final_state(True) != 0 or not self.board.available_squares()
    
    # Create restart method
    def restart(self):
        self.player = 1
        self.over = False
        self.draw.lines()
        self.board.squares = np.zeros((ROWS, COLS))


# Create Draw class
class Draw:
    # Draw the 4 main lines
    @staticmethod
    def lines():
        # Fill screen
        screen.fill(BG_COLOR)
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)
        
        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)
    
    # Draw X and O
    @staticmethod
    def figures(row, col, player):
        # Draw cross
        if player == 1:
            # Descending line
            desc_start = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            desc_end = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, desc_start, desc_end, CROSS_WIDTH)
            
            # Ascending line
            asc_start = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            asc_end = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, asc_start, asc_end, CROSS_WIDTH)
        # Draw circle
        else:
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)
    
    # Draw vertical winning line
    @staticmethod
    def vertical_winning_line(col, player):
        start_pos = (col * SQSIZE + SQSIZE // 2, OFFSET // 4)
        end_pos = (col * SQSIZE + SQSIZE // 2, HEIGHT - OFFSET // 4)
        color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
        pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
    
    # Draw horizontal winning line
    @staticmethod
    def horizontal_winning_line(row, player):
        start_pos = (OFFSET // 4, row * SQSIZE + SQSIZE // 2)
        end_pos = (WIDTH - OFFSET // 4, row * SQSIZE + SQSIZE // 2)
        color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
        pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
    
    # Draw descending diagonal
    @staticmethod
    def descending_diagonal(player):
        start_pos = (OFFSET // 2, OFFSET // 2)
        end_pos = (WIDTH - OFFSET // 2, HEIGHT - OFFSET // 2)
        color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
        pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
    
    # Draw ascending diagonal
    @staticmethod
    def ascending_diagonal(player):
        start_pos = (OFFSET // 2, HEIGHT - OFFSET // 2)
        end_pos = (WIDTH - OFFSET // 2, OFFSET // 2)
        color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
        pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)



if __name__ == '__main__':
    game = TicTacToe()
    # Mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game.over:
                row, col = event.pos[1] // SQSIZE, event.pos[0] // SQSIZE
                game.make_move(row, col)
            
            if game.mode == 'ai' and game.player == game.ai.player and not game.over:
                pygame.display.update()
                row, col = game.ai.eval(game.board)
                game.make_move(row, col)
            
            if event.type == pygame.KEYDOWN:
                # Restart key
                if event.key == pygame.K_r:
                    game.restart()
                
                # Change game mode key
                if event.key == pygame.K_g:
                    game.change_mode()
                
                # Change ai level
                if event.key == pygame.K_1:
                    game.ai.level = 1 # Random
                
                if event.key == pygame.K_2:
                    game.ai.level = 2 # Smart
        
        pygame.display.update()