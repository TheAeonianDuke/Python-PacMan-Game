import pygame
from pygame.locals import *
from numpy import loadtxt
import time
import pathlib

#Constants for the game
WIDTH, HEIGHT = (32, 32)
WALL_COLOR = pygame.Color(0, 0, 255, 255) # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255) # RED
COIN_COLOR = pygame.Color(255, 255, 0, 255) # RED
DOWN = (0,1)
RIGHT = (1,0)
TOP = (0,-1)
LEFT = (-1,0)


#Draws a rectangle for the wall
def draw_wall(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])

#Draws a rectangle for the player
def draw_pacman(screen, pos): 
	pixels = pixels_from_points(pos)
	pygame.draw.rect(screen, PACMAN_COLOR, [pixels, (WIDTH, HEIGHT)])

#Draws a rectangle for the coin
def draw_coin(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.rect(screen, COIN_COLOR, [pixels, (WIDTH, HEIGHT)])

#Uitlity functions
def add_to_pos(pos, pos2):
	return (pos[0]+pos2[0], pos[1]+pos2[1])
def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)


#Initializing pygame
pygame.init()
screen = pygame.display.set_mode((320,320), 0, 32)
background = pygame.surface.Surface((320,320)).convert()


#Initializing variables
layout = loadtxt('C:/Users/Abhi/Desktop/IP/Projects/PacMan Game/layout.txt', dtype=str)
rows, cols = layout.shape
pacman_position = (1,1)
background.fill((0,0,0))

# Main game loop 
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	screen.blit(background, (0,0))

	#Draw board from the 2d layout array.
  #In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins
	for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'w':
				draw_wall(screen, pos)
			elif value == 'c':
				draw_coin(screen, pos)

	#Draw the player
	draw_pacman(screen, pacman_position)

	#TODO: Take input from the user and update pacman moving direction, Currently hardcoded to always move down
	move_direction = DOWN

	#Update player position based on movement.
	pacman_position = add_to_pos(pacman_position, move_direction)

	#TODO: Check if player ate any coin, or collided with the wall by using the layout array.
	# player should stop when colliding with a wall
	# coin should dissapear when eating, i.e update the layout array

	#Update the display
	pygame.display.update()

	#Wait for a while, computers are very fast.
	time.sleep(0.1)
