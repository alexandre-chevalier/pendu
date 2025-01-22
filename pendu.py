import random

## fonction pour inserer un mot dans le fichier texte
def insert():
    insertion = input("veuillez entrez le mot que vous voulez ajoutez a la liste :")+"\n"
    with open('mots.txt', 'a') as fichier:
        fichier.write(insertion)

## fonction pour choisir un mot aleatoire dans le fichier texte et qui retourne le mot
def word_choice():
    with open('mots.txt', 'r') as word:
            tab_words = [i.strip() for i in word]
            return random.choice(tab_words)
            

def lose():
    print(f"vous avez perdu")

## fonction qui gere le jeu
def game(scoring,essai,word):
    words = ["_" for i in word]
    wrong_letters = []
    while True:
        print("".join(words))
        letter = input("veuillez entrez une lettre : ")
        if essai == 11: 
            lose()
            break
        else:
            if letter in word:
                for i in range(len(word)):
                    if letter == word[i]:
                        words[i] = letter
            if letter not in word:
                wrong_letters.append(letter)
                print(wrong_letters)
                essai+=1

            if "".join(words) == word:
                print("vtc")
                score(essai, scoring)




def score(essai, scoring):
    if essai >= 0 and essai <=2:
        scoring +=100  
    elif essai >= 3 and essai <=6:
        scoring +=75   
    elif essai >= 7 and essai <=8:
        scoring +=50
    elif essai >= 9 and essai <=10:
        scoring +=25    
    elif essai == 11:
        scoring =0
    message_victoire(essai, scoring)         
                    
def message_victoire(essai, scoring):
    print(f"vous avez trouver le mot mais vous avez fait {essai} erreurs,  ce qui vous fait un score de {scoring}")

def main():
    essai = 0
    score = 0
    while True:
        print("""
              1 : demarrer une nouvelle partie
              2 : inserer un mot dans la liste
              """)
        
        choices = int(input(""))

        if choices == 1:
            
            choix = word_choice()
            game(score,essai,choix)
        elif choices == 2:
            insert()
        

        
main()