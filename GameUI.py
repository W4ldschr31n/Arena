import random, pygame, sys
from pygame.locals import *
from Arena.environments.Coliseum import Coliseum
from Arena.controllers.FightController import FightController

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

FONT = pygame.font.Font('freesansbold.ttf', 16)
FONTCOLOR = (255, 255, 255)
BGCOLOR = (50,50,50)
def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	pygame.display.set_caption('Arena')
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

	COLISEUM = Coliseum()
	FIGHTCONTROLLER = FightController(COLISEUM, [])
	while True: #Main game loop
		DISPLAYSURF.fill(BGCOLOR)

		
		for event in pygame.event.get():
		    if event.type == QUIT:
		        pygame.quit()
		        sys.exit()

		pygame.display.update()
		FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()

