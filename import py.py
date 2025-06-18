import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game Screen")

WHITE = (255, 255, 255)
VIOLET = (148, 0, 211)
TEXT_COLOR = (0, 0, 0)

font = pygame.font.SysFont("Arial", 30)

rect_width, rect_height = 200, 100
rect_x = (WIDTH - rect_width) // 2
rect_y = (HEIGHT - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

text = font.render("Welcome to my screen!", True, TEXT_COLOR)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, VIOLET, rectangle)
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
