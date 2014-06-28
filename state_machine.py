import pygame
from localmap import LocalMap


class StateMachine:

    def __init__(self, width, height, title):
        self.__stack = []
        self.__top = None
        self.__running = False
        self.__screen = pygame.display.set_mode((width, height))
        self.__screen.fill((0, 0, 0))
        pygame.display.set_caption(title)

    def push(self, state):
        self.__stack.append(state)
        self.__top = state

    def update(self):
        self.__top.update()

    def pop(self):
        self.__stack.pop()
        self.__top = self.__stack[0]

    def start(self):

        pygame.display.flip()

        self.__running = True
        while self.__running:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
