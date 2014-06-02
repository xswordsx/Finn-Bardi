import unittest
import os
import sys
from random import randint

sys.path.append(os.path.abspath('..'))

from player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(randint(0, 50), randint(0, 50), 'Finn')

    def test_attributes(self):
        player = Player(5, 6, 'gooby')
        self.assertTrue(player.pos[0] >= 0)
        self.assertTrue(player.pos[1] >= 0)
        self.assertEqual(player.name, 'gooby')
        self.assertEqual(player.direction, 'down')

    def test_player_movement(self):

        old_position = self.player.pos[:]
        self.player.move('down')
        self.assertEqual(old_position[0] + 0, self.player.pos[0])
        self.assertEqual(old_position[1] + 1, self.player.pos[1])

        old_position = self.player.pos[:]
        self.player.move('not really a direction')
        self.assertEqual(self.player.pos, old_position)
