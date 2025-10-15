from circleshape import *
from constants import *

class Shot(CircleShape):
	def __init__(self, position, rotation):
		super().__init__(position.x, position.y, SHOT_RADIUS)
		self.radius = SHOT_RADIUS
		self.position = position
		self.rotation = rotation
		self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

	def draw(self, screen):
		pygame.draw.circle(screen, "white",self.position ,self.radius, width = 2)

	def update(self, dt):
		self.position += (self.velocity * dt)