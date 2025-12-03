import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Get rid of original asteroid
        self.kill()
        # Make two smaller asteroids to replace it
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            toggle = True
            for _ in range(ASTEROID_SPLIT_COUNT):
                if toggle:
                    direction = 1
                    toggle = False
                else:
                    direction = -1
                    toggle = True
                new_radius = self.radius - ASTEROID_MIN_RADIUS
                new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                new_velocity = self.velocity.rotate(direction*random.uniform(20, 50))*ASTEROID_SPEEDUP_FACTOR
                new_asteroid.velocity = new_velocity
