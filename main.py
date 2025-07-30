# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

BLACK = (0, 0, 0)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    ret = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gclock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #rect = pygame.Surface.fill(color(0,0,0))
        screen.fill(BLACK)
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()
        tick_ret = gclock.tick(60)
        dt = tick_ret / 1000
        

if __name__ == "__main__":
    main()
