import pygame
import random

pygame.init()

# FPS
clock = pygame.time.Clock()

# set screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# creating basket's size
basket_width = 70
basket_height = 70
x_pos = int(screen_width/2) - int(basket_width/2)
y_pos = screen_height - basket_height

# creating basket2 (upper part)
basket_top_width = 70
basket_top_height = 15

class Reward:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = random.randint (0, screen_width - self.width)
        self.y_pos = random.randint(-(self.height*30), -self.height)
    
    def move (self):
        self.y_pos += 5
    
    def update (self):
        self.x_pos = random.randint (0, screen_width - self.width)
        self.y_pos = random.randint(-(self.height*30), -self.height)

reward = Reward("Reward", 30, 30)
reward2 = Reward("Reward2", 40, 40)
reward3 = Reward("Reward3", 50, 50)

score = 0

running = True
while running:
    framesPS = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # a basket move by keyboard arrows
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x_pos -= 5
    if pressed[pygame.K_RIGHT]:
        x_pos += 5

    # move boundaries
    if x_pos <= 0:
        x_pos = 0
    elif x_pos >= screen_width - basket_width:
        x_pos = screen_width - basket_width



    screen.fill ((100, 255, 100))
    pygame.draw.rect(screen, (210,105,30),(x_pos, y_pos, basket_width, basket_height))
    pygame.draw.rect(screen, (100,100,100),(x_pos, y_pos, basket_top_width, basket_top_height)) 
    
    pygame.draw.rect(screen, (255, 255, 0),(reward.x_pos , reward.y_pos, reward.width, reward.height))
    pygame.draw.rect(screen, (255, 255, 0),(reward2.x_pos , reward2.y_pos, reward2.width, reward2.height))
    pygame.draw.rect(screen, (255, 255, 0),(reward3.x_pos , reward3.y_pos, reward3.width, reward3.height))

    reward.move()
    reward2.move()
    reward3.move()

    #print(reward.y_pos)
    if reward.y_pos >= screen_height:
        reward.update()
    if reward2.y_pos >= screen_height:
        reward2.update()
    if reward3.y_pos >= screen_height:
        reward3.update()
        
    pygame.display.update()


pygame.quit()
