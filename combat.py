from state_machine import StateMachine
import pygame


class Combat:

    def __init__(self, game, monster, player):
        self._player = player
        self._game = game
        self._monster = monster

    def fight(self):
        # TODO
        # check dextirity to see who goes first
        # while player and monster are alive
            # inflict damage to one another
        # return (is player alive?)
        pass

    def update(self):
        # draw background over game
        # wait for user input
        # execute user command
            # fight animations
        # if the player is alive
            # pop this out of the state machine
            # and resume as is
            # ELSE----
            # end of game - sorry bud.
        pass

    def check_initiative(self):
        pass

    def draw_bg(self):
        pass

    def menu_prompt(self):
        # This will be the actions menu
        # It should return a value, indicating
        # The action that needs to be executed
        # to the player
        pass

    def player_choice(self, choice):
        # This will be the menu, from which
        # the player will interact with the game
        pass
