from os import getcwd
from sys import platform
import pygame

from tile import *


class LocalMap:

    _pallette = {(100, 200, 0, 255): {'group': 'tiles', 'type': 'grass'},
                 (5, 120, 155, 255): {'group': 'walls', 'type': 'water'},
                 (145, 145, 145, 255): {'group': 'walls', 'type': 'wall'},
                 (0, 0, 0, 255): {'group': 'npcs', 'type': 'grass'},
                 (255, 255, 255, 255): {'group': 'player', 'type': 'grass'}}

    def __init__(self, level_path, screen, block_size=32):

        if platform == 'windows':
            lvl_dir = "\\data\\level\\"
        else:
            lvl_dir = '/data/level/'

        self.level_path = getcwd() + lvl_dir + level_path
        self.block_size = block_size

        self.tiles = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.npcs = []

        self.map_image = pygame.image.load(self.level_path)
        x, y = self.map_image.get_size()
        self.map_size = (x * block_size, y * block_size)

        self.screen = screen

    def update(self, dt=(pygame.time.Clock().tick(60) / 1000.)):
        self.tiles.update()
        self.walls.update()
        # self.player.update()

        pygame.display.flip()

        # collide = pygame.sprite.spritecollide
        # for cell in collide(self.player, self.walls, False):
        #     pass

    def __generate_map__(self):
        for j in range(self.map_image.get_height()):
            for i in range(self.map_image.get_width()):
                current_pixel = self.map_image.get_at((i, j))
                if tuple(current_pixel) in LocalMap._pallette:
                    self.__import_pixel__(tuple(current_pixel), i, j)

    def __import_pixel__(self, pixel, x, y):
        path = getcwd() + '/data/tiles/'
        path += LocalMap._pallette[pixel]['type'] + '.png'

        t = Tile(x * self.block_size,
                 y * self.block_size,
                 path ,
                 self.screen,
                 (self.block_size, self.block_size))

        t.add(self.__dict__[LocalMap._pallette[pixel]['group']])
