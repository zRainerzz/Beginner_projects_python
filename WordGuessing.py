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


    try:
        a=int(input("Choose a number of tries which should be not over 15"))
    except TypeError or a>15:
        a=int(input("type an integer under 15."))




if __name__=="__main__":
    main()