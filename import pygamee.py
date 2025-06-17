import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add More Sprites")

clock = pygame.time.Clock()
BG_COLOR = (240, 248, 255)

class Bouncer(pygame.sprite.Sprite):
    def __init__(self, color, radius, speed):
        super().__init__()
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - radius*2)
        self.rect.y = random.randint(0, HEIGHT - radius*2)
        self.dx = random.choice([-1, 1]) * speed
        self.dy = random.choice([-1, 1]) * speed

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

sprites = pygame.sprite.Group()
colors = [(255, 105, 180), (144, 238, 144), (255, 165, 0), (0, 191, 255), (138, 43, 226)]

for _ in range(5):
    color = random.choice(colors)
    radius = random.randint(15, 25)
    speed = random.randint(2, 4)
    sprite = Bouncer(color, radius, speed)
    sprites.add(sprite)

running = True
while running:
    clock.tick(60)
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
