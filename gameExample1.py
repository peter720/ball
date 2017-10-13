import pygame

#--- main components ---#
# ball object, -> 5 ball objects
# movement (ball objects)
# screen

width = 640
height = 480
a = 40
a = a + (+5)
a = a + (-5)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Ball Game Example")
# rgb -> red, green, blue
# red (0-255)
# 0 -> off, 255-> red
# 0,0,0 -> black
# 255,255,255 -> white
# 0,0,255 -> blue
# 130, 255, 0

# 638+4 

background = (255,255,255)
screen.fill(background)
pygame.display.flip() # frame 1
class ball:

    def __init__(self,x ,y ,speed ,direction ,radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.radius = radius
    
    def move(self):
        screen.fill(background)
        pygame.draw.circle(screen,(255,85,7),(self.x,self.y), self.radius, 1) #
        self.x = self.x + (self.speed*self.direction)
        pygame.display.flip()

    def bounce(self):
        if self.x >= 640 - self.radius or self.x <= 0 + self.radius or self.y >= 480 - self.radius or self.y <= 0 + self.radius:
            self.direction = self.direction *(-1)
    
# game loop
ball_1 = ball(300,300,4,1,30)
ball_2 = ball(100,360,8,1,10)


state = True # running state
while state:
    events = pygame.event.get() # list of all the events
    for each_event in events:
        if each_event.type == pygame.QUIT:
            state = False
    pygame.time.delay(10)
    ball_1.move()
    ball_2.move()
    ball_1.bounce()
    ball_2.bounce()
#hw - complete that move function 
