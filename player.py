import pygame


class Player(pygame.sprite.Sprite):

    DIRECTION = {'down' : (0, 1),
                 'up' : (0, -1),
                 'left' : (-1, 0),
                 'right' : (1, 0)}

    def __init__(self, x=0, y=0, *groups):
        super(Player, self).__init__(*groups)
        self.pos = [x, y]
        self.direction = DIRECTION['down']
