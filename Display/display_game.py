import pygame
from pygame.locals import *
from User.define_user import User
from Display.define_display import Display
from define_ellermaze import Maze
from User.define_character import Character

def print_text(text, position, color = (255, 255, 255)):
	printed = User.font.render(text, True, color)
	printed_width, printed_height = printed.get_size()
	User.Display.blit(printed, (position[0] * printed_width, position[1] * printed_height))

def display_stats():
	if User.clock.get_fps() < 40:
		print_text("FPS: "+f'{User.clock.get_fps() :.1f}', [0, 0], (255, 60, 60))
		return
	print_text("FPS: "f'{User.clock.get_fps() :.1f}', [0, 0], (60, 255, 60))
	print_text("Character Position: ("+str(Character.position[0])+", "+str(Character.position[1])+")", [0, 1], (60, 60, 255))
	print_text("Target Position: ("+str(Character.targetPosition[0])+", "+str(Character.targetPosition[1])+")", [0, 2], (60, 60, 255))
	print_text("Mouse Position: ("+str(Character.mousePosition[0])+", "+str(Character.mousePosition[1])+")", [0, 3], (60, 60, 255))

def display_character():
	tileSize = (Display.DisplayWidth - (Display.ScreenOffset[0] * 2)) / (Maze.size + 2)
	totalOffset = [tileSize * 1 / 8 + Display.ScreenOffset[0] + tileSize, tileSize * 1 / 8 + Display.ScreenOffset[1] + tileSize]
	outlineRect = (Character.position[0] * tileSize + totalOffset[0], Character.position[1] * tileSize + totalOffset[1], tileSize * 3 / 4, tileSize * 3 / 4)
	pygame.draw.rect(User.Display,  (255, 60, 60), outlineRect)

def display_target():
	tileSize = (Display.DisplayWidth - (Display.ScreenOffset[0] * 2)) / (Maze.size + 2)
	totalOffset = [Display.ScreenOffset[0] + tileSize, Display.ScreenOffset[1] + tileSize]
	outlineRect = (Character.targetPosition[0] * tileSize + totalOffset[0], Character.targetPosition[1] * tileSize + totalOffset[1], tileSize, tileSize)
	pygame.draw.rect(User.Display,  (60, 60, 255), outlineRect)

def draw_numberMaze():
	tileSize = (Display.DisplayWidth - (Display.ScreenOffset[0] * 2)) / (Maze.size + 2)
	for col in range(Maze.size):
		yOffset = col * tileSize + Display.ScreenOffset[1] + tileSize
		if yOffset < -tileSize or yOffset > Display.DisplayHeight + tileSize:
			continue
		for row in range(Maze.size):
			xOffset = row * tileSize + Display.ScreenOffset[0] + tileSize
			if xOffset < -tileSize or xOffset > Display.DisplayWidth + tileSize:
				continue
			outlineRect = (xOffset, yOffset, tileSize, tileSize)
			if Character.numberMaze[col][row][1]:
				color = (0, 255, 0)
			else:
				color = (Character.numberMaze[col][row][0], 0, Character.numberMaze[col][row][0])
			pygame.draw.rect(User.Display,  color, outlineRect)

def draw_box(box, position, tileSize, size):
	if box[0] and box[1] and box[2] and box[3]:
		return
	wallWidth = round((9 / size) / 20 * tileSize)
	if wallWidth < 1:
		wallWidth = 1
	if box[0] == 1:
		pygame.draw.line(User.Display, Display.wallColor, (position[0], position[1] + tileSize), (position[0] + tileSize, position[1] + tileSize), wallWidth)
	if box[1] == 1:
		pygame.draw.line(User.Display, Display.wallColor, (position[0], position[1]), (position[0] + tileSize, position[1]), wallWidth)
	if box[2] == 1:
		pygame.draw.line(User.Display, Display.wallColor, (position[0], position[1]), (position[0], position[1] + tileSize), wallWidth)
	if box[3] == 1:
		pygame.draw.line(User.Display, Display.wallColor, (position[0] + tileSize, position[1]), (position[0] + tileSize, position[1] + tileSize), wallWidth)

def draw_maze(Maze, displayWidth = Display.DisplayWidth):
	if Maze == None:
		return
	tileSize = (Display.DisplayWidth - (Display.ScreenOffset[0] * 2)) / (Maze.size + 2)
	for col in range(Maze.size):
		yOffset = col * tileSize + Display.ScreenOffset[1] + tileSize
		if yOffset < -tileSize or yOffset > Display.DisplayHeight + tileSize:
			continue
		for row in range(Maze.size):
			xOffset = row * tileSize + Display.ScreenOffset[0] + tileSize
			if xOffset < -tileSize or xOffset > Display.DisplayWidth + tileSize:
				continue
			draw_box(Maze.maze[col][row], [xOffset, yOffset], tileSize, Maze.size)

def display_game():
	pygame.draw.rect(User.Display, Display.floorColor, (0, 0, Display.DisplayWidth, Display.DisplayHeight))
	if Display.displayStats:
		display_stats()
	draw_numberMaze()
	display_target()
	draw_maze(Maze)
	display_character()
