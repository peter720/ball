print("Welcome to hangman")
word = "ABELOE" 
q = 0

line = ['_' for i in range(len(word))]

def printLine(line):
    for i in range(len(line)):
        print(line[i]+' ', end='')
    print()

printLine(line)

while(True):
    guess = input("Guess your letter: ").upper() # it converts the char to upper
    temp = str(word)
    if guess in word:
        i = temp.find(guess)
        prev_i = 0
        while(i != -1):
            line[i+prev_i] = guess
            prev_i = i+1
            temp = temp[i+1:]
            i = temp.find(guess)
        printLine(line)
           
    else:
        print("Incorrect")
        q = q + 1
    if q == 6:
        print("You lose")
        break
    if '_' not in line:
        print("You win")
        break
    

# see if you can use some other logic
# problem 32
