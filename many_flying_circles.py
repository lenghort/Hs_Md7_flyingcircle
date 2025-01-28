import pygame
import sys
import random
import math

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

    def check_collision(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < self.radius + other.radius:
            self.vx, other.vx = other.vx, self.vx
            self.vy, other.vy = other.vy, self.vy

            overlap = 0.5 * (self.radius + other.radius - distance + 1)
            angle = math.atan2(dy, dx)
            self.x += math.cos(angle) * overlap
            self.y += math.sin(angle) * overlap
            other.x -= math.cos(angle) * overlap
            other.y -= math.sin(angle) * overlap

pygame.init()

window_width = 500
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))
bg_color = (30, 30, 30)
pygame.display.set_caption("Flying Circles")

N = 10
circles = []
for i in range(N):
    radius = random.randint(10, 20)
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

    for i, circle in enumerate(circles):
        circle.draw(screen)
        circle.move(0, 0, window_width, window_height)

        for j in range(i + 1, len(circles)):
            circle.check_collision(circles[j])

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
