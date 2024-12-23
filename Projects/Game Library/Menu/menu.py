import os
import sys
import pygame

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, '..', 'TicTacToe'))
sys.path.append(os.path.join(current_dir, '..', 'Snake'))
sys.path.append(os.path.join(current_dir, '..', 'Sudoku'))
sys.path.append(os.path.join(current_dir, '..', 'Trivia'))

from trivia import run_trivia        # type: ignore
from tictactoe import run_tictactoe  # type: ignore
from snake import run_snake          # type: ignore
from sudoku import run_sudoku        # type: ignore

# Constants
WIDTH, HEIGHT = 700, 700
FPS = 60

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GamerPy')



class MenuScreen:
    def __init__(self):
        self.load_resources()

    def load_resources(self):
        # Load images
        self.background = pygame.image.load(os.path.join(current_dir, 'assets', 'Background.png'))
        self.tictactoe_image = pygame.image.load(os.path.join(current_dir, 'assets', 'tictactoe.png'))
        self.snake_image = pygame.image.load(os.path.join(current_dir, 'assets', 'snake.png'))
        self.sudoku_image = pygame.image.load(os.path.join(current_dir, 'assets', 'sudoku.png'))
        self.trivia_image = pygame.image.load(os.path.join(current_dir, 'assets', 'trivia.png'))

    def display(self):
        self.display_background()
        self.display_title()
        
        self.display_hover_effect(self.tictactoe_image, 80.5, 105, 245, 245)
        self.display_hover_effect(self.snake_image, 374.5, 105, 245, 245)
        self.display_hover_effect(self.sudoku_image, 80.5, 409.5, 245, 245)
        self.display_hover_effect(self.trivia_image, 374.5, 409.5, 245, 245)

    # Display backgound on screen
    def display_background(self):
        screen.blit(self.background, (0, 0))

    # Display title on screen
    def display_title(self):
        font = pygame.font.Font(None, 67)
        text_surface = font.render('GamerPY', True, (255, 255, 255)) # text, antialias, color
        text_rect = text_surface.get_rect(center=(350, 52.5))
        screen.blit(text_surface, text_rect)

    # Draw rectancgle to put under games images
    def display_rectangle(self, x, y, rect_width, rect_height, color):
        pygame.draw.rect(
            surface=screen,
            color=color,
            rect=(x, y, rect_width, rect_height),
            border_radius=35,
            )

    # Display hover effect for game images
    def display_hover_effect(self, image, x, y, rect_width, rect_height):
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # GREEN rectangle if mouse hovering on game image else WHITE
        color = (0, 255, 0) if pygame.Rect(x, y, rect_width, rect_height).collidepoint(mouse_pos) else (255, 255, 255)
        self.display_rectangle(x, y, rect_width, rect_height, color)

        # Display the game image
        screen.blit(image, (x, y))
    
    def handle_clicks(self, mouse_pos):
        if pygame.Rect(80.5, 105, 245, 245).collidepoint(mouse_pos):
            run_tictactoe()
        elif pygame.Rect(374.5, 105, 245, 245).collidepoint(mouse_pos):
            run_snake()
        elif pygame.Rect(80.5, 409.5, 245, 245).collidepoint(mouse_pos):
            run_sudoku()
        elif pygame.Rect(374.5, 409.5, 245, 245).collidepoint(mouse_pos):
            run_trivia()


def main():
    menu_screen = MenuScreen()
    clock = pygame.time.Clock()

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Check if quit is pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check if mouse is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                menu_screen.handle_clicks(mouse_pos)

        menu_screen.display()
        pygame.display.update()
        clock.tick(FPS) # Fixate fps to 60


if __name__ == '__main__':
    main()
