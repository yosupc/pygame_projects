import pygame
import random

pygame.init()

# FPS
clock = pygame.time.Clock()

# set screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# creating character's size
character_width = 70
character_height = 70
x_pos = int(screen_width/2) - int(character_width/2)
y_pos = screen_height - character_height

# creating reward
reward_width = 50
reward_height = 50
reward_x = random.randint(0, screen_width - reward_width)
fixed_reward_height = reward_height
reward_y = - fixed_reward_height

running = True
while running:
    framesPS = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # a character move by keyboard arrows
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
    elif x_pos >= screen_width - character_width:
        x_pos = screen_width - character_width
    if y_pos <= 0:
        y_pos = 0
    elif y_pos >= screen_height - character_height:
        y_pos = screen_height - character_height

    screen.fill ((100, 255, 100))
    pygame.draw.rect(screen, (255, 100, 100),(x_pos, y_pos, character_width, character_height))
    pygame.draw.rect(screen, (0, 100, 100),(reward_x, reward_y, reward_width, reward_height))
    
    
    if reward_y == screen_height:
        reward_x = random.randint(0, screen_width - reward_width)
        reward_y = - fixed_reward_height
    else:
        reward_y += 5
        
    pygame.display.update()


pygame.quit()
