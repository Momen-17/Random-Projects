import os
import sys
import pygame

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add paths relative to Menu's location
sys.path.append(os.path.join(current_dir, '..', 'TicTacToe'))
sys.path.append(os.path.join(current_dir, '..', 'Snake'))
sys.path.append(os.path.join(current_dir, '..', 'Sudoku'))
sys.path.append(os.path.join(current_dir, '..', 'Trivia'))

from trivia import run_trivia        # type: ignore
from tictactoe import run_tictactoe  # type: ignore
from snake import run_snake          # type: ignore
from sudoku import run_sudoku        # type: ignore

# Constants
WIDTH, HEIGHT = 1000, 1000
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

        # Rescale
        self.tictactoe_image = pygame.transform.scale(self.tictactoe_image, (350, 350))
        self.snake_image = pygame.transform.scale(self.snake_image, (350, 350))
        self.sudoku_image = pygame.transform.scale(self.sudoku_image, (350, 350))
        self.trivia_image = pygame.transform.scale(self.trivia_image, (350, 350))

    def display(self):
        self.display_background()
        self.display_title()
        
        self.display_hover_effect(self.tictactoe_image, 115, 150, 350, 350)
        self.display_hover_effect(self.snake_image, 535, 150, 350, 350)
        self.display_hover_effect(self.sudoku_image, 115, 550, 350, 350)
        self.display_hover_effect(self.trivia_image, 535, 550, 350, 350)

    # Display backgound on screen
    def display_background(self):
        screen.blit(self.background, (0, 0))

    # Display title on screen
    def display_title(self):
        font = pygame.font.Font(None, 96)
        text_surface = font.render('GamerPY', True, (255, 255, 255)) # text, antialias, color
        text_rect = text_surface.get_rect(center=(500, 75))
        screen.blit(text_surface, text_rect)

    # Draw rectancgle to put under games images
    def display_rectangle(self, x, y, rect_width, rect_height, color):
        pygame.draw.rect(
            surface=screen,
            color=color,
            rect=(x, y, rect_width, rect_height),
            border_radius=50,
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
        if pygame.Rect(115, 150, 350, 350).collidepoint(mouse_pos):
            run_tictactoe()
        elif pygame.Rect(535, 150, 350, 350).collidepoint(mouse_pos):
            run_snake()
        elif pygame.Rect(115, 550, 350, 350).collidepoint(mouse_pos):
            run_sudoku()
        elif pygame.Rect(535, 550, 350, 350).collidepoint(mouse_pos):
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
