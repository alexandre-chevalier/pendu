import random

## fonction pour inserer un mot dans le fichier texte
def insert():
    insertion = input("veuillez entrez le mot que vous voulez ajoutez a la liste :")+'\n'
    with open('mots.txt', 'a') as fichier:
        fichier.write(insertion)

## fonction pour choisir un mot aleatoire dans le fichier texte et qui retourne le mot
def word_choice():
    with open('mots.txt', 'r') as word:
        read = word.readlines()
        word = read[random.randint(0, len(read)-1)]
        return word
          
## fonction qui gere le jeu
def game(essai,word):
    mot = []
    for i in range(len(word)-1):
            mot.append("-")

    while True:
        lettre = input("veuillez entrez une lettre : ")
        if lettre in word:
            for i in range(len(word)-1):
                if lettre == word[i]:
                    mot[i] = word[i]
                    print("".join(mot))
                    print(str(mot))
                    print(word)
                if str(mot) == word:
                    break 
                    
                    
                    
                

                

    
def victoire(essai, scoring):
    print(f"vous avez trouver le mot en {essai} ce qui vous fait un score de {scoring}")

def main():
    while True:
        print("""
              1 : demarrer une nouvelle partie
              2 : inserer un mot dans la liste
              """)
        
        choices = int(input(""))

        if choices == 1:
            essai = 0
            score = 0
            choix = word_choice()
            print('hello' , choix)
            game(essai,choix)
        elif choices == 2:
            insert()
        

        
main()