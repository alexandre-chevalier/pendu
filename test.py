import pygame
import os
import sys
from pygame.locals import *
import random


def Main_menu(screen, wallpaper,orange,  r1, r2, r3, r4, font, white):
    ng = "new game"
    insert = "insert a word"
    history = "score history"
    exit = "exit"
    
    pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))

    pygame.draw.rect(screen,orange, r1)
    #je selectionne le rendu de la font avec le texte a ecrire, l'antialiasing et la couleur
    font_dis = font.render(ng, 1,white)
    #le get_rect me permet de positionner le texte dans le rectangle créer
    font_rect = font_dis.get_rect(center=r1.center)
    #je fais passer le render de la font et le positionnement du texte dans le blit
    screen.blit(font_dis, font_rect)


    pygame.draw.rect(screen, orange, r2)
    font_dis2 = font.render(insert, 1, white)
    font_rect2 = font_dis2.get_rect(center = r2.center)
    screen.blit(font_dis2, font_rect2)

    pygame.draw.rect(screen, orange, r3)
    font_dis3 = font.render(history, 1, white)
    font_rect3 = font_dis3.get_rect(center = r3.center)
    screen.blit(font_dis3, font_rect3)

    pygame.draw.rect(screen, orange, r4)
    font_dis4 = font.render(exit, 1, white)
    font_rect4 = font_dis4.get_rect(center = r4.center)
    screen.blit(font_dis4, font_rect4)

    pygame.display.update()
    
    

def New_Game(screen, wallpaper):
    print("hello")
   


def insert_words(screen,wallpaper, r, orange, my_font):
     print("hello")

    
def Show_history(screen, wallpaper, r, orange, font, white, r2, score):
    main_menu = "main menu"
    
    pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper,(0,0))

    pygame.draw.rect(screen, orange, r)
    font_dis = font.render(main_menu, 1, white)
    font_rect = font_dis.get_rect(center= r.center)
    screen.blit(font_dis,font_rect)

    pygame.draw.rect(screen,orange, r2 )
    for index, i in enumerate(score):
        verical_pos =r2.top + 20 + index * 30

        font_score = font.render(i, 1, white)
        font_rect2 = font_score.get_rect(midtop=(r2.centerx, verical_pos))
        screen.blit(font_score, font_rect2)

    pygame.display.update()

def word_choice():
    with open('mots.txt', 'r') as word:
            tab_words = [i.strip() for i in word]
            return random.choice(tab_words)

def read_history():
    with open('scores.txt', 'r') as file:
         data = file.readlines()
         return data
    
def main():
    Main_Menu =0
    New_game= 1
    Insert_Word = 2
    Show_History = 3
    Exit = 4
    state_game = Main_Menu
    word = word_choice()
    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1000,600))
    wallpaper = pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    
    r1 = pygame.Rect(150,100,400,75)
    r2 = pygame.Rect(250,200,400,75)
    r3 = pygame.Rect(350,300,400,75)
    r4 = pygame.Rect(450,400,400,75)
    r5 = pygame.Rect(75, 100,850,350)
    r6 = pygame.Rect(375,0,250, 75)
    orange = [255,140,0]
    white = [255,255,255]
    my_Font = pygame.font.SysFont("comicsansms", 32)
    pygame.display.set_caption("hello")
    score = read_history()
    print(score)
    run = True
    Main_menu(screen, wallpaper, orange, r1, r2, r3, r4, my_Font, white)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
            ## event de type clic de souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                ##condition qui permer de voir que l'on clique bien sur le rectangle
                if state_game == Main_Menu and r1.collidepoint(event.pos):
                    #on affecte une nouvelle valeur a state_game
                    state_game =  New_game
                elif state_game == Main_Menu and r2.collidepoint(event.pos):
                    state_game = Insert_Word
                elif state_game == Main_Menu and r3.collidepoint(event.pos):
                    state_game = Show_History
                elif state_game == Main_Menu and r4.collidepoint(event.pos):
                    state_game = Exit

        ## condition qui verifie la valeur de state_game et
        ## appelle la fonction correspondante
        if state_game == New_game:
            New_Game(screen, wallpaper)
        elif state_game == Insert_Word:
            insert_words(screen, wallpaper)
        elif state_game == Show_History:
            Show_history(screen, wallpaper, r6, orange, my_Font, white, r5, score)
        elif state_game == Exit:
            pygame.quit()
            sys.exit()


        
        
    pygame.display.flip()
        

    


main()

if __name__ == "__main__":
    main()