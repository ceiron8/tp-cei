import pygame
import random
import math
#Instructions this game read it
#Click on the fruits as they move down the screen to slice them and earn points
# Avoid missing fruits and try to get the highest score before the game ends.

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


FPS = 30
FPS_CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Fruit Ninja")


class Fruit:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.moving = True
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def move(self):
        if self.moving:
            self.y -= 5
            if self.y < 0:
                self.y = SCREEN_HEIGHT
                self.x = random.randint(self.radius, SCREEN_WIDTH - self.radius)

fruits = [
    Fruit(random.randint(30, SCREEN_WIDTH - 30), SCREEN_HEIGHT - 30, RED, 30),
    Fruit(random.randint(30, SCREEN_WIDTH - 30), SCREEN_HEIGHT - 30, GREEN, 30),
    Fruit(random.randint(30, SCREEN_WIDTH - 30), SCREEN_HEIGHT - 30, BLUE, 30)
]


running = True
score = 0
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    
    if mouse_pressed[0]: 
        for fruit in fruits:
            if math.sqrt((mouse_x - fruit.x) ** 2 + (mouse_y - fruit.y) ** 2) < fruit.radius:
                fruit.y = SCREEN_HEIGHT 
                fruit.x = random.randint(fruit.radius, SCREEN_WIDTH - fruit.radius)
                score += 1
    
    
    for fruit in fruits:
        fruit.move()
    
    
    screen.fill(WHITE)
    
    for fruit in fruits:
        fruit.draw()
    
    
    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    FPS_CLOCK.tick(FPS)

pygame.quit()

