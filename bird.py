from const import *

class Bird:
    def __init__(self):
        self.img_count = 0
        self.img = BIRD_IMGS[self.img_count]
        self.x = 220
        self.y = 300
        self.vel = 1
    def move(self):
        self.vel -= 1
        self.y -= self.vel
    def draw(self,screen):
        self.img_count += 1

        if self.img_count < ANIM_TIME:
            self.img = BIRD_IMGS[0]
        elif self.img_count < ANIM_TIME*2:
            self.img = BIRD_IMGS[1]
        elif self.img_count < ANIM_TIME*3:
            self.img = BIRD_IMGS[2]
            self.img_count = 0
        if self.vel < 0:
            self.img = pg.transform.rotate(self.img,-25)

        screen.blit(self.img, (self.x, self.y))
    def jump(self):
        self.vel = 10
    def get_mask(self):
        return pg.mask.from_surface(self.img)
