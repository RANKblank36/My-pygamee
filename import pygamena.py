import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event Demo")
clock = pygame.time.Clock()

BG_COLOR = (25, 25, 112)
STAR_COLOR = (255, 215, 0)

stars = []

SPAWN_STAR = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_STAR, 2000)

running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_STAR:

            x = random.randint(10, WIDTH - 10)
            y = random.randint(10, HEIGHT - 10)
            stars.append((x, y))

    for star in stars:
        pygame.draw.circle(screen, STAR_COLOR, star, 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()