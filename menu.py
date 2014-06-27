'''
@author: avalanchy (at) google mail dot com
@version: 0.1; python 2.7; pygame 1.9.2pre; SDL 1.2.14; MS Windows XP SP3
@date: 2012-04-08
@license: This document is under GNU GPL v3

README on the bottom of document.

@font: from http://www.dafont.com/coders-crux.font
      more abuot license you can find in data/coders-crux/license.txt
'''

import pygame
from pygame.locals import *

if not pygame.display.get_init():
    pygame.display.init()

if not pygame.font.get_init():
    pygame.font.init()


class Menu:
    _list = []
    boxes = []
    font_size = 32
    font_path = 'data/fonts/coders_crux.ttf'
    font = pygame.font.Font
    dest_surface = pygame.Surface
    number_fields = 0
    background_color = (51,51,51)
    text_color =  (255, 255, 153)
    selection_color = (153,102,255)
    selected_item = 0
    drawing_position = (0,0)
    menu_width = 0
    menu_height = 0

    class Field:
        text = ''
        field = pygame.Surface
        field_rect = pygame.Rect
        selected_rect = pygame.Rect

    def move_menu(self, top, left):
        self.drawing_position = (top,left)

    def set_position_commands(self, hashmap):
        self._actions = hashmap.copy()

    def set_colors(self, text, selection, background):
        self.background_color = background
        self.text_color =  text
        self.selection_color = selection
        
    def set_fontsize(self,font_size):
        self.font_size = font_size
        
    def set_font(self, path):
        self.font_path = path
        
    def get_position(self):
        return self.selected_item
    
    def __init__(self, fields, dest_surface):
        self._list = fields
        self.dest_surface = dest_surface
        self.number_fields = len(self._list)
        self.create_structure()        

    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.draw(-1) #here is the Menu class function
                if event.key == K_DOWN:
                    self.draw(1) #here is the Menu class function

                if event.key == K_RETURN:
                    self._actions[self.selected_item](self)
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    sys.exit()
                pygame.display.update()
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()
        
    def draw(self, move=0):
        if move:
            self.selected_item += move 
            if self.selected_item == -1:
                self.selected_item = self.number_fields - 1
            self.selected_item %= self.number_fields
        menu = pygame.Surface((self.menu_width, self.menu_height))
        menu.fill(self.background_color)
        selected_rect = self.boxes[self.selected_item].selected_rect
        pygame.draw.rect(menu,self.selection_color,selected_rect)

        for i in range(self.number_fields):
            menu.blit(self.boxes[i].field,self.boxes[i].field_rect)
        self.dest_surface.blit(menu,self.drawing_position)
        return self.selected_item

    def create_structure(self):
        offset = 0
        self.menu_height = 0
        self.font = pygame.font.Font(self.font_path, self.font_size)
        for i in range(self.number_fields):
            self.boxes.append(self.Field())
            self.boxes[i].text = self._list[i]
            self.boxes[i].field = self.font.render(self.boxes[i].text, 1, self.text_color)

            self.boxes[i].field_rect = self.boxes[i].field.get_rect()
            offset = int(self.font_size * 0.2)

            height = self.boxes[i].field_rect.height
            self.boxes[i].field_rect.left = offset
            self.boxes[i].field_rect.top = offset + (offset * 2 + height) * i

            width = self.boxes[i].field_rect.width + offset * 2
            height = self.boxes[i].field_rect.height + offset * 2
            left = self.boxes[i].field_rect.left - offset
            top = self.boxes[i].field_rect.top - offset

            self.boxes[i].selected_rect = (left,top ,width, height)
            if width > self.menu_width:
                    self.menu_width = width
            self.menu_height  += height
        x = self.dest_surface.get_rect().centerx - self.menu_width / 2
        y = self.dest_surface.get_rect().centery - self.menu_height / 2
        mx, my = self.drawing_position
        self.drawing_position = (x + mx, y + my) 
