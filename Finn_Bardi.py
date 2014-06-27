from state_machine import StateMachine
from localmap import LocalMap
from menu import Menu
import pygame

game = StateMachine(800, 600, 'Finn bardi')

menu = Menu(['Start', 'Exit'], game._StateMachine__screen)
menu.set_colors((255,255,255), (50, 50, 50), (0,0,0))

def start_game(self):
    level_one = LocalMap('1.bmp', game._StateMachine__screen)
    game.push(level_one)

def stop_game(self):
    pygame.display.quit()
    sys.exit()

commands = {}
commands[0] = start_game
commands[1] = stop_game

menu.set_position_commands(commands)

game.push(menu)
menu._initial_draw()
game.start()