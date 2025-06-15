import pygame as pg
from const import *
from bird import Bird
from pipe import Pipe
#game obj
bird = Bird()
pipes = [Pipe()]

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pg.time.Clock()
def main():
    score = 0
    while True:
        #control
        for event in pg.event.get():
            if event.type ==  pg.QUIT:
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    bird.jump()
        #OBJ update
        bird.move()
        for pipe in pipes:
            pipe.move(score)
            if score % 5 == 0:
                if pipe.gap > 100:
                    pipe.gap -=40



            if pipe.collide(bird):
                print("GAME OVER")
                print(f"your score:  {score}")
                pg.quit()


            if not pipe.passed and pipe.x < bird.x:
                pipes.append(Pipe())
                pipe.passed = True
                score += 1


                 
        #frames
        screen.blit(BG_IMG, (0,0))
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)


        pg.display.update()
        clock.tick(FPS)
main()
