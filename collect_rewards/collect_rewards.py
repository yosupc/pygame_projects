import pygame

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
x_pos = screen_width/2 - screen_width/2
y_pos = screen_height - character_height

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
    

    screen.fill ((100, 255, 100))
    pygame.draw.rect(screen, (255, 100, 100),(x_pos, y_pos, character_width, character_height))
    pygame.display.update()


pygame.quit()
