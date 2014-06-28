import pygame
from localmap import LocalMap

pygame.init()

screen = pygame.display.set_mode((640, 480))

map = LocalMap('1.bmp', screen, 32)
map.__generate_map__()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    map.update()

