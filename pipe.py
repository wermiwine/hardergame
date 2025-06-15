import pygame.mask

from const import *
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
import random


class Pipe:
     def __init__(self):
         self.y_top = 0
         self.y_bottom = 0
         self.gap = 200
         self.x = SCREEN_WIDTH + 30
         self.heights = 0
         self.passed = False
         self.pipetop = pg.transform.flip(PIPE_IMG, False, True)
         self.pipebottom = PIPE_IMG
         self.set_height()
     def set_height(self):
         height = random.randrange(50,SCREEN_HEIGHT//3)
         self.y_bottom = height + PIPE_GAP
         self.y_top = height - self.pipetop.get_height()



     def draw(self,screen):
         screen.blit(self.pipebottom, (self.x, self.y_bottom))
         screen.blit(self.pipetop, (self.x, self.y_top))
     def move(self,score):
         self.x -=PIPE_VEL + (score // 2)
     def collide(self, game_obj):
         pipe_top_mask = pg.mask.from_surface(self.pipetop)
         pipe_bottom_mask = pg.mask.from_surface(self.pipebottom)
         object_mask = game_obj.get_mask()

         top_offset = (self.x - game_obj.x, self.y_top - round(game_obj.y))
         bottom_offset = (self.x - game_obj.x, self.y_bottom - round(game_obj.y))

         top_point = object_mask.overlap(pipe_top_mask, top_offset)
         bottom_point = object_mask.overlap(pipe_bottom_mask, bottom_offset)
         if top_point or bottom_point:
             return True
         return False
