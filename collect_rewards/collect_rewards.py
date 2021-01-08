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
top_x = x_pos
top_y = y_pos

# creating reward
reward_width = 50
reward_height = 50
reward_x = random.randint(0, screen_width - reward_width)
fixed_reward_height = reward_height
reward_y = - fixed_reward_height

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
    if pressed[pygame.K_UP]:
        y_pos -= 5
    if pressed[pygame.K_DOWN]:
        y_pos += 5

    # move boundaries
    if x_pos <= 0:
        x_pos = 0
    elif x_pos >= screen_width - basket_width:
        x_pos = screen_width - basket_width
    if y_pos <= 0:
        y_pos = 0
    elif y_pos >= screen_height - basket_height:
        y_pos = screen_height - basket_height

    screen.fill ((100, 255, 100))
    pygame.draw.rect(screen, (210,115,30),(x_pos, y_pos, basket_width, basket_height))
    pygame.draw.rect(screen, (100,100,100),(x_pos, y_pos, basket_top_width, basket_top_height))    
    pygame.draw.rect(screen, (255, 255, 0),(reward_x, reward_y, reward_width, reward_height))
    
    
    if reward_y == screen_height:
        reward_x = random.randint(0, screen_width - reward_width)
        reward_y = - fixed_reward_height
    else:
        reward_y += 5

    # reward collision
    if reward_y == y_pos:
        tmp = reward_x
        basket_range_x = x_pos + basket_width
        for i in range (reward_width):
            if x_pos <= tmp & tmp <= basket_range_x:
                score += 10
                reward_x = random.randint(0, screen_width - reward_width)
                reward_y = - fixed_reward_height
                print("score: ", score)
                break
            tmp += 1
        
    pygame.display.update()


pygame.quit()
