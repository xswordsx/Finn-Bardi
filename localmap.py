from os import getcwd
from system import platform
import pygame


class LocalMap:

    def __init__(self, level_path, block_size=32):
        lvl_dir = "\\level\\" if platform == 'windows' else '/level/'
        self.level_path = getcwd() + level_path
        self.block_size = block_size
        self.tiles = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = None
        self.map_image = pygame.image.load(self.level_path)
        x, y = *self.map_image.get_size()
        self.map_size = (x * block_size, y * block_size)

    def update(self, dt=(pygame.time.Clock().tick(30) / 1000.))
        self.walls.update()
        self.tiles.update()
        self.player.update()
        collide = pygame.sprite.spritecollide
        for cell in collide(self.player, self.walls, False):
            collide_player_with_mobs(not_yet_done)
