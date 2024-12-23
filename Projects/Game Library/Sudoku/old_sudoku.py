import os
import sys
import copy
import pygame
import random

SQUARE_POSITIONS = {}
for i in range(9):
    for j in range(9):
        SQUARE_POSITIONS[(i, j)] = (27 + 54.5 * j, 154 + 54.5 * i)

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, '..', 'Menu'))

pygame.init()
screen = pygame.display.set_mode((700, 700))


class Display:
    def __init__(self) -> None:
        self.load_resources()
    
    def load_resources(self):
        self.background = pygame.image.load(os.path.join(current_dir, 'assets', 'background.png'))
        self.board = pygame.image.load(os.path.join(current_dir, 'assets', 'Sudoku.png'))
        self.back = pygame.image.load(os.path.join(current_dir, 'assets', 'back.png'))
        self.reset = pygame.image.load(os.path.join(current_dir, 'assets', 'reset.png'))
        self.back_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'back_hover.png'))
        self.reset_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'reset_hover.png'))
        self.number_1 = pygame.image.load(os.path.join(current_dir, 'assets', 'number_1.png'))
        self.number_1_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'number_1_hover.png'))
        self.number_2 = pygame.image.load(os.path.join(current_dir, 'assets', 'number_2.png'))
        self.number_2_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'number_2_hover.png'))
        self.number_3 = pygame.image.load(os.path.join(current_dir, 'assets', 'number_3.png'))
        self.number_3_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'number_3_hover.png'))
        self.number_4 = pygame.image.load(os.path.join(current_dir, 'assets', 'number_4.png'))
        self.number_4_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'number_4_hover.png'))
        self.number_5 = pygame.image.load(os.path.join(current_dir, 'assets', 'number_5.png'))
        self.number_5_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'number_5_hover.png'))
        self.number_6 = pygame.image.load(os.path.join(current_dir, 'assets', 'number_6.png'))
        self.number_6_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'number_6_hover.png'))
        self.number_7 = pygame.image.load(os.path.join(current_dir, 'assets', 'number_7.png'))
        self.number_7_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'number_7_hover.png'))
        self.number_8 = pygame.image.load(os.path.join(current_dir, 'assets', 'number_8.png'))
        self.number_8_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'number_8_hover.png'))
        self.number_9 = pygame.image.load(os.path.join(current_dir, 'assets', 'number_9.png'))
        self.number_9_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'number_9_hover.png'))
        self.erase = pygame.image.load(os.path.join(current_dir, 'assets', 'erase.png'))
        self.erase_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'erase_hover.png'))
        self.show_answer = pygame.image.load(os.path.join(current_dir, 'assets', 'show_answer.png'))
        self.show_answer_hover = pygame.image.load(os.path.join(current_dir, 'assets', 'show_answer_hover.png'))
        self.faded_black = pygame.image.load(os.path.join(current_dir, 'assets', 'faded_black.png'))
    
    def render(self, sudoku, selected_square=False, easy_toggle=True, medium_toggle=False, hard_toggle=False, unfair_toggle=False, extreme_toggle=False):
        self.render_background()
        self.render_board()
        
        self.render_buttons_hover()
        
        self.render_option(self.number_1, self.number_1_hover, 540, 195)
        self.render_option(self.number_2, self.number_2_hover, 610, 195)
        self.render_option(self.number_3, self.number_3_hover, 540, 265)
        self.render_option(self.number_4, self.number_4_hover, 610, 265)
        self.render_option(self.number_5, self.number_5_hover, 540, 335)
        self.render_option(self.number_6, self.number_6_hover, 610, 335)
        self.render_option(self.number_7, self.number_7_hover, 540, 405)
        self.render_option(self.number_8, self.number_8_hover, 610, 405)
        self.render_option(self.number_9, self.number_9_hover, 540, 475)
        self.render_option(self.erase, self.erase_hover, 610, 475)
        self.render_show_answer(self.show_answer, self.show_answer_hover, 540, 545)
        
        self.render_selected_square(sudoku, selected_square)
        
        self.render_text('Difficulty:', 72, 120)
        self.render_difficulty('Easy', 124, 110, easy_toggle)
        self.render_difficulty('Medium', 199, 110, medium_toggle)
        self.render_difficulty('Hard', 274, 110, hard_toggle)
        self.render_difficulty('Unfair', 349, 110, unfair_toggle)
        self.render_difficulty('Extreme', 424, 110, extreme_toggle)
        
        self.render_text(f'Mistakes: {sudoku.mistakes}/3', 620, 30)
        
        self.render_numbers(sudoku)
        
        if sudoku.mistakes == 3:
            self.render_max_mistakes()
        elif sudoku.solvable_board == sudoku.solved_board:
            self.render_game_won()
    
    def render_background(self):
        screen.blit(self.background, (0, 0))
    
    def render_board(self):
        screen.blit(self.board, (23, 150))
    
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
    
    def render_option(self, option, option_hover, x, y):
        mouse_pos = pygame.mouse.get_pos()
        
        if x <= mouse_pos[0] <= x + 64 and y <= mouse_pos[1] <= y + 64:
            screen.blit(option_hover, (x, y))
        else:
            screen.blit(option, (x, y))
    
    def render_show_answer(self, show_answer, show_answer_hover, x, y):
        mouse_pos = pygame.mouse.get_pos()
        
        if x <= mouse_pos[0] <= x + 138 and y <= mouse_pos[1] <= y + 64:
            screen.blit(show_answer_hover, (x, y))
        else:
            screen.blit(show_answer, (x, y))
    
    def render_selected_square(self, sudoku, selected_square):
        if selected_square:
            row, column = selected_square[0], selected_square[1]
            
            for i in range(9):
                pygame.draw.rect(screen, '#e2ebf3', (26 + 54.7 * i, 153 + 54.7 * row, 52, 52))
            for j in range(9):
                pygame.draw.rect(screen, '#e2ebf3', (26 + 54.7 * column, 153 + 54.7 * j, 52, 52))
            
            subgrid_start_row, subgrid_start_column = row // 3 * 3, column // 3 * 3
            for i in range(subgrid_start_row, subgrid_start_row + 3):
                for j in range(subgrid_start_column, subgrid_start_column + 3):
                    pygame.draw.rect(screen, '#e2ebf3', (26 + 54.7 * j, 153 + 54.7 * i, 52, 52))
            
            if sudoku.solvable_board[row][column] != 0:
                for i in range(9):
                    for j in range(9):
                        if sudoku.solvable_board[i][j] == sudoku.solvable_board[row][column]:
                            pygame.draw.rect(screen, '#c3d7ea', (26 + 54.7 * j, 153 + 54.7 * i, 52, 52))
            
            pygame.draw.rect(screen, '#bbdefb', (26 + 54.7 * column, 153 + 54.7 * row, 52, 52))
    
    def render_text(self, text, x, y, font_size=28, color='white'):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)
    
    def render_difficulty(self, text, x, y, toggle=False):
        mouse_pos = pygame.mouse.get_pos()
        font = pygame.font.Font(None, 24)
        
        if (x <= mouse_pos[0] <= x + 70 and y <= mouse_pos[1] <= y + 20) or toggle:
            pygame.draw.rect(screen, '#00adff', (x, y, 70, 20), border_radius=3)
            text_surface = font.render(text, True, 'white')
        else:
            pygame.draw.rect(screen, '#b1e6ff', (x, y, 70, 20), border_radius=3)
            text_surface = font.render(text, True, 'black')
        
        text_rect = text_surface.get_rect(center=(x+35, y+10))
        screen.blit(text_surface, text_rect)
    
    def render_numbers(self, sudoku):
        font = pygame.font.Font(None, 48)
        
        for row in range(9):
            for col in range(9):
                if sudoku.board[row][col] != 0:
                    text_surface = font.render(str(sudoku.board[row][col]), True, 'black')
                    text_rect = text_surface.get_rect(center=(27 + 26.5 + 54.5 * col, 154 + 26.5 + 54.5 * row))
                    screen.blit(text_surface, text_rect)
                elif sudoku.solvable_board[row][col] != 0 and sudoku.solvable_board[row][col] == sudoku.solved_board[row][col]:
                    text_surface = font.render(str(sudoku.solvable_board[row][col]), True, '#325aaf')
                    text_rect = text_surface.get_rect(center=(27 + 26.5 + 54.5 * col, 154 + 26.5 + 54.5 * row))
                    screen.blit(text_surface, text_rect)
                elif sudoku.solvable_board[row][col] != 0 and sudoku.solvable_board[row][col] != sudoku.solved_board[row][col]:
                    text_surface = font.render(str(sudoku.solvable_board[row][col]), True, '#e55c6c')
                    text_rect = text_surface.get_rect(center=(27 + 26.5 + 54.5 * col, 154 + 26.5 + 54.5 * row))
                    screen.blit(text_surface, text_rect)
    
    def render_max_mistakes(self):
        screen.blit(self.faded_black, (0, 0))
        pygame.draw.rect(screen, 'white', (175, 200, 350, 300), border_radius=15)
        self.render_text('Game Over', 350, 240, font_size=72, color='black')
        self.render_text('You made 3 mistakes', 350, 295, font_size=36, color='black')
        self.render_text('and lost the game', 350, 320, font_size=36, color='black')
        
        pygame.draw.rect(screen, '#5a7bc0', (225, 360, 250, 40), border_radius=5)
        self.render_text('Second Chance', 350, 380, font_size=36, color='white')
        pygame.draw.rect(screen, '#5a7bc0', (225, 420, 250, 40), border_radius=5)
        self.render_text('New Game', 350, 440, font_size=36, color='white')
    
    def render_game_won(self):
        screen.blit(self.faded_black, (0, 0))
        pygame.draw.rect(screen, 'white', (175, 200, 350, 300), border_radius=15)
        self.render_text('Great Job', 350, 240, font_size=72, color='#6a994e')
        self.render_text('You successfully', 350, 295, font_size=36, color='black')
        self.render_text('solved the puzzle', 350, 320, font_size=36, color='black')
        
        pygame.draw.rect(screen, '#5a7bc0', (225, 360, 250, 40), border_radius=5)
        self.render_text('New Game', 350, 380, font_size=36, color='white')
        pygame.draw.rect(screen, '#e36172', (225, 420, 250, 40), border_radius=5)
        self.render_text('Quit', 350, 440, font_size=36, color='white')

class Sudoku:
    def __init__(self, file_name=os.path.join(current_dir, 'seeds', 'Easy.seed')) -> None:
        self.mistakes = 0
        self.display = Display()
        self.board = self.generate_board(file_name)
        self.solvable_board = copy.deepcopy(self.board)
        self.solved_board = copy.deepcopy(self.board)
        self.solve()
    
    def generate_board(self, file_name):
        with open(file_name, 'r') as file:
            line = random.choice(file.readlines())[0:81]
        
        return [list(map(lambda x: int(x) if x.isdigit() else 0, line[i:i+9])) for i in range(0, 81, 9)]
    
    def is_valid(self, row, column, number):
        if number in self.solved_board[row]:
            return False
        
        if number in (self.solved_board[i][column] for i in range(9)):
            return False
        
        subgrid_start_row, subgrid_start_column = row // 3 * 3, column // 3 * 3
        for i in range(subgrid_start_row, subgrid_start_row + 3):
            for j in range(subgrid_start_column, subgrid_start_column + 3):
                if self.solved_board[i][j] == number:
                    return False
        
        return True
    
    def solve(self, row=0, column=0):
        if row == 9:
            return True
        
        elif column == 9:
            return self.solve(row + 1, 0)
        
        elif self.solved_board[row][column] != 0:
            return self.solve(row, column + 1)
        
        else:
            for number in range(1, 10):
                if self.is_valid(row, column, number):
                    self.solved_board[row][column] = number
                    if self.solve(row, column + 1):
                        return True
                    self.solved_board[row][column] = 0
        
        return False
    
    def make_move(self, row, column, number):
        if self.board[row][column] == 0:
            self.solvable_board[row][column] = number
            
            if number != self.solved_board[row][column] and number != 0:
                self.mistakes += 1
    
    def game_over(self):
        return self.solvable_board == self.solved_board or self.mistakes == 3


def run_sudoku():
    sudoku = Sudoku()
    
    difficulty = 'Easy.seed'
    selected_square = None
    easy_toggle, medium_toggle, hard_toggle, unfair_toggle, extreme_toggle = True, False, False, False, False
    
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 17.5 <= mouse_pos[0] <= 87.5 and 17.5 <= mouse_pos[1] <= 87.5:
                    from menu import main  # type: ignore
                    main()
                elif 87.5 <= mouse_pos[0] <= 157.5 and 17.5 <= mouse_pos[1] <= 87.5:
                    sudoku.mistakes = 0
                    selected_square = None
                    sudoku.solvable_board = copy.deepcopy(sudoku.board)
                
                if sudoku.game_over():
                    if sudoku.mistakes == 3:
                        if 225 <= mouse_pos[0] <= 475 and 360 <= mouse_pos[1] <= 400:
                            sudoku.mistakes = 2
                        elif 225 <= mouse_pos[0] <= 475 and 420 <= mouse_pos[1] <= 460:
                            sudoku = Sudoku(os.path.join(current_dir, 'seeds', difficulty))
                    else:
                        if 225 <= mouse_pos[0] <= 475 and 360 <= mouse_pos[1] <= 400:
                            sudoku = Sudoku(os.path.join(current_dir, 'seeds', difficulty))
                        elif 225 <= mouse_pos[0] <= 475 and 420 <= mouse_pos[1] <= 460:
                            running = False
                else:
                    if 124 <= mouse_pos[0] <= 124 + 70 and  110 <= mouse_pos[1] <= 130:
                        difficulty = 'Easy.seed'
                        easy_toggle, medium_toggle, hard_toggle, unfair_toggle, extreme_toggle = True, False, False, False, False
                        sudoku = Sudoku(os.path.join(current_dir, 'seeds', difficulty))
                    elif 199 <= mouse_pos[0] <= 199 + 70 and  110 <= mouse_pos[1] <= 130:
                        difficulty = 'Medium.seed'
                        easy_toggle, medium_toggle, hard_toggle, unfair_toggle, extreme_toggle = False, True, False, False, False
                        sudoku = Sudoku(os.path.join(current_dir, 'seeds', difficulty))
                    elif 274 <= mouse_pos[0] <= 274 + 70 and  110 <= mouse_pos[1] <= 130:
                        difficulty = 'Hard.seed'
                        easy_toggle, medium_toggle, hard_toggle, unfair_toggle, extreme_toggle = False, False, True, False, False
                        sudoku = Sudoku(os.path.join(current_dir, 'seeds', difficulty))
                    elif 349 <= mouse_pos[0] <= 349 + 70 and  110 <= mouse_pos[1] <= 130:
                        difficulty = 'Unfair.seed'
                        easy_toggle, medium_toggle, hard_toggle, unfair_toggle, extreme_toggle = False, False, False, True, False
                        sudoku = Sudoku(os.path.join(current_dir, 'seeds', difficulty))
                    elif 424 <= mouse_pos[0] <= 424 + 70 and  110 <= mouse_pos[1] <= 130:
                        difficulty = 'Extreme.seed'
                        easy_toggle, medium_toggle, hard_toggle, unfair_toggle, extreme_toggle = False, False, False, False, True
                        sudoku = Sudoku(os.path.join(current_dir, 'seeds', difficulty))
                    
                    for square, position in SQUARE_POSITIONS.items():
                        if position[0] <= mouse_pos[0] <= position[0] + 53 and position[1] <= mouse_pos[1] <= position[1] + 53:
                            selected_square = square
                    
                    if selected_square:
                        if (540 <= mouse_pos[0] <= 540 + 64 and 195 <= mouse_pos[1] <= 195 + 64):
                            sudoku.make_move(selected_square[0], selected_square[1], 1)
                        elif (610 <= mouse_pos[0] <= 610 + 64 and 195 <= mouse_pos[1] <= 195 + 64):
                            sudoku.make_move(selected_square[0], selected_square[1], 2)
                        elif (540 <= mouse_pos[0] <= 540 + 64 and 265 <= mouse_pos[1] <= 265 + 64):
                            sudoku.make_move(selected_square[0], selected_square[1], 3)
                        elif (610 <= mouse_pos[0] <= 610 + 64 and 265 <= mouse_pos[1] <= 265 + 64):
                            sudoku.make_move(selected_square[0], selected_square[1], 4)
                        elif (540 <= mouse_pos[0] <= 540 + 64 and 335 <= mouse_pos[1] <= 335 + 64):
                            sudoku.make_move(selected_square[0], selected_square[1], 5)
                        elif (610 <= mouse_pos[0] <= 610 + 64 and 335 <= mouse_pos[1] <= 335 + 64):
                            sudoku.make_move(selected_square[0], selected_square[1], 6)
                        elif (540 <= mouse_pos[0] <= 540 + 64 and 405 <= mouse_pos[1] <= 405 + 64):
                            sudoku.make_move(selected_square[0], selected_square[1], 7)
                        elif (610 <= mouse_pos[0] <= 610 + 64 and 405 <= mouse_pos[1] <= 405 + 64):
                            sudoku.make_move(selected_square[0], selected_square[1], 8)
                        elif (540 <= mouse_pos[0] <= 540 + 64 and 475 <= mouse_pos[1] <= 475 + 64):
                            sudoku.make_move(selected_square[0], selected_square[1], 9)
                        elif (610 <= mouse_pos[0] <= 610 + 64 and 475 <= mouse_pos[1] <= 475 + 64):
                            sudoku.make_move(selected_square[0], selected_square[1], 0)
                        elif (540 <= mouse_pos[0] <= 540 + 138 and 545 <= mouse_pos[1] <= 545 + 64):
                            sudoku.solvable_board[selected_square[0]][selected_square[1]] = sudoku.solved_board[selected_square[0]][selected_square[1]]
            
            if event.type == pygame.KEYDOWN and selected_square and not sudoku.game_over():
                if event.key == pygame.K_1:
                    sudoku.make_move(selected_square[0], selected_square[1], 1)
                elif event.key == pygame.K_2:
                    sudoku.make_move(selected_square[0], selected_square[1], 2)
                elif event.key == pygame.K_3:
                    sudoku.make_move(selected_square[0], selected_square[1], 3)
                elif event.key == pygame.K_4:
                    sudoku.make_move(selected_square[0], selected_square[1], 4)
                elif event.key == pygame.K_5:
                    sudoku.make_move(selected_square[0], selected_square[1], 5)
                elif event.key == pygame.K_6:
                    sudoku.make_move(selected_square[0], selected_square[1], 6)
                elif event.key == pygame.K_7:
                    sudoku.make_move(selected_square[0], selected_square[1], 7)
                elif event.key == pygame.K_8:
                    sudoku.make_move(selected_square[0], selected_square[1], 8)
                elif event.key == pygame.K_8:
                    sudoku.make_move(selected_square[0], selected_square[1], 8)
                elif event.key == pygame.K_9:
                    sudoku.make_move(selected_square[0], selected_square[1], 9)
                elif event.key == pygame.K_BACKSPACE:
                    sudoku.make_move(selected_square[0], selected_square[1], 0)
                elif event.key == pygame.K_LEFT and selected_square[1] != 0:
                    selected_square = (selected_square[0], selected_square[1] - 1)
                elif event.key == pygame.K_RIGHT and selected_square[1] != 8:
                    selected_square = (selected_square[0], selected_square[1] + 1)
                elif event.key == pygame.K_UP and selected_square[0] != 0:
                    selected_square = (selected_square[0] - 1, selected_square[1])
                elif event.key == pygame.K_DOWN and selected_square[0] != 8:
                    selected_square = (selected_square[0] + 1, selected_square[1])
        
        
        sudoku.display.render(sudoku, selected_square, easy_toggle, medium_toggle, hard_toggle, unfair_toggle, extreme_toggle)
        pygame.display.update()

if __name__ == '__main__':
    run_sudoku()
