import unittest
import pygame
import os
import sys

sys.path.append(os.path.abspath('..'))

from tile import Tile


class TestTile(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((32, 32))
        self.tile = Tile(0, 0, 'data/tiles/wall.png', self.screen, (32, 32))

    def test_blitting(self):
        self.tile.update()
        pygame.display.flip()
        pygame.time.Clock().tick(2)
