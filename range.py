# 0 -> 5 -> 10 -> 15 -> 20 -> 25 ....
# 2 -> 7 -> 12 -> 17 -> 22 -> 27 -> ...
# 0,0 -> 0,5 -> 0,10, 0,15

(x,y) = (0,0)

def move():
    global x, y
    y = y+5
    print(str(x) + " " + str(y))


for i in range(10):
    move()

