import os
import sys
import pygame

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add paths relative to current location
sys.path.append(os.path.join(current_dir, '..', 'Menu'))

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('GamerPy')
# screen.fill((0, 0, 0))


class Trivia:
    def __init__(self) -> None:
        pass


def run_trivia():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

if __name__ == '__main__':
    run_trivia()