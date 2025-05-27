import pygame, os, pickle
from pygame.locals import *
from User.define_user import User
from Display.display_game import display_game
from event_handler import event_handler

def main():
	while User.playing:
		User.clock.tick(User.FPS)
		event_handler()
		display_game()
		pygame.display.update()
	pygame.quit()

main()
