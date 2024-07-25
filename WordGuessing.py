import random

def main():
    name=input("It would be nice if you introduce yourself. isn't it?")
    result=[]
    converted=[]
    wordslist=["KING","QUEEN","PRINCE","HOME","LIFE","DETERMINATION","SUCESS","PALESTINE","FREE"]
    win=random.choice(wordslist)
    converted=list_convert(win)
    result=word_contain(converted)
    try:
        a=int(input("Choose a number of tries which should be not over 15"))
    except TypeError or a>15:
        a=int(input("type an integer under 15."))


    for _ in range(a):
        guess=input("What's your first letter to start with?").upper()
        if len(guess)!=1 or (guess not in ["A-Z","a-z"]):
            guess=input("1 letter is a must.")
    wordslist=["KING","QUEEN","PRINCE","HOME","LIFE","DETERMINATION","SUCESS","PALESTINE","FREE"]
    win=random.choice(wordslist)
    converted=list_convert(win)
    result=word_contain(converted)
    print(result)



def word_contain(win,guess,converted):
#test if the guess is in win or not.
    for i in range (len(win)):
        if guess==win[i]:
            converted[i]=guess
    return converted
    

def list_convert(win):
#make a list of dot according to letters in a word.
    result = []

    for _ in (len(win)):
            result.append(".")
    return result



if __name__=="__main__":
    main()