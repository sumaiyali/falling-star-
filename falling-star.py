import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Stars")

clock = pygame.time.Clock()

# Spaceship properties
spaceship_width = 50
spaceship_height = 50
spaceship_x = (WIDTH - spaceship_width) // 2
spaceship_y = HEIGHT - spaceship_height - 10
spaceship_speed = 5

# Star properties
star_width = 25
star_height = 25
star_x = random.randint(0, WIDTH - star_width)
star_y = -star_height
star_speed = 3

score = 0
font = pygame.font.Font(None, 36)

game_over = False

def draw_spaceship(x, y):
    pygame.draw.rect(window, WHITE, (x, y, spaceship_width, spaceship_height))

def draw_star(x, y):
    pygame.draw.rect(window, WHITE, (x, y, star_width, star_height))

def display_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

def game_over_message():
    text = font.render("Game Over", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_x < WIDTH - spaceship_width:
        spaceship_x += spaceship_speed

    window.fill(BLACK)

    draw_spaceship(spaceship_x, spaceship_y)
    draw_star(star_x, star_y)

    # Update star position
    star_y += star_speed

    # Check for collision
    if star_y + star_height >= spaceship_y and spaceship_x <= star_x <= spaceship_x + spaceship_width:
        score += 1
        star_x = random.randint(0, WIDTH - star_width)
        star_y = -star_height

    # Check if star reaches the bottom
    if star_y >= HEIGHT:
        star_x = random.randint(0, WIDTH - star_width)
        star_y = -star_height

    display_score()

    pygame.display.update()
    clock.tick(60)

# Clean up
pygame.quit()
