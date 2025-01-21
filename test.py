with open('test.txt', 'r') as file:
    for mot in file:
        print(mot)


import pygame
from pygame.locals import *


def screen():
    pygame.display.set_caption("hello")
    screen = pygame.display.set_mode((1000,600))

def main():
    pygame.init()
    run = True
    while run:
        screen()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False
        pygame.display.update()

main()
if __name__ == "__main__":
    main()