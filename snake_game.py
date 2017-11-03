import pygame
import random
import math

width = 750
height = 600
r = 16
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake_game")
background = (255,255,255)
screen.fill(background)
rect = pygame.Rect(0,0,width, height)
state = True # running state


class snake:
    def __init__(self,x,y,radius,direction,dots, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.direction = direction
        self.dots = dots
        self.locations = [[x,y],[x+2*radius,y],[x+4*radius,y]]
        self.color = color
        r = 0 if color[0]-60 < 0 else color[0]-60 #ternary operator
        g = 0 if color[1]-60 < 0 else color[1]-60
        b = 0 if color[2]-60 < 0 else color[2]-60
        self.head_color = (r,g,b)
        

    def draw(self):
        pygame.draw.circle(screen,self.head_color,self.locations[0],self.radius)
        for i in range(1,self.dots):
            pygame.draw.circle(screen,self.color,self.locations[i],self.radius)
            #pygame.display.flip()
       

    def change_size(self):
        self.dots += 1
        # adds new locations in the self.locations array
        if self.direction=='a':
            self.x = self.x-self.radius*2
            self.locations.insert(0, [self.x, self.y])
        if self.direction=='d':
            self.x = self.x+self.radius*2
            self.locations.insert(0, [self.x,self.y])
        if self.direction=='w':
            self.y = self.y-self.radius*2
            self.locations.insert(0, [self.x,self.y])
        if self.direction=='s':
            self.y = self.y+self.radius*2
            self.locations.insert(0, [self.x, self.y])
            

    def cont_move(self):
        #self.direction = input()
        if self.direction=='a':
            self.x = self.x-self.radius*2
            self.locations.insert(0, [self.x, self.y])
            self.locations.pop()
        if self.direction=='d':
            self.x = self.x+self.radius*2
            self.locations.insert(0, [self.x,self.y])
            self.locations.pop()
        if self.direction=='w':
            self.y = self.y-self.radius*2
            self.locations.insert(0, [self.x,self.y])
            self.locations.pop()
        if self.direction=='s':
            self.y = self.y+self.radius*2
            self.locations.insert(0, [self.x, self.y])
            self.locations.pop()
            

    def change_direction(self, direction):
        #self.direction = input()
        #self.direction = direction
        if self.direction=='a' and direction != 'd':
            self.direction = direction
        elif self.direction == 'd' and direction != 'a':
            self.direction = direction
        elif self.direction == 'w' and direction != 's':
            self.direction = direction
        elif self.direction == 's' and direction != 'w':
            self.direction = direction 


    def collision(self):
        global width, height
        if self.x <= 0 + 25 or self.x >= width - 25 or self.y <= 0 + 25 or self.y >= height - 25:
            return True
    
    def eating(self, food):
        if math.sqrt((food.x-self.x)**2+(food.y-self.y)**2) <= (food.radius+self.radius):
            food.delete()
            self.change_size()
            
    def hit(self):
        dots = self.locations
        for i in range(1,self.dots):
            if math.sqrt((dots[i][0]-self.x)**2+(dots[i][1]-self.y)**2) <= (2*self.radius-15):
                return True
        return False

class food:
    def __init__(self, radius):
        self.x = random.randint(50,600)
        self.y = random.randint(50,500)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen,(200,200,100),[self.x,self.y],self.radius)

    def delete(self):
        self.x = random.randint(50,600)
        self.y = random.randint(50,500)

snake1 = snake(200,200,10,'d',3,(200,100,120))
food1 = food(9)

collide = False
while state:
    events = pygame.event.get() # list of all the events
    for each_event in events:
        if each_event.type == pygame.QUIT:
            state = False
        elif each_event.type == pygame.KEYDOWN:
            if each_event.key == pygame.K_LEFT:
                snake1.change_direction('a')
            if each_event.key == pygame.K_RIGHT:
                snake1.change_direction('d')
            if each_event.key == pygame.K_UP:
                snake1.change_direction('w')
            if each_event.key == pygame.K_DOWN:
                snake1.change_direction('s')
            
    screen.fill(background)
    pygame.draw.rect(screen,(150,75,220),rect,25)
    food1.draw()
    if not collide:
        snake1.cont_move()
    snake1.draw()
    if snake1.collision() or snake1.hit():
        collide = True
    snake1.eating(food1)
    pygame.display.flip()
    pygame.time.delay(150)
    

pygame.quit()


# 1. consumption of food
