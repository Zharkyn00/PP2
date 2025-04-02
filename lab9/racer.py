import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Настройки экрана и игры
f = 60
fs = pygame.time.Clock()
B = (0, 0, 0)
R = (255, 0, 0)
SW = 400
SH = 600
SPEED = 3
SCORE = 0
COINS = 0
COINS_COLLECTED = 0  # Үлкен монетаны санайтын айнымалы

font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, B)

screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Racer")

# Фон
background = pygame.image.load("im/road.JPG")
background = pygame.transform.scale(background, (SW, SH))

# Жасыл машинаның класы
class Enemy(pygame.sprite.Sprite):
    def __init__(self, lane='left'):
        super().__init__()
        self.image = pygame.image.load("im/green_car.png")
        self.image = pygame.transform.scale(self.image, (50, 100))

        if lane == 'left':
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect = self.image.get_rect(center=(80, 0))
        else:
            self.rect = self.image.get_rect(center=(300, 0))

        self.lane = lane

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SH:
            SCORE += 1
            if self.lane == 'left':
                self.rect.center = (80, 0)
            else:
                self.rect.center = (300, 0)

# Монытаның класы
class Coin(pygame.sprite.Sprite):
    def __init__(self, big=False):
        super().__init__()
        self.big = big
        self.image = pygame.image.load("im/coin.png")
        size = 60 if big else 40
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, SW - 60), random.randint(-100, -40))

    def move(self):
        global COINS, COINS_COLLECTED

        if self.big:
            COINS += 2
        else:
            COINS += 1

        COINS_COLLECTED += 1
        self.kill()

        big = (COINS_COLLECTED % 5 == 0)
        new_coin = Coin(big=big)
        coinss.add(new_coin)
        all_sprites.add(new_coin)

    def update(self):
        self.rect.y += SPEED
        if self.rect.top > SH:
            self.kill()
            big = (COINS_COLLECTED % 5 == 0)
            new_coin = Coin(big=big)
            coinss.add(new_coin)
            all_sprites.add(new_coin)

# Ойыншының класы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("im/yellow_car.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(center=(160, 520))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < SW:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] and self.rect.bottom < SH:
            self.rect.move_ip(0, 5)

# Объектер
P1 = Player()
E1 = Enemy(lane='left')
E2 = Enemy(lane='right')
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1, E2)

coinss = pygame.sprite.Group()
coinss.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, E2, C1)

# Жылдамдықты әр секунд сайын қосып отыратын счетчик 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

background_y = 0

# Басты цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Жасыл машинамен соғысқанда
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(R)
        screen.blit(game_over, (100, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Фонның қимылы
    background_y = (background_y + SPEED) % SH
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - SH))

    # Счет
    screen.blit(font_small.render("Score: " + str(SCORE), True, B), (10, 10))
    screen.blit(font_small.render("Coins: " + str(COINS), True, B), (300, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        if isinstance(entity, Coin):
            entity.update()
        elif hasattr(entity, 'move'):
            entity.move()

    # Монетаны жинау
    for coin in pygame.sprite.spritecollide(P1, coinss, False):
        coin.move()

    pygame.display.update()
    fs.tick(f)
