import random
import json
import pickle
## function to insert the word in the txt file
def insert():
    while True:
            insertion = input("Enter the word you want to add to the list :")
            if insertion.isdigit() == True:
                print("this is not a word but a number please enter a word with letter")
            else:
                insertion = insertion+"\n"
                if len(insertion)>3:
                    with open('mots.txt', 'a') as file:
                        file.write(insertion)
                        break
                else:
                    print("please enter a word with length >=3 letter")
                

## function who choose a random word of the list
def word_choice():
    with open('mots.txt', 'r') as word:
            tab_words = [i.strip() for i in word]
            return random.choice(tab_words)
            

## function who manage the main task of the game
def game(tryin,word):
    words = ["_" for i in word]
    wrong_letters = []
    while True:
        print("".join(words))
        letter = input("enter a letter : ")
        if tryin == 11:
            print("vous avez perdue")
            break
        else:
            if letter in word:
                for i in range(len(word)):
                    if letter == word[i]:
                        words[i] = letter
            if letter not in word:
                wrong_letters.append(letter)
                print(wrong_letters)
                tryin += 1

            if "".join(words) == word:
                return tryin

## function who add a score to the user
def scoring(tryin, score, name):
        if tryin >= 1 and tryin <=3:
            score +=100
        elif tryin >= 4 and tryin <=6:
            score +=50
        elif tryin >= 7 and tryin <=10:
            score +=25
        else:
            score = 0
            
            
        
        insert_score(name, score)
        return tryin, score
            
# function to insert the score into the json file                    
def insert_score(name, score):
    data = f"{name} : {score} \n"
    with open('scores.txt',"a+") as file:
         file.write(data)
    """
    data = {
                'name' : name,
                'score':score
            }
    array = [{i:data[i]} for i in data]
    json_str = json.dumps(array)

    with open('score.json','a') as file_json:
        json.dump(json_str, file_json)
    """
#function who show the score history   
def read_history():
    with open('scores.txt', 'r') as file:
         data = file.read()
         print(data)
    """
    with open('score.json','r')as file:
        data = json.load(file)
        print(data)
    """

## function who dislplay a message of victory or losing              
def victory_message(trying):
        print(f"you find the word here is your score {trying[1]}")


    


#main function who call the other function
def main():
    essai = 0
    score = 0
    name= input("enter your name : ")
    while True:
        
        print(f"""
              {name} choose between the next choices
              1 : new game
              2 : insert a word in the list
              3 : show score history
              4 : exit the game
              """)
        
        choices = int(input(""))

        if choices == 1:
            
            choix = word_choice()
            gamer =  game(essai,choix)
            scores = scoring(gamer,score, name)
            victory_message(scores)
        elif choices == 2:
            insert()
        elif choices == 3:
            read_history()
        elif choices== 4 :
            break
        

        
main()