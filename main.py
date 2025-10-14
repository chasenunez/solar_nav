import pygame
from constants import *
from player import *

def main():
	print("Starting Asteroids!")
	pygame.init()
	
	screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	Clock = pygame.time.Clock()
	dt = 0

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	
	while True:
		for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return
			
		screen.fill("black")
		Player.draw(Player(x,y), screen)
		pygame.display.flip()
		dt = (Clock.tick(60)*1000)
if __name__ == "__main__":
	main()
