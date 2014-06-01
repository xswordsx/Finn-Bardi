import pygame


class Player(pygame.sprite.Sprite):

    DIRECTION = {'down': (0, 1),
                 'up': (0, -1),
                 'left': (-1, 0),
                 'right': (1, 0)}

    def __init__(self, x=0, y=0, name, *groups):
        super(Player, self).__init__(*groups)
        self.direction = 'down'
        self.name = name
        self.pos = [x, y]

    def move(dir):
        if DIRECTION.get(dir):
            self.pos[0] += DIRECTION[dir][0]
            self.pos[1] += DIRECTION[dir][1]
            self.direction = dir
        else:
            pass
