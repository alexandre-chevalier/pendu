import random



## fonction pour inserer un mot dans le fichier texte
def insert():
    insertion = input("veuillez entrez le mot que vous voulez ajoutez a la liste :")+'\n'
    with open('mots.txt', 'a') as fichier:
        fichier.write(insertion)

## fonction pour choisir un mot aleatoire dans le fichier texte et qui retourne le mot
def word_choice():
    with open('mots.txt', 'r') as word:
        read = word.read().strip("\n")
        print(read)
        word = read[random.randint(0, len(read)-1)]
        print(word)
        return word

def lose():
    print(f"vous avez perdu")


## fonction qui gere le jeu
def game(scoring,essai,word):
    mot = []
    wrong_letters = []

    print(word)
    for i in range(len(word)):
            mot.append("-")
    while True:

        if " ".join(mot) == word:
            print("vtc")
            return score(essai, scoring)
        if essai == 11:
            lose()
            break
        print(mot)
        lettre = input("veuillez entrez une lettre : ")
        
        print(f"vous avez {essai} erreur")
            
        if lettre in word:   
            for i in range(len(word)):
                if lettre == word[i]:
                    mot[i] = lettre
                    print(mot)
        if lettre not in word:
            essai += 1
            wrong_letters.append(lettre)
            print(wrong_letters)



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
        scoring +=0

    return message_victoire(essai, scoring)
        


                    
                    
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