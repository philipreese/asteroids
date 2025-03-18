import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def update(self, dt):
    self.position += (self.velocity * dt)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    angle = random.uniform(20, 50)
    small_radius = self.radius - ASTEROID_MIN_RADIUS
    asteroid1 = Asteroid(self.position.x, self.position.y, small_radius)
    asteroid2 = Asteroid(self.position.x, self.position.y, small_radius)
    asteroid1.velocity = self.velocity.rotate(angle) * 1.2
    asteroid2.velocity = self.velocity.rotate(-angle) * 1.2