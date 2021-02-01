import pygame
import random

pygame.init()

# FPS
clock = pygame.time.Clock()

# set screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# creating Basket class
class Basket:
    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
    
# creating basket size
basket_width = 70
basket_height = 70
x_pos = int(screen_width/2) - int(basket_width/2)
y_pos = screen_height - basket_height
basket = Basket("Basket", basket_width, basket_height, x_pos, y_pos)


# creating basket2 (upper part)
basket_top_width = 70
basket_top_height = 15

class Reward:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = random.randint (0, screen_width - self.width)
        self.y_pos = random.randint(-(self.height), -self.height)
    
    def move (self):
        self.y_pos += 5
    
    def update (self):
        self.x_pos = random.randint (0, screen_width - self.width)
        self.y_pos = random.randint(-(self.height*30), -self.height)

reward = Reward("Reward", 30, 30)
reward2 = Reward("Reward2", 40, 40)
reward3 = Reward("Reward3", 50, 50)

def myCollision (basket_c, reward_c, score_check):
    tmp = reward_c.x_pos
    tmp2 = basket_c.x_pos
    basket_end = basket_c.x_pos + basket_c.width

    for i in range (reward_c.width):
        for j in range (basket_c.width):
            if tmp == tmp2:
                score_check += 10
                return True
            tmp2 += 1
        tmp += 1
        tmp2 = basket_c.x_pos
    return False


font = pygame.font.SysFont(None, 50)
img = font.render ("PRESS SPACE TO START", True, (0,0,0))
on_off = False


check_once = 0
score = 0
print("score is" , score)
collision_line = screen_height - basket_height
running = True
while running:
    framesPS = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_SPACE]:
        on_off = True

    elif on_off:
        # a basket move by keyboard arrows
        if pressed[pygame.K_LEFT]:
            basket.x_pos -= 5
        if pressed[pygame.K_RIGHT]:
            basket.x_pos += 5

        # move boundaries
        if basket.x_pos <= 0:
            basket.x_pos = 0
        elif basket.x_pos >= screen_width - basket.width:
            basket.x_pos = screen_width - basket.width



        screen.fill ((100, 255, 100))
        pygame.draw.rect(screen, (210,105,30),(basket.x_pos, basket.y_pos, basket.width, basket.height))
        pygame.draw.rect(screen, (100,100,100),(basket.x_pos, basket.y_pos, basket_top_width, basket_top_height)) 
        
        pygame.draw.rect(screen, (255, 255, 0),(reward.x_pos , reward.y_pos, reward.width, reward.height))
        pygame.draw.rect(screen, (255, 255, 0),(reward2.x_pos , reward2.y_pos, reward2.width, reward2.height))
        pygame.draw.rect(screen, (255, 255, 0),(reward3.x_pos , reward3.y_pos, reward3.width, reward3.height))

        reward.move()
        reward2.move()
        reward3.move()

        if reward.y_pos >= screen_height:
            reward.update()
            check_once = 0
        if reward2.y_pos >= screen_height:
            reward2.update()
            check_once = 0
        if reward3.y_pos >= screen_height:
            reward3.update()
            check_once = 0
            
        if reward.y_pos + reward.height >= collision_line:
            if check_once == 0 and myCollision(basket, reward, score):
                score += 10
                print("score is" , score)
            check_once += 1
        if reward2.y_pos + reward2.height >= collision_line:
            if check_once == 0 and myCollision(basket, reward2, score):
                score += 10
                print("score is" , score)
            check_once += 1
        if reward3.y_pos + reward3.height >= collision_line:
            if check_once == 0 and myCollision(basket, reward3, score):
                score += 10
                print("score is" , score)
            check_once += 1

    else:
        screen.fill((100,255,100))
        screen.blit(img, (115, 250))

    pygame.display.update()


pygame.quit()
