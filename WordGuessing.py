import random

def main():
    wordslist=["KING","QUEEN","PRINCE","HOME","LIFE","DETERMINATION","SUCESS","PALESTINE","FREE"]
    win=random.choice(wordslist)

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

    #guesses input type configuration.
    try:
        tries=input("type your guess here. ").upper()
    except tries not in ["A-Z"] and (len(tries))>1:
        tries=input("type your guess here, 1 letter is a must. ").upper()

    while not a and (tries not in win):





if __name__=="__main__":
    main()