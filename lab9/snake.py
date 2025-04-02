import pygame
import random
import time

pygame.init()

# ұяшық пен экранның парамерлары
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

# Цветтер
B = (0, 0, 0)
G = (0, 255, 0)
DG = (0, 180, 0)
R = (255, 0, 0)
G = (255, 215, 0)
W = (255, 255, 255)

# Экран
s = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

f = pygame.font.SysFont(None, 36)
sf = pygame.font.SysFont(None, 28)
cl = pygame.time.Clock()

# Жаланның киіпі
def draw_snake(snake):
    for seg in snake:
        pygame.draw.rect(s, G, (seg[0] * CELL_SIZE, seg[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# қабырғаның суреті
def draw_walls(walls):
    for wa in walls:
        pygame.draw.rect(s, DG, (wa[0] * CELL_SIZE, wa[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Жай тамақтық генерациясы
def generate_food(snake, walls):
    while True:
        pos = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)]
        if pos not in snake and pos not in walls:
            return {"pos": pos, "weight": 1}

# Редкий тамақтың генерациясы
def generate_big_food(snake, walls):
    while True:
        pos = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)]
        if pos not in snake and pos not in walls:
            return {"pos": pos, "weight": 5, "spawn_time": time.time()}

# тамақтың киіпі
def draw_food(food, is_big=False):
    color = G if is_big else R
    pygame.draw.rect(s, color, (food["pos"][0] * CELL_SIZE, food["pos"][1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Жалпы сурет
def draw_ui(score, level, countdown=None):
    score_text = f.render(f"Score: {score}", True, W)
    level_text = f.render(f"Level: {level}", True, W)
    s.blit(score_text, (10, 10))
    s.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))

    if countdown is not None:
        timer_text = sf.render(f"Big food: {countdown}s", True, G)
        s.blit(timer_text, (WIDTH - timer_text.get_width() - 10, 50))

# Бастапқы мән
snake = [[5, 5]]
direction = [1, 0]
walls = []
score = 0
level = 1
speed = 10
food_to_level = 4

food = generate_food(snake, walls)
big_food = None
food_lifetime = 5 

running = True
while running:
    cl.tick(speed)
    s.fill(B)

    # Ойыннан шығару жүсесі
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Жыланмен басқару
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != [0, 1]:
        direction = [0, -1]
    elif keys[pygame.K_DOWN] and direction != [0, -1]:
        direction = [0, 1]
    elif keys[pygame.K_LEFT] and direction != [1, 0]:
        direction = [-1, 0]
    elif keys[pygame.K_RIGHT] and direction != [-1, 0]:
        direction = [1, 0]

    # Құйрықтың өсуі
    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

    # Жеңілуді тексеру
    if (new_head in snake or new_head in walls or
        not 0 <= new_head[0] < COLS or not 0 <= new_head[1] < ROWS):
        running = False

    snake.insert(0, new_head)

    # Желінген жәй тамақ
    if new_head == food["pos"]:
        score += food["weight"]
        food = generate_food(snake, walls)

        # Әр 5 очко сайын жаңа дәу тамақ шығуы
        if score % 5 == 0 and big_food is None:
            big_food = generate_big_food(snake, walls)

        if score % food_to_level == 0:
            level += 1
            speed += 2

    # Дәу тамақтың желінгені
    elif big_food and new_head == big_food["pos"]:
        score += big_food["weight"]
        big_food = None
    else:
        snake.pop()

    # Тексеру! егер дәу тамақ желінген болса және таймер
    if big_food and time.time() - big_food["spawn_time"] > food_lifetime:
        big_food = None

    # Сурет 
    draw_snake(snake)
    draw_food(food)
    if big_food:
        draw_food(big_food, is_big=True)
        countdown = max(0, int(food_lifetime - (time.time() - big_food["spawn_time"])))
        draw_ui(score, level, countdown)
    else:
        draw_ui(score, level)

    pygame.display.flip()

pygame.quit()
