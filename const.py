import random
import pygame as pg

# Window settings
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
FPS = 30
#Assets
BG_IMG = pg.transform.scale(pg.image.load("img/day.png"),(SCREEN_HEIGHT,SCREEN_HEIGHT))
BIRD_IMGS = [pg.transform.scale(pg.image.load("img/bird 1.png"),(50,40)),
             pg.transform.scale(pg.image.load("img/bird 2.png"),(50,40)),
             pg.transform.scale(pg.image.load("img/bird 3.png"),(50,40))]
ANIM_TIME = 7
PIPE_IMG = pg.transform.scale(pg.image.load("img/Pipe.png"),(104,358))
PIPE_VEL = 5
PIPE_GAP = 200