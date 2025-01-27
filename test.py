import pygame
import os
import sys
from pygame.locals import *
import random

##function who display the main menu
def Main_menu(screen, wallpaper,orange,  r1, r2, r3, r4, font, white):
    ng = "new game"
    insert = "insert a word"
    history = "score history"
    exit = "exit"
    
    pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))

    pygame.draw.rect(screen,orange, r1)
        #i select the render of the font
    font_dis = font.render(ng, 1,white)
        #get_rect can be use to center an element on the rect, in this case the text
    font_rect = font_dis.get_rect(center=r1.center)
        # i blit the screen
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

###function new game who manage the core gameplay of the game

def New_Game(screen,wallpaper, r2, orange, font, white, r,r3, letter, word, r9, name):
    text = "please enter a letter"
    lose= "you lose, click to go to the main menu"
    scores = 0
    select_index= 0
    words = ["_" for i in word]
    
    print(words)
    wrong_letter = []
    run = True
    print(name)
    pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0)) 

    while run:
        ##code who manage the letter choice
        input_text = font.render(name, 1, (255,255,255))
        screen.blit(input_text, (r.x + 20, r.y +20))
        for i , char in enumerate(letter):
            if i == select_index:
                char_surface = font.render(char,1, (135,206,250))
            else:
                char_surface = font.render(char, 1, (255,255,255))
            screen.blit(char_surface,(100 + i * 30, 500))

        pygame.draw.rect(screen, orange, r2)
        font_dis = font.render(text,1, white)
        font_rect = font_dis.get_rect(center = r2.center)
        screen.blit(font_dis, font_rect)

        word_fin= " ".join(words)
        pygame.draw.rect(screen, orange, r)
        font_dis3 = font.render(word_fin,1, white)
        font_rect3 = font_dis3.get_rect(center= r.center)
        screen.blit(font_dis3, font_rect3)   
        
        if len(wrong_letter) >= 12:
            pygame.draw.rect(screen, orange, r9, border_radius=10)
            font_dis4 = font.render(lose, 1, white)
            font_rect4 = font_dis4.get_rect(center=r9.center)
            screen.blit(font_dis4, font_rect4)
        ## condition who manage the victory of the user
        elif "".join(words) == word:
            score = scoring(scores, len(wrong_letter))
           
            screen.fill(orange)
            win=f"{name} you win with {len(wrong_letter)}try, your score is {score}"

            pygame.draw.rect(screen, orange, r9, border_radius=10)
            font_dis4 = font.render(win, 1, white)
            font_rect4 = font_dis4.get_rect(center=r9.center)
            screen.blit(font_dis4, font_rect4)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    insert_score(name, score)
                    return  0
                    
        else:
            ## loop who manage the keyboard input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        select_index = (select_index + 1) % len(letter)
                    elif event.key == pygame.K_LEFT:
                        select_index = (select_index - 1) % len(letter)
                    elif event.key == pygame.K_UP:
                        if letter[select_index] in word:
                            for i,char in enumerate(word):
                                if char == letter[select_index]:
                                    words[i] = char
                                    
                        if letter[select_index] not in word:
                                wrong_letter.append(letter[select_index])
                                pen = pendu(wrong_letter)
                                image = pygame.transform.scale(pen, (r3.width, r3.height))
                                screen.blit(image,r3.topleft )
                                
        pygame.display.update()
        
        pygame.time.Clock().tick(60)
    
## function who load the picture dynamicaly
def pendu(wrong):
        w=min(len(wrong), 12)
        pendus = pygame.image.load(os.path.join('image', f'pendu{w}.jpg'))
        return pendus
        

## function who add a score to the user
def scoring(score, tryin):        
    
        if tryin >=0 and tryin <=3:
            score +=100
        elif tryin >= 4 and tryin <=6:
            score +=50
        elif tryin >= 7 and tryin <=10:
            score +=25
        else:
            score = 0 
        return score
            
# function to insert the score into the txt file                    
def insert_score(name, score):
    data = f"{name} : {score} \n"
    with open('scores.txt',"a+") as file:
        file.write(data)        

## this function insert the word the user enter
def insert_words(screen,wallpaper, r2, orange, font, white, r, letter):
    main_menu = "main menu"
    text = "please enter a word"
    select_index= 0
    name =""
    run = True
    
    pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))

    pygame.draw.rect(screen, orange, r2)
    font_dis = font.render(main_menu,1, white)
    font_rect = font_dis.get_rect(center = r2.center)
    screen.blit(font_dis, font_rect)

    pygame.draw.rect(screen, orange, r)
    font_dis2 =font.render(text, 1, white)
    font_rect2= font_dis2.get_rect(midtop = r.midtop)
    screen.blit(font_dis2, font_rect2)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    insert(name)
                    return 0
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RIGHT:
                    select_index = (select_index + 1) % len(letter)
                elif event.key == pygame.K_LEFT:
                    select_index = (select_index - 1) % len(letter)
                elif event.key == pygame.K_UP:
                    name += letter[select_index]
    
        pygame.draw.rect(screen, orange, r, 0)
        screen.blit(font_dis,font_rect)
        

        input_text = font.render(name, 1, (255,255,255))
        screen.blit(input_text, (r.x + 20, r.y +20))
        for i , char in enumerate(letter):
            if i == select_index:
                char_surface = font.render(char,1, (135,206,250))
            else:
                char_surface = font.render(char, 1, (255,255,255))
            screen.blit(char_surface,(100 + i * 30, 500))

        pygame.display.update()
        
        pygame.time.Clock().tick(60)

## function where the user can enter his name
def name(screen,wallpaper, r2, orange, font, white, r, letter):
    text = "please enter a name"
    select_index= 0
    name =""
    run = True
    
    pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    pygame.Surface.blit(screen, wallpaper, (0,0))

    pygame.draw.rect(screen, orange, r)
    font_dis2 =font.render(text, 1, white)
    font_rect2= font_dis2.get_rect(midtop = r.midtop)
    screen.blit(font_dis2, font_rect2)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name
                    
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RIGHT:
                    select_index = (select_index + 1) % len(letter)
                elif event.key == pygame.K_LEFT:
                    select_index = (select_index - 1) % len(letter)
                elif event.key == pygame.K_UP:
                    name += letter[select_index]
                    

        input_text = font.render(name, 1, (255,255,255))
        screen.blit(input_text, (r.x + 20, r.y +20))
        for i , char in enumerate(letter):
            if i == select_index:
                char_surface = font.render(char,1, (135,206,250))
            else:
                char_surface = font.render(char, 1, (255,255,255))
            screen.blit(char_surface,(100 + i * 30, 500))

        pygame.display.update()
        
        pygame.time.Clock().tick(60)

## function who insert the word in the txt file
def insert(name):
    while True:
            if name.isdigit() == True:
                print("this is not a word but a number please enter a word with letter")
            else:
                name = name+"\n"
                if len(name)>3:
                    with open('mots.txt', 'a') as file:
                        file.write(name)
                        break
                else:
                    print("please enter a word with length >=3 letter")


## function who show the score history  on screen
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
    

## main who manage the variable of the game who serve as parameter for the function
## and manage the screen transition with a variable state_game and condition
def main():
    Main_Menu = 0
    New_game= 1
    Insert_Word = 2
    Show_History = 3
    Exit = 4
    enter_name = 5
    state_game = enter_name
       
    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    pygame.init()
    pygame.font.init()
    
    pygame.mixer.init()
    pygame.mixer.music.load("balatro.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    screen = pygame.display.set_mode((1000,600))
    wallpaper = pygame.image.load(os.path.join('image\cyberpunk.jpg')).convert()
    
    r1 = pygame.Rect(150,100,400,75)
    r2 = pygame.Rect(250,200,400,75)
    r3 = pygame.Rect(350,300,400,75)
    r4 = pygame.Rect(450,400,400,75)
    r5 = pygame.Rect(75, 100,850,350)
    r6 = pygame.Rect(375,0,250, 75)
    r7 = pygame.Rect(75,100,387 ,380)
    r8 = pygame.Rect(537,100,387 ,380)
    r9 = pygame.Rect(0,0,1000 ,600)
    orange = [255,140,0]
    white = [255,255,255]
    my_Font = pygame.font.SysFont("comicsansms", 32)
   
    pygame.display.set_caption("hello")
    score = read_history()
    print(score)
    run = True
    ent_name = name(screen,wallpaper, r2, orange, my_Font, white, r1, letter)
    
    
    while run:
        word = word_choice()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state_game = Main_Menu

            ##condition with event click on the rect
            #we change the valuer of state_game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state_game == Main_Menu and r1.collidepoint(event.pos): 
                    print(ent_name)  
                    state_game =  New_game
                elif state_game == Main_Menu and r2.collidepoint(event.pos):
                    print(state_game)
                    state_game = Insert_Word
                elif state_game == Main_Menu and r3.collidepoint(event.pos):
                    print(state_game)
                    state_game = Show_History
                elif state_game == Main_Menu and r4.collidepoint(event.pos):
                    print(state_game)
                    state_game = Exit
                
                if state_game == Insert_Word and r6.collidepoint(event.pos):
                    ret = insert_words(screen, wallpaper, r6, orange, my_Font,white, r5, letter)
                    state_game = ret
                
                if state_game == Show_History and r6.collidepoint(event.pos):
                    print(state_game)
                    state_game = Main_Menu

                if state_game == New_game and r9.collidepoint(event.pos):
                    ret = New_Game(screen, wallpaper, r6, orange, my_Font,white, r7,r8, letter, word, r9, ent_name)
                    state_game =  ret
                


        ## condition qui verifie la valeur de state_game et
        ## appelle la fonction correspondante
        if state_game == New_game:
            New_Game(screen, wallpaper, r6, orange, my_Font,white, r7,r8, letter, word, r9, ent_name)
        elif state_game == Insert_Word:
            insert_words(screen, wallpaper, r6, orange, my_Font,white, r5, letter)
        elif state_game == Show_History:
            Show_history(screen, wallpaper, r6, orange, my_Font, white, r5, score)
        elif state_game == Main_Menu:
             Main_menu(screen, wallpaper, orange, r1, r2, r3, r4, my_Font, white)            
        elif state_game == Exit:
            pygame.quit()
            sys.exit()
  
        
    pygame.display.flip()

main()

if __name__ == "__main__":
    main()