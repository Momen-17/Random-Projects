import os
import sys
import copy
import math
import pygame
import random

SQUARES_POSITIONS = {
            0: (150, 150),
            1: (290, 150),
            2: (430, 150),
            3: (150, 290),
            4: (290, 290),
            5: (430, 290),
            6: (150, 430),
            7: (290, 430),
            8: (430, 430),
        }

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, '..', 'Menu'))

pygame.init()
screen = pygame.display.set_mode((700, 700))


class Display:
    def __init__(self) -> None:
        self.load_resources()
    
    def load_resources(self):
        # Load images
        self.background = pygame.image.load(os.path.join(current_dir, 'assets', 'Background.png'))
        self.board = pygame.image.load(os.path.join(current_dir, 'assets', 'board_600.png'))
        self.back = pygame.image.load(os.path.join(current_dir, 'assets', 'back.png'))
        self.reset = pygame.image.load(os.path.join(current_dir, 'assets', 'reset.png'))
        self.back_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'back_hover.png'))
        self.reset_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'reset_hover.png'))
        self.pvc = pygame.image.load(os.path.join(current_dir, 'assets', '1player.png'))
        self.pvp = pygame.image.load(os.path.join(current_dir, 'assets', '2players.png'))
        self.pvc_hover = pygame.image.load(os.path.join(current_dir, 'assets', '1player_hover.png'))
        self.pvp_hover = pygame.image.load(os.path.join(current_dir, 'assets', '2players_hover.png'))
        self.ellipsea = pygame.image.load(os.path.join(current_dir, 'assets', 'EllipseA.png'))
        self.ellipsed = pygame.image.load(os.path.join(current_dir, 'assets', 'EllipseD.png'))
        self.ellipseh = pygame.image.load(os.path.join(current_dir, 'assets', 'EllipseH.png'))
        self.ellipsev = pygame.image.load(os.path.join(current_dir, 'assets', 'EllipseV.png'))
        self.x_marker = pygame.image.load(os.path.join(current_dir, 'assets', 'x.png'))
        self.o_marker = pygame.image.load(os.path.join(current_dir, 'assets', 'o.png'))
    
    def render(self, board, game_mode, scores, game_winner, easy_toggle=False, medium_toggle=False, hard_toggle=False):
        self.render_background()
        self.render_board()
        self.render_buttons_hover()
        self.render_game_mode(game_mode)
        
        self.render_moves(board)
        
        if game_mode == 'pvc':
            self.render_ai_difficulty(210, 'Easy', easy_toggle)
            self.render_ai_difficulty(308, 'Medium', medium_toggle)
            self.render_ai_difficulty(406, 'Hard', hard_toggle)
        
        self.render_scores(scores)
        if game_winner:
            if game_winner[0] == 'a':
                screen.blit(self.ellipsea, (140, 140))
            if game_winner[0] == 'd':
                screen.blit(self.ellipsed, (140, 140))
            if game_winner[0] == 'h':
                screen.blit(self.ellipseh, (125, 206.5 + game_winner[1] * 140))
            if game_winner[0] == 'v':
                screen.blit(self.ellipsev, (206.5 + game_winner[1] * 140, 125))
            self.render_next()
    
    def render_background(self):
        screen.blit(self.background, (0, 0))
    
    def render_board(self):
        screen.blit(self.board, (140, 140))
    
    def render_buttons_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        
        if 17.5 <= mouse_pos[0] <= 87.5 and 17.5 <= mouse_pos[1] <= 87.5:
            screen.blit(self.back_hover, (17.5, 17.5))
            screen.blit(self.reset, (87.5, 17.5))
        elif 87.5 <= mouse_pos[0] <= 157.5 and 17.5 <= mouse_pos[1] <= 87.5:
            screen.blit(self.back, (17.5, 17.5))
            screen.blit(self.reset_hover, (87.5, 17.5))
        else:
            screen.blit(self.back, (17.5, 17.5))
            screen.blit(self.reset, (87.5, 17.5))
    
    def render_hover_pvc(self):
        mouse_pos = pygame.mouse.get_pos()
        
        if 595 <= mouse_pos[0] <= 647.5 and 28 <= mouse_pos[1] <= 80.5:
            screen.blit(self.pvc_hover, (595, 28))
        else:
            screen.blit(self.pvc, (595, 28))
    
    def render_hover_pvp(self):
        mouse_pos = pygame.mouse.get_pos()
        
        if 595 <= mouse_pos[0] <= 647.5 and 28 <= mouse_pos[1] <= 80.5:
            screen.blit(self.pvp_hover, (595, 28))
        else:
            screen.blit(self.pvp, (595, 28))
    
    def render_scores(self, scores):
        font = pygame.font.Font(None, 39)
        offset = 0
        
        for player, score in scores.items():
            text_surface = font.render(player, True, (255, 255, 255))  # Render states
            text_rect = text_surface.get_rect(center=(210 + offset, 605))
            
            score_surface = font.render(str(score), True, (255, 255, 255))  # Render score
            score_rect = score_surface.get_rect(center=(210 + offset, 640))
            
            screen.blit(text_surface, text_rect)
            screen.blit(score_surface, score_rect)
            offset += 140
    
    def render_game_mode(self, game_mode):
        self.render_hover_pvc() if game_mode == 'pvc' else self.render_hover_pvp()
    
    def render_moves(self, board):
        for square, player in enumerate(board):
            if player != 0:
                position = SQUARES_POSITIONS[square]
                screen.blit(self.x_marker, position) if player == 1 else screen.blit(self.o_marker, position)
    
    def render_next(self):
        pygame.draw.rect(screen, '#073b4c', (322, 341, 56, 17.5), border_radius=5)
        font = pygame.font.Font(None, 18)
        text_surface = font.render('Next', True, (255, 255, 255)) # text, antialias, color
        text_rect = text_surface.get_rect(center=(350, 350))
        screen.blit(text_surface, text_rect)
    
    def render_ai_difficulty(self, x, text, toggeled=False):
        mouse_pos = pygame.mouse.get_pos()
        
        font = pygame.font.Font(None, 22)
        if (x <= mouse_pos[0] <= x + 84 and 42 <= mouse_pos[1] <= 63) or toggeled:
            pygame.draw.rect(screen, '#d6d6d6', (x, 42, 84, 21), border_radius=5)
            text_surface = font.render(text, True, '#3e3d4a') 
        else:
            pygame.draw.rect(screen, '#454545', (x, 42, 84, 21), border_radius=5)
            text_surface = font.render(text, True, (255, 255, 255)) 
        
        text_rect = text_surface.get_rect(center=(x + 42, 52.5))
        screen.blit(text_surface, text_rect)


class Board:
    def __init__(self) -> None:
        self.board = [0] * 9
    
    def game_winner(self, player, square):
        if self.board.count(0) <= 5:
            row_ind = square // 3
            row = self.board[row_ind * 3: (row_ind + 1) * 3]
            if all(spot == player for spot in row):
                return 'h', row_ind
            
            col_ind = square % 3
            col = [self.board[col_ind + i * 3] for i in range(3)]
            if all(spot == player for spot in col):
                return 'v', col_ind
            
            if square % 2 == 0:
                asc_diagonal = [self.board[i] for i in [2, 4, 6]]
                if all(spot == player for spot in asc_diagonal):
                    return 'a'
                
                desc_diagonal = [self.board[i] for i in [0, 4, 8]]
                if all(spot == player for spot in desc_diagonal):
                    return 'd'
        
        return 0
    
    def is_available(self, square):
        return self.board[square] == 0
    
    def available_squares(self):
        return [i for i, square in enumerate(self.board) if square == 0]
    
    def reset(self):
        self.board = [0 for _ in range(9)]


class AI:
    def easy(self, board):
        winning_squares, blocking_squares = [], []
        
        if len(board.available_squares()) in [1, 7, 8, 9]:
            return random.choice(board.available_squares())
        
        if len(board.available_squares()) < 6:
            for square in board.available_squares():
                board_copy = copy.deepcopy(board)
                board_copy.board[square] = -1
                if board_copy.game_winner(-1, square):
                    winning_squares.append(square)
        
        for square in board.available_squares():
            board_copy = copy.deepcopy(board)
            board_copy.board[square] = 1
            if board_copy.game_winner(1, square):
                blocking_squares.append(square)
        
        filtered_squares = [square for square in board.available_squares()
        if square not in winning_squares and square not in blocking_squares]
        
        if filtered_squares:
            return random.choice(filtered_squares)
        elif blocking_squares:
            blocking_not_winning = [square for square in blocking_squares if square not in winning_squares]
            return random.choice(blocking_not_winning) if blocking_not_winning else random.choice(blocking_squares)
        else:
            return random.choice(winning_squares)
    
    def medium(self, board):
        winning_squares, blocking_squares = [], []
        
        if len(board.available_squares()) in [1, 7, 8, 9]:
            return random.choice(board.available_squares())
        
        if len(board.available_squares()) < 6:
            for square in board.available_squares():
                board_copy = copy.deepcopy(board)
                zxc = board_copy.board
                board_copy.board[square] = -1
                zxc[square] = -1
                if board_copy.game_winner(-1, square):
                    winning_squares.append(square)
        
        for square in board.available_squares():
            board_copy = copy.deepcopy(board)
            zxc = board_copy.board
            board_copy.board[square] = 1
            zxc[square] = 1
            if board_copy.game_winner(1, square):
                blocking_squares.append(square)
        
        
        if winning_squares:
            return random.choice(winning_squares)
        elif blocking_squares:
            return random.choice(blocking_squares)
        else:
            return random.choice(board.available_squares())
    
    def hard(self, board):
        if len(board.available_squares()) == 9:
            return random.choice([0, 2, 4, 6, 8])
        else:
            return self.minimax(board, -1)['position']
    
    def minimax(self, board, player):
        maximizer = -1
        other_player = 1 if player == -1 else -1
        
        if board.winner == other_player:
            return {'position': None,
                    'score': 1 * (len(board.available_squares()) + 1) if other_player == maximizer
                    else -1 * (len(board.available_squares()) + 1)}
        elif not board.available_squares():
            return {'position': None, 'score': 0}
        
        best = {'position': None, 'score': -math.inf if player == maximizer else math.inf}
        
        for square in board.available_squares():
            board.board[square] = player
            board.game_winner(player, square)
            sim_score = self.minimax(board, other_player)
            
            board.board[square] = 0
            board.winner = None
            sim_score['position'] = square
            
            if player == maximizer:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best


class TicTacToe:
    def __init__(self) -> None:
        self.default_values()
        self.display = Display()
    
    def default_values(self):
        self.ai = AI()
        self.player = 1
        self.board = Board()
        self.game_mode = 'pvc'
        self.initial_player = 1
        
        self.game_winner = None
        
        self.pvp_scores = {'Player (X)': 0, 'Tie': 0, 'Player (O)': 0}
        self.pvc_scores = {'Player (X)': 0, 'Tie': 0, 'Computer (O)': 0}
    
    def is_over(self):
        return 0 not in self.board.board or self.game_winner
    
    def change_game_mode(self):
        self.board = Board()
        self.game_winner = None
        self.player = -1 if self.game_mode == 'pvp' else 1
        if self.game_mode == 'pvp':
            self.initial_player = -1
        self.game_mode = 'pvp' if self.game_mode == 'pvc' else 'pvc'

    
    def change_player_turn(self):
        self.player = 1 if self.player == -1 else -1
    
    def mark_square(self, player, square):
        if self.board.is_available(square) and not self.game_winner:
            self.board.board[square] = player
            game_winner = self.board.game_winner(player, square)
            if game_winner:
                self.game_winner = game_winner
                if self.game_mode == 'pvc' and player == 1:
                    self.pvc_scores['Player (X)'] += 1
                elif self.game_mode == 'pvc' and player == -1:
                    self.pvc_scores['Computer (O)'] += 1
                elif self.game_mode == 'pvp' and player == 1:
                    self.pvp_scores['Player (X)'] += 1
                elif self.game_mode == 'pvp' and player == -1:
                    self.pvp_scores['Player (O)'] += 1
            elif self.is_over():
                self.game_winner = 'n'
                if self.game_mode == 'pvc':
                    self.pvc_scores['Tie'] += 1
                elif self.game_mode == 'pvp':
                    self.pvp_scores['Tie'] += 1
            self.change_player_turn()
    
    def next_game(self):
        self.board.reset()
        self.game_winner = None
        self.player = 1 if self.initial_player == -1 else -1
        self.initial_player = 1 if self.initial_player == -1 else -1


def run_tictactoe():
    tictactoe = TicTacToe()

    easy_toggle, medium_toggle, hard_toggle = False, True, False

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if tictactoe.game_mode == 'pvc' and tictactoe.player == -1 and not tictactoe.is_over():
                if easy_toggle:
                    tictactoe.mark_square(-1, tictactoe.ai.easy(tictactoe.board))
                elif medium_toggle:
                    tictactoe.mark_square(-1, tictactoe.ai.medium(tictactoe.board))
                else:
                    tictactoe.mark_square(-1, tictactoe.ai.hard(tictactoe.board))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 17.5 <= mouse_pos[0] <= 87.5 and 17.5 <= mouse_pos[1] <= 87.5:
                    from menu import main  # type: ignore
                    main()
                elif 87.5 <= mouse_pos[0] <= 157.5 and 17.5 <= mouse_pos[1] <= 87.5:
                    easy_toggle, medium_toggle, hard_toggle = False, True, False
                    tictactoe.default_values()
                elif 595 <= mouse_pos[0] <= 651 and 28 <= mouse_pos[1] <= 84:
                    tictactoe.change_game_mode()
                elif 294 <= mouse_pos[0] <= 406 and 322 <= mouse_pos[1] <= 364 and tictactoe.game_winner:
                    tictactoe.next_game()
                elif 210 < mouse_pos[0] <= 294 and 42 <= mouse_pos[1] <= 63 and tictactoe.game_mode == 'pvc':
                    easy_toggle, medium_toggle, hard_toggle = True, False, False
                elif 308 < mouse_pos[0] <= 392 and 42 <= mouse_pos[1] <= 63 and tictactoe.game_mode == 'pvc':
                    easy_toggle, medium_toggle, hard_toggle = False, True, False
                elif 406 < mouse_pos[0] <= 490 and 42 <= mouse_pos[1] <= 63 and tictactoe.game_mode == 'pvc':
                    easy_toggle, medium_toggle, hard_toggle = False, False, True
                else:
                    for square, position in SQUARES_POSITIONS.items():
                        if position[0] <= mouse_pos[0] <= position[0] + 136.5 and position[1] <= mouse_pos[1] <= position[1] + 136.5:
                            tictactoe.mark_square(tictactoe.player, square)

        if tictactoe.game_mode == 'pvc':
            tictactoe.display.render(tictactoe.board.board, tictactoe.game_mode, tictactoe.pvc_scores, tictactoe.game_winner, easy_toggle, medium_toggle, hard_toggle)
        else:
            tictactoe.display.render(tictactoe.board.board, tictactoe.game_mode, tictactoe.pvp_scores, tictactoe.game_winner)

        pygame.display.update()

if __name__ == '__main__':
    run_tictactoe()
