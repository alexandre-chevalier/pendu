import pygame
import os
from pygame.locals import *


def screen1():

    orange = [255,140,0]
    r = Rect(300,400,400,75)
    my_Font = pygame.font.SysFont("comicsansms", 16)
    ng = "new game"

    pygame.display.set_caption("hello")
    screen = pygame.display.set_mode((1000,600))
    wallpaper = pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))
    menu = pygame.draw.rect(screen, orange, r,0)
    ng_display = my_Font.render(ng, 1 , (255,255,255))
    screen.blit(ng_display, (100,100))


def screen2():
    screen = pygame.display.set_mode((1000,600))
    wallpaper = pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))
    

    
def main():
    pygame.init()
    pygame.font.init()
    run = True
    screen1()
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False
        pygame.display.update()

main()
if __name__ == "__main__":
    main()