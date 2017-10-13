import random

y = ["rock", "paper", "scissors"] #0-2


while(True):
    player = input("Type rock, paper, or scissors: ").strip()
    
    if player != "rock" and player != "scissors" and player != "paper":
        print("type again correctly")
        continue

    z = random.randint(0,2) # 0-2
    comp = y[z]
    if player == comp:
        print("Tie")
    else:
        if player == "rock":
            if comp == "scissors":
                print("You Win")
            else:
                print("paper")
                print("You Lose")
            
        elif player == "scissors":
            if comp == "paper":
                print("You Win")
                
            else:
                print("Rock")
                print("You Lose")
        elif player == "paper":
            if comp == "rock":
                print("You Win")
            else:
                print("scissors")
                print("You Lose")
    
        break

    
    
