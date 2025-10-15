from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.radius = radius

	def draw(self, screen):
		pygame.draw.circle(screen, "white",self.position ,self.radius, width = 2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			d = random.uniform(20,50)

			split_v_one = self.velocity.rotate(d) * 1.2
			split_v_two = self.velocity.rotate(-d) * 1.2
			split_r = self.radius - ASTEROID_MIN_RADIUS

			a1 = Asteroid(self.position.x, self.position.y, split_r)
			a1.velocity = split_v_one

			a2 = Asteroid(self.position.x, self.position.y, split_r)
			a2.velocity = split_v_two

			self.kill()