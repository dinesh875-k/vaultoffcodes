import pygame
import random
import time

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# Colors
black = pygame.Color(20, 20, 20)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 50, 50)
green = pygame.Color(50, 255, 50)
blue = pygame.Color(50, 50, 255)
gray = pygame.Color(50, 50, 50)

# Initialize pygame
pygame.init()

# Game window
pygame.display.set_caption('Modern Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Snake initial position
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# Directions
direction = 'RIGHT'
change_to = direction

# Initial score
score = 0

# Show score
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size, bold=True)
    score_surface = score_font.render(f'Score: {score}', True, color)
    score_rect = score_surface.get_rect()
    score_rect.topright = (window_x - 20, 20)
    game_window.blit(score_surface, score_rect)

# Game over
def game_over():
    my_font = pygame.font.SysFont('arial', 50, bold=True)
    game_over_surface = my_font.render(f'Your Score: {score}', True, red)
    game_over_rect = game_over_surface.get_rect(center=(window_x/2, window_y/2))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validate direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake growth
    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True

    # Background
    game_window.fill(black)
    
    # Draw grid (optional)
    for x in range(0, window_x, 20):
        pygame.draw.line(game_window, gray, (x, 0), (x, window_y))
    for y in range(0, window_y, 20):
        pygame.draw.line(game_window, gray, (0, y), (window_x, y))

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10), border_radius=5)

    # Draw fruit
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10), border_radius=5)

    # Game over conditions
    if (snake_position[0] < 0 or snake_position[0] > window_x-10 or
        snake_position[1] < 0 or snake_position[1] > window_y-10):
        game_over()

    # Check self collision
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Display score
    show_score(white, 'arial', 24)

    # Refresh screen
    pygame.display.update()
    fps.tick(snake_speed)
