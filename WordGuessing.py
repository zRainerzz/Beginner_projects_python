import random
name=input("It would be nice if you introduce yourself. isn't it?")
def main():
    guess="a"
    wordslist=["KING","QUEEN","PRINCE","HOME","LIFE","DETERMINATION","Success","PALESTINE","FREE"]
    win=random.shuffle(wordslist)
    for i in range (len(win)):
        input_1_letter(guess)
        if guess




def input_1_letter(guess):
#condition to put 1 letter only and being an alphabet is a must.
    guess=input("What's your first letter to start with?")
    if len(guess):
        guess=input("1 letter is a must")
    elif (guess not in ["A-Z","a-z"]):
        guess=input("Alphabets are a must.")
    else:
        return guess
    

def word_contain():
    ...
if __name__=="main":
    main()