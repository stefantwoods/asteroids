import pygame
import sys
from constants import *
from player import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    # Group instantiation
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    player1 = player(x,y)
    asteroidfild_obj = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            player_collision = player1.collision_check(asteroid)
            if player_collision:
                print("Game Over!")
                sys.exit()

            for shot in shots:
                shot_collision = shot.collision_check(asteroid)
                if shot_collision:
                    shot.kill()
                    asteroid.kill()
            

        # Make the entire screen black
        screen.fill((0,0,0))
    
        for obj in drawable:
            obj.draw(screen)

        # Update the screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
