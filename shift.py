# initialize
snake = [(0,3), (0,4), (0,5), (0,6)]
direction = 'a' # ['a', 'd', 'w', 's']

'''
a - left
d - right
w - up
s - down
'''

def createGrid():
    grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    return grid

def resetGrid():
    return createGrid()

def drawSnake(grid, snake_loc):
    for i in snake_loc:
        y = i[0]
        x = i[1]
        grid[y][x] =  '*'
    print(grid)

def moveDown(snake_loc):
    if direction != 's':
        for i in range(len(snake)):
            snake[1+i][1] = snake[1+i][1] - 1
        snake[0][0] = snake[0][0]+1

grid = createGrid()

drawSnake(grid, snake)

grid = resetGrid()

##snake = [(1,3),(0,3),(0,4),(0,5)]
moveDown(snake)
drawSnake(grid, snake)
    
'''
for x,y in snake:
    print(x)
    print(y)
'''
    
'''
moveDown()
grid = [[' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ']]
'''
'''
for i in snake:
    grid[snake[0][0]] = ' '
    grid[1][3] = '*'
'''
