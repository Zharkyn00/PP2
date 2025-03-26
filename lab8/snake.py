import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, DARK_GREEN, (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def generate_food(snake, walls):
    while True:
        pos = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)]
        if pos not in snake and pos not in walls:
            return pos

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_ui(score, level):
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))

snake = [[5, 5]]
direction = [1, 0]
food = generate_food(snake, [])
walls = []
score = 0
level = 1
speed = 10  
food_to_level = 4  

running = True
while running:
    clock.tick(speed)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != [0, 1]:
        direction = [0, -1]
    elif keys[pygame.K_DOWN] and direction != [0, -1]:
        direction = [0, 1]
    elif keys[pygame.K_LEFT] and direction != [1, 0]:
        direction = [-1, 0]
    elif keys[pygame.K_RIGHT] and direction != [-1, 0]:
        direction = [1, 0]

    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

    if (new_head in snake or                 
        new_head in walls or                 
        not 0 <= new_head[0] < COLS or      
        not 0 <= new_head[1] < ROWS):       
        running = False  

    snake.insert(0, new_head)

   
    if new_head == food:
        score += 1
        food = generate_food(snake, walls)

        
        if score % food_to_level == 0:
            level += 1
            speed += 2  
    else:
        snake.pop()  
    
    draw_snake(snake)
    draw_food(food)
    draw_walls(walls)
    draw_ui(score, level)

    pygame.display.flip()

pygame.quit()