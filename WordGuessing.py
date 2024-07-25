import random

def main():
    name=input("It would be nice if you introduce yourself. isn't it?")
    result=[]
    converted=[]
    guess="a"
    wordslist=["KING","QUEEN","PRINCE","HOME","LIFE","DETERMINATION","Success","PALESTINE","FREE"]
    win=random.shuffle(wordslist)
    converted=list_convert(win)
    result=word_contain(converted)



def word_contain(win,guess,converted):
#test if the guess is in win or not.
    for i in range (len(win)):
        if guess==win[i]:
            converted[i]=guess
    return converted

        



def input_1_letter(guess):
#condition to put 1 letter only and being an alphabet is a must.
    guess=input("What's your first letter to start with?")
    if len(guess):
        guess=input("1 letter is a must")
    elif (guess not in ["A-Z","a-z"]):
        guess=input("Alphabets are a must.")
    else:
        return guess
    

def list_convert(win):
#make a list of dot according to letters in a word.
    result = []

    for _ in (len(win)):
            result.append(".")
    return result



if __name__=="main":
    main()