import random

def main():
    wordslist=["KING","QUEEN","PRINCE","HOME","LIFE","DETERMINATION","SUCESS","PALESTINE","FREE"]
    win=random.choice(wordslist)
    #first name && last name.
    while True:
        first_name = input("Enter your first: ")
        if is_alphabetic(first_name):
            break
        else:
            print("Invalid first name. Please enter only alphabetic characters.")


    while True:
        last_name = input("Enter your last name: ")
        if is_alphabetic(last_name):
            break
        else:
            print("Invalid last name. Please enter only alphabetic characters.")

    #number of guesses.
    try:
        a=int(input("Choose a number of tries which should be not over 15 "))
    except TypeError and a>15:
        a=int(input("your tries count should be an integer under 15. "))
        
    #making a list of dots
    dots=[]
    for _ in range(len(win)):
        dots.append(".")
    print("So try your typo 1 by1 according to word's lengh ",dots)

    lenght=len(win)
    i=0
    while (i!=a):
        #starting to guess.
        #guesses input type configuration.
        guess=input("Give 1 letter. ").upper()
        while not (guess not in "ABCDEFGHIJKLMNEPQRSTUVWXYZ") and ((len(guess))>1):
            guess=input("type your guess here, 1 letter is a must. ").upper()


            #moving through all letters
        dot=0
        for dot in range (len(win)):
            if (guess == win[dot]) and (dot<lenght):
                dots[dot]=guess
                print ("you were right about it.", dots)
        i+=1
        if  (set(dots) == set(win)):
            with open ("WordGuessing_ranking.csv","a") as file:
                file.write(f"{first_name},{last_name},{win} \n")
                print(f"Congratulations {first_name}, You Won.{dots}")
            break

        if (i==a) and not (set(dots) == set(win)):
            print ("Unfortunately,you tried, but failed")
            break




def is_alphabetic(name):
    return name.isalpha()





if __name__=="__main__":
    main()