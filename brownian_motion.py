import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 600, 600
ROBOT_RADIUS = 10
VELOCITY = 2
FPS = 60
# Colors
BG_COLOR = (0, 255, 255)  # Background color (light blue)
CIRCLE_BALL = (0, 128, 255)  # Circle color (blue)


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brownian Motion for JdeRobot")
clock = pygame.time.Clock()

# BrownianMotion class
class BrownianMotion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += VELOCITY * math.cos(self.angle)
        self.y += VELOCITY * math.sin(self.angle)

        # Check collision with boundary
        if self.x - ROBOT_RADIUS <= 0 or self.x + ROBOT_RADIUS >= WIDTH or \
           self.y - ROBOT_RADIUS <= 0 or self.y + ROBOT_RADIUS >= HEIGHT:
            self.rotate_random()

    def rotate_random(self):
        self.angle += random.uniform(math.pi / 3, 3 * math.pi / 4)

    def draw(self, screen):
        pygame.draw.circle(screen, CIRCLE_BALL, (int(self.x), int(self.y)), ROBOT_RADIUS)

# Main loop
def Run():
    brownianMotion = BrownianMotion(WIDTH // 2, HEIGHT // 2)
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        brownianMotion.move()
        brownianMotion.draw(screen)

        pygame.display.flip()

    pygame.quit()

