import pygame
from pygame.locals import *
from User.define_user import User
from User.define_controls import Controls
from Display.define_display import Display
from User.define_character import Character

def event_handler():
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				Character.targetPosition = Character.mousePosition
				Character.create_numberMaze()

		if event.type == pygame.KEYDOWN:
			if event.key == Controls.quitGame:
				User.playing = False

			if event.key in Controls.changedisplayStats:
				Display.displayStats = not Display.displayStats
			if event.key in Controls.changeTime:
				Display.change_time()
			if event.key in Controls.fullscreen:
				Display.toggle_fullscreen()

		if event.type == pygame.VIDEORESIZE:
			width, height = event.size
			Display.change_displaySize(width, height)
		if event.type == pygame.QUIT:
			User.playing = False

	Character.update_character()

