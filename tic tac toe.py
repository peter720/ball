'''

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

player 1 -> X,
player 2 -> O

'''
'''
123
456
789
grid[row][col]
grid[0][0] grid[0][1] grid[0][2]
grid[1][0] grid[1][1] grid[1][2]
grid[2][0] grid[2][1] grid[2][2]

row = 0, col = 0, 1, 2
row = 1, col = 0, 1, 2
row = 2, col = 0, 1, 2

'''
def printGrid(grid):
    print('\n --- --- ---')
    for row in range(3):
        for col in range(3):
            print("| "+grid[row][col]+" ", end = "")
        print('|')
        print(' --- --- ---')
    
    
grid = [['1','2','3'],
        ['4','5','6'],
        ['7','8','9']] # 2d list

printGrid(grid)
print("Player 1 is X and player 2 is O")

'''
player 1: 5

1 | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9

player 2: 3

X | X | O
---------
X | 5 | O
---------
7 | 8 | O


'''

def checkHorizontal(grid):
    
    if grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2]:
        return True
    if grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2]:
        return True
    if grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2]:
        return True
    return False

def checkVertical(grid):
    if grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0]:
        return True
    if grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1]:
        return True
    if grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2]:
        return True
    return False

def checkDiagonal(grid):
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
        return True
    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
        return True
    return False

player = 0

ch = ''
for round1 in range(1,10):
    if round1 % 2 == 0 :
        player = 2
        ch = 'O'
    else:
        player = 1
        ch = 'X'
    location = input('Player ' + str(player) + ': ') # '11'

    found = False
    for row in range(3):
        if location in grid[row]:
            found = True
            col = grid[row].index(location)
            grid[row][col] = ch # if player 1 ch is X, otherwise O
            printGrid(grid)
            break

    #******
    o = 'Player ' + str(player) + ' has won the game.'
    if(checkHorizontal(grid) == True):
        print(o)
        break
    elif (checkVertical(grid) ==True):
        print(o)
        break
    elif(checkDiagonal(grid)== True):
        print(o)
        break
    if round1 == 9:
        print("This game is a draw")
    
    #******

    if not found:
        print('invalid location')



'''
rounds -> 1 2 3 4 5 6 7 8 9 
player -> 1 2 1 2 1 2 1 2 1 <-end

'''

# hw1: check if its a tie
# hw2: reduce that code inside the marked (******) lines  to 1 or 2 lines
