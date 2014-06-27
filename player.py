import pygame


class Player(pygame.sprite.Sprite):

    __DIRECTION = {'down': (0, 1),
                   'up': (0, -1),
                   'left': (-1, 0),
                   'right': (1, 0)}

    def __init__(self, x, y, name, *groups):
        super(Player, self).__init__(*groups)
        self.direction = 'down'
        self.name = name
        self.position = [x, y]

        self.inventory = {'left hand': None,
                          'right hand': None,
                          'head': None,
                          'torso': None
                          'legs': None,
                          'feet': None,
                          'arms': None
                          'neck': None,
                          'stash': []}
        self.inventory_weight = 0
        self.stats = {'strength': 15,
                      'dexterity': 10,
                      'intelligence': 12,
                      'health': 80,
                      'mana': 40}

    def move(self, dir):
        if Player.__DIRECTION.get(dir):
            self.position[0] += Player.__DIRECTION[dir][0]
            self.position[1] += Player.__DIRECTION[dir][1]
            self.direction = dir
        else:
            pass

    def inflict_damage(self):
        # pending formula
        pass

    def take_damage(self):
        # pending formula
        pass

    def collect_loot(selfm, monster):
        # XP from enemy gets transfered to player
        # player is able to grab items
        pass
