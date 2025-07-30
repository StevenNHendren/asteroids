# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

BLACK = (0, 0, 0)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    ret = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #rect = pygame.Surface.fill(color(0,0,0))
        screen.fill(BLACK)
        pygame.display.flip()

if __name__ == "__main__":
    main()
