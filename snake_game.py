import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)

# Game settings
snake_block = 10
snake_speed = 15

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 25)

# Score display
def show_score(score):
    text = font.render(f"Score: {score}", True, black)
    win.blit(text, [10, 10])

# Draw the snake
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(win, green, [block[0], block[1], snake_block, snake_block])

# Game over message
def game_over_message():
    msg = font.render("Game Over! Press C to play again or Q to quit", True, red)
    win.blit(msg, [width // 12, height // 3])

# Main game function
def game_loop():
    game_over = False
    game_close = False

    # Snake starting position
    x = width // 2
    y = height // 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    # Random food position
    food_x = random.randint(0, (width - snake_block) // 10) * 10
    food_y = random.randint(0, (height - snake_block) // 10) * 10

    while not game_over:
        while game_close:
            win.fill(white)
            game_over_message()
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        # Key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = snake_block
                    x_change = 0

        # Boundary check
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        win.fill(white)

        # Draw food
        pygame.draw.rect(win, blue, [food_x, food_y, snake_block, snake_block])

        # Update snake
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        # Eating food
        if x == food_x and y == food_y:
            food_x = random.randint(0, (width - snake_block) // 10) * 10
            food_y = random.randint(0, (height - snake_block) // 10) * 10
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
game_loop()
