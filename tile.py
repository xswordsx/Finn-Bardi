import pygame


class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y, tile_image_path, surface, block_size):

        pygame.sprite.Sprite.__init__(self)

        self.__position = (x, y)

        self.__image = pygame.image.load(tile_image_path)
        self.__image = pygame.transform.scale(self.__image, block_size)
        self.__image.convert()

        self.__surface = surface

        self.rect = self.__image.get_rect()
        self.rect.topleft = self.__position

    def update(self):
        self.__surface.blit(self.__image, self.__position)
