import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tap the Circle Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game Variables
score = 0
circle_radius = 30
circle_x = random.randint(circle_radius, WIDTH - circle_radius)
circle_y = random.randint(circle_radius, HEIGHT - circle_radius)

# Font for displaying score
font = pygame.font.Font(None, 36)

# Game Loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:  # Left-click
                mouse_x, mouse_y = pygame.mouse.get_pos()
                distance = ((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2) ** 0.5
                if distance < circle_radius:
                    score += 1
                    circle_x = random.randint(circle_radius, WIDTH - circle_radius)
                    circle_y = random.randint(circle_radius, HEIGHT - circle_radius)

    # Draw the circle
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

    # Draw the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    print("You scored 1 point")

    pygame.display.update()

    clock.tick(60)

pygame.quit()
