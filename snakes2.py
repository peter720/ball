#  2D list (matrix)
# 20x20
# ex: 5x5
'''
   0 1 2 3 4
0: # # # # # 
1:
2:
3:
4: # # # # #

'''

'''
grid = []
l = [' ' for i in range(20)] # list comprehension
for i in range(20):
    grid.append(l)
'''
x = 20
grid = [[' ' for i in range(x)] for j in range(x)]
snake_length = 3
snake = [10,10]

def drawSnake(grid):
    for i in range(snake_length):
        grid[snake[0]][snake[1]+i] = "*"
def makeBorder(grid):
    #grid[0][0] = "#"
    #grid[0][1] = "#"
    
    for i in range(x):
        grid[0][i] = "#"
        grid[x-1][i] = "#"
        grid[i][0] = "#"
        grid[i][x-1] = "#"
    
def printGrid(grid):
    for i in range(x):
        # printing a row
        for j in range(x):
            print(grid[i][j], end='')
        print() # print a new line (goes to a new line)

def moveRight(grid):
    global snake
    for i in range(len(snake)):
        grid[snake[1]+1] = '*'
        snake[1] = snake[1]+1
    grid[snake[1]] = ' '
    
def moveLeft(grid):
    for i in range(len(snake)):
        grid[snake[1]-1] = '*'
        snake[1] = snake[1]-1
    grid[snake[1]+2]= ' '
    
def moveUp(grid):
    for i in range(len(snake)):
        grid[snake[0]-1] = '*'
        snake[0] = snake[0]-1
    grid[snake[0]+1] = ' '
   
    
    
def moveDown(grid):
    for i in range(len(snake)):
        grid[snake[0]+1] = '*'
        snake[0] = snake[0]+ 1
    grid[snake[-1]+1] = ' '
    
'''
def func():
    a = 5 # local to the function

# global
func()
a = 6
print(a)
'''   
import random

prey_loc = (random.randint(1, x-1), random.randint(1, x-1))
makeBorder(grid)
drawSnake(grid)

# game loop
while(True):
    
    grid[prey_loc[0]][prey_loc[1]] = '^' 
    printGrid(grid)
    grid[prey_loc[0]][prey_loc[1]] = " "
    
    prey_loc = (random.randint(1, x-1), random.randint(1, x-1))
    p = input()
    if p == 'd':
        moveRight(grid)
    if p == 'a':
        moveLeft(grid)
    if p == 'w':
        moveUp(grid)
    if p == 's':
        moveDown(grid)


'''
|_

[6,4][6,5][6,6]
[6,3][6,4][6,5]

l=[1,2,3,4]
l[0], l[1], l[2]

HW 1: reset snake
HW 2: moveLeft()
HW 3: moveDown(), if possible moveUp()
'''
