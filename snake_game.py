import pygame
width = 750
height = 600
r = 20
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake_game")
background = (255,255,255)
screen.fill(background)
rect = pygame.Rect(0,0,width, height)
pygame.draw.rect(screen,(150,75,220),rect,25)
pygame.display.flip()


class snake:
    def __init__(self,x,y,speed,direction,dots, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.dots = dots
        self.locations = [(x,y),(x+r,y+r),(x+2*r,y+2*r)]
        self.color = color

    def draw(self):
        global r
        pygame.draw.circle(screen,self.color,self.locations[0],r)

    def change_size(self, num):
        self.dots = self.dots + num
        # adds new locations in the self.locations array

    
# 1. finish the draw method
# 2. finish the change_size method
# 3. create the snake object
# 4. show it on the sceen
