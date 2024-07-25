import random

def main():
    wordslist=["KING","QUEEN","PRINCE","HOME","LIFE","DETERMINATION","SUCESS","PALESTINE","FREE"]
    win=random.choice(wordslist)
    winning_word=""
    #first name && last name.
    try:
        first_name=input("your first name,It would be nice if you introduce yourself. isn't it? ").lower()
        last_name=input("What about your last name?").lower()
    except (first_name not in ["a-z"]) and (last_name not in ["a-z"]):
        first_name=input("you cannot have other than letters in your name dude").lower()
        last_name=input("what? your last name must have no more than letters.").lower()

    #number of guesses.
    try:
        a=int(input("Choose a number of tries which should be not over 15 "))
    except TypeError and a>15:
        a=int(input("type an integer under 15. "))
        
    #making a list of dots
    dots=[]
    for _ in range(len(win)):
        dots.append(".")
    print("So try your typo 1 by1 according to word's lengh ",dots)

    lenght=len(win)
    i=0
    while (i!=a) or (set(winning_word) != set(win)):
        #starting to guess.
        #guesses input type configuration.
        try:
            guess=input("Give your first letter. ").upper()
        except guess not in ["A-Z"] and (len(guess))>1:
            guess=input("type your guess here, 1 letter is a must. ").upper()


            #moving through all letters
        dot=0
        if (guess == win[dot]) and (dot<(len(win))):
            dots[dot]=guess
            print ("you were right about it.", dots)
        else:
            dot +=1
        i+=1
    print(winning_word, "okay")

if __name__=="__main__":
    main()