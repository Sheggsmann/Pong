#! python3

# The ai is not fully functional it just moves up and down
# You can look up the ai in my version
# And i left the collision part up to u
# Sheggsmann

# Pong-solutions
# Pong-solutions
import pygame
from sys import exit
from pygame.locals import*

#sprite_file = "Images/name.jpg"

pygame.init()

# width for screen width
# Height for screen height
width, height = 640, 480

screen = pygame.display.set_mode((width, height), 0, 32)

#sprite = pygame.image.load(sprite_file)

# speed_x, speed_y = 133, 170
ball_speed_x = 3
ball_speed_y = 3
ball_width = 20
ball_y = 240
ball_x = 320

paddle_move_y = 5
paddle2_move_y = 5
paddle = Rect(20, 20, 20, 100)
paddle2 = Rect(600, 20, 20, 100)
paddle_y = 20
paddle2_y = 20

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # A better way to implement key_presses instead of KEY_DOWN and KEY_UP
    # it returns a dictionary of all events that happened in the game
    # I store it in a variable named keys
    keys = pygame.key.get_pressed()

    # Then use dictionary lookup method to assign a function to the key that was pressed
    if keys[K_UP] and paddle2_y > 0:
        paddle2_y -= paddle2_move_y
    elif keys[K_DOWN] and paddle2_y < height - (100):   # change 100 to a variable eg: paddle_height = 100
        paddle2_y += paddle2_move_y

    screen.fill((255, 255, 255))
    #screen.blit(sprite, (100, 100))

    paddle_y += paddle_move_y
    paddle = Rect(20, paddle_y, 20, 100)
    if paddle_y > 400 - 20:
        paddle_move_y *= -1
    elif paddle_y < 0:
        paddle_move_y *= -1

    paddle2 = Rect(600, paddle2_y, 20, 100)

    # When u multiply d speed by (-1) it makes it -ve or +ve depending on where it is
    # When u add or subtract 4rm d x and y co-ordinates at the xame time, it gives u a diagonal movement
    # Notice how the ball changes direction on hitting co_ordinates
    # Study the physics, I trust u!!!

    if ball_x < 0 + ball_width or ball_x > width - ball_width:
        ball_speed_x *= -1
    if ball_y < 0 + ball_width or ball_y > height - ball_width:
        ball_speed_y *= -1

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    pygame.draw.rect(screen, (0, 0, 0), paddle)
    pygame.draw.rect(screen, (0, 0, 0), paddle2)
    pygame.draw.circle(screen, (0, 0, 0), (ball_x, ball_y), ball_width)

    clock.tick(30)      # Handle game speed: try commenting this line out and see what happens

    pygame.display.update()