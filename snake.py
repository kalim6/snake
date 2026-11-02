# Example file showing a circle moving on screen
import pygame
from enum import Enum

# class syntax
class SnakeDirection(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
SPEED = 100
snake_direction = SnakeDirection.RIGHT

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(screen, "red", pygame.rect.Rect(int(player_pos.x) ^ 32,int(player_pos.y) ^ 32, 32, 32) )

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 32
    if keys[pygame.K_s]:
        player_pos.y += 32
    if keys[pygame.K_a]:
        player_pos.x -= 32
    if keys[pygame.K_d]:
        player_pos.x += 32

    player_pos.x += SPEED * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()