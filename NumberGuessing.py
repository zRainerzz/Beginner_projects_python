import math
import sys
import random
import csv
informations=[]
def main():
    method=input("type p to play or type c to check the winners list. ").upper()
    if method=="P":
        guesses=0
        #number of done guesses
        first, second=inpu_t()
        max_guesses=calculate_max_guesses(first, second)
        print(f"you have {max_guesses} chances.")
        interval=random_range(first,second)
        print(interval)
        #the output to the user of what is the range exp: [15;70]
        starting_point=inferior_func(first,second)
        #the lower number where to start the randint machine
        print(f"this is it ")
        for i in range (max_guesses):
            guess=int(input("*What is your guess?* "))
            the_jackpot=random.randint(starting_point, randomly(first,second))
            if guess==the_jackpot:
                print (f"👑you won! {interval} and you just typed {guess}👑")
                prename=input("given name of the new person is:  ").title()
                name=input(f"{prename}'s last name is: ").title()
                town=input(f"{prename} {name} is from: ")
                city=input(f"{name} {prename} is from {town} and the city's name is: ").title()
                hood=input(f"{name} {prename} lives in {city}, and the hood is: ").title()
                with open ("winners.csv", "a") as file:
                    file.write(f"{name},{prename},{town},{city},{hood} \n")
                break  
            else:
                print(f"--unfortunately! the winner number is {the_jackpot} and you just typed {guess}!")
                guesses=1
                print(f"{guesses} done, you still {max_guesses -1} left.")
    elif method=="C":
        print("Access denied, you need to re-try as a root or open the file manually(it will be locally created automatically).")
        print("Remember, it's a local ranking.")
    else:
        print("invalid input, you should type input to add or print to show.")
        sys.exit()


def inferior_func(x,y):
    if x>y:
        return y
    else:
        return x

def random_range(x,y):
    #the output to the user of what is the range exp [15;70]
    if x>y :
        return f'the game interval is: [{x} ; {y}]'
    else:
        return f'the game interval is: [{y} ; {y}]'
    

def randomly(x, y):
    #the argument needed for random range.
    bot=abs(x-y)
    return bot


def inpu_t():
    #the input interval of the user and its type.
    try:
        first_number=int(input("give me the first integer. "))
        second_number=int(input("give me the second integer. "))
    except ValueError:    
        print("you should type 2 integers ")
        sys.exit()
    else:
        return first_number, second_number
    

def calculate_max_guesses(x, y):
    #calculation of the guesses he can use
    range_size=abs(x - y + 1)
    try:
        s=math.log2(range_size)
    except:
        print("range too small, try again!")

        ValueError
        sys.exit()
    else: 
        return math.ceil(s)
    

informations = "global data"

def my_function():
  global informations
  informations = "modified data"
  print(informations)


if __name__=="__main__":
    main()