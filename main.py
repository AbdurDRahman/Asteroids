# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import * 
from asteroidfield import *
from shot import *
def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
   
    clock = pygame.time.Clock() 
    dt = 0.0
   
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteriods,updateable,drawable)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable,drawable)
    Shot.containers = (updateable,drawable,shots)
    gamer = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()
    while(True):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(0x000000)  
        
        for obj in drawable:
            obj.draw(screen)
        for asteroid in asteriods:
            if(gamer.checkCollision(asteroid)):
                print("Game Over")
                return 
            for shot in shots :
                if(shot.checkCollision(asteroid)):
                    shot.kill()
                    asteroid.split()
        
        pygame.display.flip()
        updateable.update(dt)
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()

