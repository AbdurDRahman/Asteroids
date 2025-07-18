from circleshape import *
import random 
from constants import (ASTEROID_MAX_RADIUS , ASTEROID_MIN_RADIUS )

class Asteroid(CircleShape):
    def __init__ (self, x,y,radius):
        super().__init__(x,y,radius)
    
    def draw (self , screen):
        pygame.draw.circle(screen , "white" , self.position , self.radius , 2)
    
    def  update (self , dt):
        self.position += self.velocity * dt 
    
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS): return 
        random_number = random.uniform(20,50)
        first_child_velocity = self.velocity.rotate(random_number) * 1.2
        second_child_velocity = self.velocity.rotate(-random_number) *1.2
        first_asteroid = Asteroid(self.position.x , self.position.y , self.radius - ASTEROID_MIN_RADIUS)
        second_asteroid = Asteroid(self.position.x , self.position.y , self.radius - ASTEROID_MIN_RADIUS)
        first_asteroid.velocity = first_child_velocity 
        second_asteroid.velocity = second_child_velocity 

        
