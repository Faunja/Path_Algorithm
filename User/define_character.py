import pygame
from pygame.locals import *
from User.define_user import User
from Display.define_display import Display
from define_ellermaze import Maze

class define_Character:
	def create_numberMaze(self):
		self.numberMaze = []
		for row in range(Maze.size):
			self.numberMaze.append([])
			for column in range(Maze.size):
				self.numberMaze[row].append([0, False])
		self.numberMaze[self.position[1]][self.position[0]][0] = 1

	def return_mousePosition(self):
		position = pygame.mouse.get_pos()
		tileSize = (Display.DisplayWidth - (Display.ScreenOffset[0] * 2)) / (Maze.size + 2)
		mousePosition = [int((position[0] - Display.ScreenOffset[0]) / tileSize) - 1, int((position[1] - Display.ScreenOffset[1]) / tileSize) - 1]
		if mousePosition[0] < 0:
			mousePosition[0] = 0
		if mousePosition[1] < 0:
			mousePosition[1] = 0
		return mousePosition

	def __init__(self):
		self.position = [0, 0]
		self.targetPosition = [0, 0]
		self.mousePosition = self.return_mousePosition()
		
		self.path = False
		self.create_numberMaze()
	
	def check_numberMaze(self):
		for col in range(Maze.size):
			for row in range(Maze.size):
				if [row, col] == self.targetPosition and self.numberMaze[col][row][0] != 0:
					self.numberMaze[col][row][1] = True
					return False
		return True

	def check_number(self, row, col):
		if self.numberMaze[col][row][0] == 0:
			return
		if col != Maze.size - 1:
			if self.numberMaze[col + 1][row][0] == 0:
				if not Maze.maze[col][row][0]:
					self.numberMaze[col + 1][row][0] = self.numberMaze[col][row][0] + 1

		if col != 0:
			if self.numberMaze[col - 1][row][0] == 0:
				if not Maze.maze[col][row][1]:
					self.numberMaze[col - 1][row][0] = self.numberMaze[col][row][0] + 1

		if row != 0:
			if self.numberMaze[col][row - 1][0] == 0:
				if not Maze.maze[col][row][2]:
					self.numberMaze[col][row - 1][0] = self.numberMaze[col][row][0] + 1

		if row != Maze.size - 1:
			if self.numberMaze[col][row + 1][0] == 0:
				if not Maze.maze[col][row][3]:
					self.numberMaze[col][row + 1][0] = self.numberMaze[col][row][0] + 1

	def check_path(self, row, col):
		if not self.numberMaze[col][row][1]:
			return
		if col != Maze.size - 1:
			if not self.numberMaze[col + 1][row][1] and self.numberMaze[col + 1][row][0] != 0 and self.numberMaze[col + 1][row][0] < self.numberMaze[col][row][0]:
				if not Maze.maze[col][row][0]:
					self.numberMaze[col + 1][row][1] = True

		if col != 0:
			if not self.numberMaze[col - 1][row][1] and self.numberMaze[col - 1][row][0] != 0 and self.numberMaze[col - 1][row][0] < self.numberMaze[col][row][0]:
				if not Maze.maze[col][row][1]:
					self.numberMaze[col - 1][row][1] = True

		if row != 0:
			if not self.numberMaze[col][row - 1][1] and self.numberMaze[col][row - 1][0] != 0 and self.numberMaze[col][row - 1][0] < self.numberMaze[col][row][0]:
				if not Maze.maze[col][row][2]:
					self.numberMaze[col][row - 1][1] = True

		if row != Maze.size - 1:
			if not self.numberMaze[col][row + 1][1] and self.numberMaze[col][row + 1][0] != 0 and self.numberMaze[col][row + 1][0] < self.numberMaze[col][row][0]:
				if not Maze.maze[col][row][3]:
					self.numberMaze[col][row + 1][1] = True

	def move_character(self):
		if Character.position[1] != Maze.size - 1:
			if self.numberMaze[Character.position[1] + 1][Character.position[0]][1] and self.numberMaze[Character.position[1] + 1][Character.position[0]][0] > self.numberMaze[Character.position[1]][Character.position[0]][0]:
				self.position[1] += 1
				return

		if Character.position[1] != 0:
			if self.numberMaze[Character.position[1] - 1][Character.position[0]][1] and self.numberMaze[Character.position[1] - 1][Character.position[0]][0] != 0 and self.numberMaze[Character.position[1] - 1][Character.position[0]][0] > self.numberMaze[Character.position[1]][Character.position[0]][0]:
				self.position[1] -= 1
				return

		if Character.position[0] != 0:
			if self.numberMaze[Character.position[1]][Character.position[0] - 1][1] and self.numberMaze[Character.position[1]][Character.position[0] - 1][0] != 0 and self.numberMaze[Character.position[1]][Character.position[0] - 1][0] > self.numberMaze[Character.position[1]][Character.position[0]][0]:
				self.position[0] -= 1
				return

		if Character.position[0] != Maze.size - 1:
			if self.numberMaze[Character.position[1]][Character.position[0] + 1][1] and self.numberMaze[Character.position[1]][Character.position[0] + 1][0] != 0 and self.numberMaze[Character.position[1]][Character.position[0] + 1][0] > self.numberMaze[Character.position[1]][Character.position[0]][0]:
				self.position[0] += 1
				return

	def check_position(self):
		if self.position != self.targetPosition and not self.numberMaze[self.position[1]][self.position[0]][1]:
			for col in range(Maze.size):
				for row in range(Maze.size):
					if self.check_numberMaze():
						self.check_number(row, col)
					else:
						self.check_path(row, col)
		elif self.position != self.targetPosition:
			self.move_character()

	def update_character(self):
		self.mousePosition = self.return_mousePosition()
		self.check_position()

Character = define_Character()
