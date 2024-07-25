import random

def main():
    try:
        name=input("It would be nice if you introduce yourself. isn't it?").lower
    except name not in ["a-z"]:

    result=[]
    converted=[]
    wordslist=["KING","QUEEN","PRINCE","HOME","LIFE","DETERMINATION","SUCESS","PALESTINE","FREE"]
    win=random.choice(wordslist)
    win_result=[]
    
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
        if win==converted:
            print("you won!, congratz.")
            break
    print(result)



def word_contain(win,a,converted):
#test if the guess is in win or not.
    for i in range (len(win)):
        if a==win[i]:
            converted[i]=a
    return converted
    

def list_convert(win):
#make a list of dot according to letters in a word.
    result = []

    for _ in (len(win)):
            result.append(".")
    return result



if __name__=="__main__":
    main()