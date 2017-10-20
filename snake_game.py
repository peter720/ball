import pygame
width = 750
height = 600
r = 16
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake_game")
background = (255,255,255)
screen.fill(background)
rect = pygame.Rect(0,0,width, height)



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
        

    def change_size(self, num):
        self.dots = self.dots + num
        # adds new locations in the self.locations array

    def cont_move(self):
        #self.direction = input()
        if self.direction=='a':
           for loc in self.locations:
               loc[0] = loc[0]-2*self.radius
        if self.direction=='d':
            for loc in self.locations:
               loc[0] = loc[0]+2*self.radius
        if self.direction=='w':
            
        if self.direction=='s':
        
            

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


    
            
snake1 = snake(200,200,10,'d',3,(200,100,120))
state = True # running state
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
    snake1.cont_move()
    snake1.draw()
    pygame.display.flip()
    pygame.time.delay(200)

pygame.quit()

# 1. finish the draw method
# 2. finish the change_size method
# 3. create the snake object
# 4. show it on the sceen
