import pygame
import os
import sys
from pygame.locals import *
import random

def enter_name(screen,r5, orange, my_Font, letter):
    
    wallpaper = pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))
    pygame.draw.rect(screen, orange, r5, 0)
    hello = "hello, enter your username : "
    font_dis = my_Font.render(hello,1, (255,255,255))
    font_rect = font_dis.get_rect(center=r5.center)
    screen.blit(font_dis, font_rect)
   
    name= ""
    input_active = True
    selected_index = 0 
    pygame.display.update()

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RIGHT:
                    selected_index = (selected_index + 1) % len(letter)
                elif event.key == pygame.K_LEFT:
                    selected_index = (selected_index - 1) % len(letter)
                elif event.key == pygame.K_UP:
                    name += letter[selected_index]
        
        ##blit  screen element
        pygame.draw.rect(screen, orange, r5, 0)
        screen.blit(font_dis,font_rect)

        #display the word enter by the user
        input_text = my_Font.render(name, 1, (255,255,255))
        screen.blit(input_text, (r5.x + 20, r5.y +20))

        for i , char in enumerate(letter):
            if i == selected_index:
                char_surface = my_Font.render(char,1, (135,206,250))
            else:
                char_surface = my_Font.render(char, 1, (255,255,255))
            screen.blit(char_surface,(100 + i * 30, 500))
        pygame.display.update()
        ## lock  screen at 60 fps
        pygame.time.Clock().tick(60)
    



def Main_menu(screen, r1, r2,r3,r4, orange, my_Font):
    ng = "new game"
    insert = "insert a word"
    history = "score history"
    exit = "exit"
    wallpaper = pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))

    pygame.draw.rect(screen, orange, r1,0)
    font_dis = my_Font.render(ng, 1 , (255,255,255))
    font_rect = font_dis.get_rect(center=r1.center)
    screen.blit(font_dis, font_rect)

    pygame.draw.rect(screen, orange, r2,0)
    font_dis2 = my_Font.render(insert, 1 , (255,255,255))
    font_rect2 =font_dis2.get_rect(center=r2.center)
    screen.blit(font_dis2, font_rect2)

    pygame.draw.rect(screen, orange, r3,0)
    font_dis3 = my_Font.render(history, 1 , (255,255,255))
    font_rect3 =  font_dis3.get_rect(center = r3.center)
    screen.blit(font_dis3, font_rect3)

    pygame.draw.rect(screen, orange, r4,0)
    font_dis4 = my_Font.render(exit, 1, (255,255,255))
    font_rect4 = font_dis4.get_rect(center = r4.center)
    screen.blit(font_dis4, font_rect4)

    pygame.display.update()

def New_Game(screen, r, orange, my_font, letter, word):
    words = ["_" for i in word]
    display_underscore= "  ".join(words)
    wrong_letter= []
    select_index = 0
    trying = 0
    wallpaper = pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))

    pygame.draw.rect(screen,orange, r, 0 )
    font_dis = my_font.render("entrez votre mot : ", 1,(255,255,255))
    font_rect = font_dis.get_rect()
    font_rect.midtop = (r.centerx, r.top)
    screen.blit(font_dis, font_rect)

    font_dis =my_font.render(display_underscore, 1, (255,255,255))
    font_rect = font_dis.get_rect(center = r.center)
    screen.blit(font_dis, font_rect)

    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN :
                print("shallow")
            elif event.type == pygame.K_LEFT:
                select_index = (select_index -1) % len(letter) 
            elif event.type == pygame.K_RIGHT:
                select_index = (select_index + 1) % len(letter)
            elif event.type == pygame.K_UP:
                if letter[select_index] in word:
                    for i in range(len(word)):
                        if letter == word[i]:
                            words[i] = letter[select_index]
                        if letter[select_index] not in word:
                            wrong_letter.append(letter[select_index])
                            print(wrong_letter)
                            trying +=1
            
    for i , char in enumerate(letter):
        if i == select_index:
            char_surface = my_font.render(char,1, (135,206,250))
        else:
            char_surface = my_font.render(char, 1, (255,255,255))
            screen.blit(char_surface,(100 + i * 30, 500))
    pygame.display.update()
        ## lock  screen at 60 fps
    pygame.time.Clock().tick(60)

            
                








def insert_words(screen, r, orange, my_font):
    
    wallpaper = pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))

    pygame.draw.rect(screen,orange, r, 0 )
    font_dis = my_font.render("Insert a word", 1,(255,255,255))
    font_rect = font_dis.get_rect(center = r.center)
    screen.blit(font_dis, font_rect)

    
def Show_history(screen,r1, orange, my_Font ):
    
    wallpaper = pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))

def word_choice():
    with open('mots.txt', 'r') as word:
            tab_words = [i.strip() for i in word]
            return random.choice(tab_words)

    
def main():
    Main_Menu =0
    New_game= 1
    Insert_Word = 2
    Show_History = 3
    Exit = 4
    state_game = Main_Menu
    word = word_choice()

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1000,600))
    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    r1 = pygame.Rect(150,100,400,75)
    r2 = pygame.Rect(250,200,400,75)
    r3 = pygame.Rect(350,300,400,75)
    r4 = pygame.Rect(450,400,400,75)
    r5 = pygame.Rect(300, 200,400,200)
    orange = [255,140,0]
    my_Font = pygame.font.SysFont("comicsansms", 32)
    pygame.display.set_caption("hello")
    
    run = True
    Main_menu(screen, r1, r2,r3,r4, orange, my_Font)
    
            
    while run:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run =False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if state_game == Main_Menu and r1.collidepoint(event.pos):
                        state_game = New_game
                    elif state_game == Main_Menu and r2.collidepoint(event.pos):
                        state_game = Insert_Word
                    elif state_game == Main_Menu and r3.collidepoint(event.pos):
                        state_game = Show_History
                    elif state_game == Main_Menu and r4.collidepoint(event.pos):
                        state_game = Exit
                
                        
            if state_game == New_game:
                New_Game(screen, r5, orange, my_Font, letter, word)
            elif state_game == Insert_Word:
                insert_words(screen,r5, orange, my_Font )
            elif state_game == Show_History:
                Show_history(screen,r5, orange, my_Font )
            elif state_game == Exit:
                pygame.quit()
                sys.exit()

                    
            pygame.display.flip()
        
main()
if __name__ == "__main__":
    main()