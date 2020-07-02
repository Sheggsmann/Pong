import pygame, sys
from pygame.locals import *
import random

def animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
         ball_speed_x *= -1


width, height = 620, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()

# Game Rectangles
ball = pygame.Rect(width/2 - 10, height/2 - 10 , 20, 20)
player = pygame.Rect(width - 20, height/2 - 70, 10, 140)
opponent = pygame.Rect(10, height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7

player_speed = 0
opponet_speed = 12

def ball_restart():
    global  ball_speed_x, ball_speed_y
    ball.center = (width/2, height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


def playerAnimation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponet_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponet_speed
    if opponent.bottom >= height:
        opponent.bottom = height


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    animation()
    playerAnimation()
    opponent_ai()
    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (width/2, 0), (width/2, height))

    pygame.display.update()
    clock.tick(30)