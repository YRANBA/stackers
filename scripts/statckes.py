from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
import random

sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640,480))
		self.gaming = True
	
	def startGame(self):
		pygame.time.set_timer(USEREVENT +1, 800)
		x = 0
		v = 1
		row = 7
		while self.gaming:

			if not v == 0 and row >= 0:
				#sense.set_pixel((x-v)%8,row, (0,0,0) )
				sense.set_pixel(x,row, (0,0,255) )
				time.sleep(.05)
				sense.set_pixel(x,row, (0,0,0) )
				time.sleep(.05)
				x = (x+v)%7
			elif row >= 0:
				sense.set_pixel(x,row, (0,0,255) )
				v = 1
				x += 1
				row -= 1

			for event in pygame.event.get():
				if event.type == KEYDOWN:
					v = 0

if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
