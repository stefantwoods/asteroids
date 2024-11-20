import pygame
from constants import *
from player import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player1 = player(x,y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Move the player
        player1.update(dt)

        # Make the entire screen black
        screen.fill((0,0,0))

        # Draw the player
        player1.draw(screen)

        # Update the screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
