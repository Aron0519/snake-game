import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
BLOCK_SIZE = 20

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 35)

def draw_text(text, color, x, y):
    msg = font.render(text, True, color)
    screen.blit(msg, (x, y))

def game_loop():
    snake_pos = [100, 50]
    snake_body = [[100, 50], [80, 50], [60, 50]]
    direction = "RIGHT"
    change_to = direction

    food_pos = [
        random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
        random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE
    ]

    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"

        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        if change_to == "DOWN" and direction != "UP":
            direction = "DOWN"
        if change_to == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        if change_to == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"

        if direction == "UP":
            snake_pos[1] -= BLOCK_SIZE
        if direction == "DOWN":
            snake_pos[1] += BLOCK_SIZE
        if direction == "LEFT":
            snake_pos[0] -= BLOCK_SIZE
        if direction == "RIGHT":
            snake_pos[0] += BLOCK_SIZE

        snake_body.insert(0, list(snake_pos))

        if snake_pos == food_pos:
            score += 10
            food_pos = [
                random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE
            ]
        else:
            snake_body.pop()

        if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
            running = False

        for block in snake_body[1:]:
            if snake_pos == block:
                running = False

        screen.fill(BLACK)
        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

        draw_text(f"Score: {score}", WHITE, 10, 10)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
