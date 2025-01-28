import pygame
import sys
import random

class Circle:
    def __init__(self, radius, x, y, vx, vy, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, min_x, min_y, max_x, max_y):
        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius < min_x or self.x + self.radius > max_x:
            self.vx = -self.vx
        
        if self.y - self.radius < min_y or self.y + self.radius > max_y:
            self.vy = -self.vy

pygame.init()

window_width = 500
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))
bg_color = (30, 30, 30)
pygame.display.set_caption("Flying Circles")

N = 10
circles = []
for i in range(N):
    radius = random.randint(5, 15)
    x = random.randint(radius, window_width - radius)
    y = random.randint(radius, window_height - radius)
    vx = random.choice([-1, 1]) * random.randint(2, 5)
    vy = random.choice([-1, 1]) * random.randint(2, 5)
    color = (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255),
    )
    circles.append(Circle(radius, x, y, vx, vy, color))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)
    for circle in circles:
        circle.draw(screen)
        circle.move(0, 0, window_width, window_height)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()