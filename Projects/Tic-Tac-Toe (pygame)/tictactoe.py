import sys
import pygame
import random
import numpy as np

from constants import *

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacToe')
screen.fill(BG_COLOR)


# Create Board class
class Board:
    def __init__(self):
        # Create 3 by 3 grid of zeros
        self.squares = np.zeros((ROWS, COLS))
    
    # Create mark square function
    def mark_square(self, row, col, player):
        self.squares[row][col] = player
    
    # Create empty square function
    def empty_square(self, row, col):
        return self.squares[row][col] == 0


# Create TicTacToe class
class TicTacToe:
    def __init__(self):
        self.player = 1
        self.draw = Draw()
        self.draw.lines()
        self.board = Board()
    
    # Create computer player
    def computer_player(self):
        available_square = []
        for row in range(3):
            for col in range(3):
                if self.board.empty_square(row, col):
                    available_square.append((row, col))
        
        return random.choice(available_square) if available_square else None
    
    # Create check win function
    def check_win(self, row , col):
        # Vertical win
        for col in range(3):
            if np.all(self.board.squares[:, col] == self.player):
                self.draw.vertical_winning_line(col, self.player)
                return True
        
        # Horizontal win
        for row in range(3):
            if np.all(self.board.squares[row, :] == self.player):
                self.draw.horizontal_winning_line(row, self.player)
                return True
        
        # Descending diagonal win
        if np.all(np.diag(self.board.squares == self.player)):
            self.draw.descending_winning_diagonal(self.player)
            return True
        
        # Ascending diagonal win
        if np.all(np.diag(np.fliplr(self.board.squares == self.player))):
            self.draw.ascending_winning_diagonal(self.player)
            return True
        
        # If all checks fail then we don't yet have a winner
        return False
    
    # Create restart function
    def restart(self):
        screen.fill(BG_COLOR)
        self.player = 1
        self.draw.lines()
        for row in range(3):
            for col in range(3):
                self.board.squares[row][col] = 0
    
    # Create next turn function
    def next_turn(self):
        self.player = 1 if self.player == -1 else -1


# Create Draw class
class Draw:
    # Draw 4 main lines
    @staticmethod
    def lines():
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)
        
        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)
    
    # Draw X or O
    @staticmethod
    def figures(row, col, player):
        # Draw cross
        if player == 1:
            # Descending line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            # Ascending line
            start_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            end_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        # Draw circle
        else:
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)
    
    # Draw vertical winning line
    @staticmethod
    def vertical_winning_line(col, player):
        start_pos = (col * SQSIZE + SQSIZE // 2, OFFSET // 2)
        end_pos = (col * SQSIZE + SQSIZE // 2, HEIGHT - OFFSET // 2)
        color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
        pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
    
    # Draw horizontal winning line
    @staticmethod
    def horizontal_winning_line(row, player):
        start_pos = (OFFSET // 2, row * SQSIZE + SQSIZE // 2)
        end_pos = (WIDTH - OFFSET // 2, row * SQSIZE + SQSIZE // 2)
        color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
        pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
    
    # Draw descending winning diagonal
    @staticmethod
    def descending_winning_diagonal(player):
        start_pos = (OFFSET // 2, OFFSET // 2)
        end_pos = (WIDTH - OFFSET // 2, HEIGHT - OFFSET // 2)
        color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
        pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
    
    # Draw ascending winning diagonal
    @staticmethod
    def ascending_winning_diagonal(player):
        start_pos = (WIDTH - OFFSET // 2, OFFSET // 2)
        end_pos = (OFFSET // 2, HEIGHT - OFFSET // 2)
        color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
        pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)


def main():
    # Game setup
    game_over = False
    game = TicTacToe()
    board = game.board
    
    # Mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Human player's turn
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and game.player == 1:
                row, col = event.pos[1] // SQSIZE, event.pos[0] // SQSIZE
                
                if board.empty_square(row, col):
                    board.mark_square(row, col, game.player)
                    game.draw.figures(row, col, game.player)
                    if game.check_win(row, col):
                        game_over = True
                    game.next_turn()
                    
                    time = pygame.time.get_ticks()
            
            # Computer player's turn
            if game.player == -1 and not game_over and game.computer_player() is not None:
                # Add time delay
                if pygame.time.get_ticks() - time > 500:
                    row, col = game.computer_player()
                    board.mark_square(row, col, game.player)
                    game.draw.figures(row, col, game.player)
                    if game.check_win(row, col):
                        game_over = True
                    game.next_turn()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game_over = False
                game.restart()
        
        pygame.display.update()


if __name__ == '__main__':
    main()