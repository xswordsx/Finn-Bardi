import unittest
import pygame
import '../player'


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
