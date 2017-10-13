# 12343428798436578647863
# 7


import random

def compare_numbers(number, user_guess):
    cowbull = [0,0] 
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[0]+=1 # cows (index 0)

        else:
            for e in range(len(number)):
                if number[e] == user_guess[i]:
                    cowbull[1] += 1
                    break
        
    return cowbull

if __name__=="__main__":
    playing = True 
    number = str(random.randint(1000,9999)) # 34 0 789
    print(number)
    guesses = 0
    while playing:
        user_guess = input("Give a guess")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[0]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break 
        else:
            print("Your guess isn't quite right. Try again.")
