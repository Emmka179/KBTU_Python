import pygame
import random
import sys

# Инициализация pygame
pygame.init()

# Параметры экрана
HEIGHT = 600
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Загрузка изображений
road = pygame.image.load(r"C:\Users\bboya\OneDrive\Desktop\pp2\week8\imgs\AnimatedStreet.png")
coin_i = pygame.image.load(r"C:\Users\bboya\OneDrive\Desktop\pp2\week8\imgs\Coin.png")
coin_im = pygame.transform.scale(coin_i, (100, 100))  # Масштабирование монеты
player_im = pygame.image.load(r"C:\Users\bboya\OneDrive\Desktop\pp2\week8\imgs\Player.png")
enemy_im = pygame.image.load(r"C:\Users\bboya\OneDrive\Desktop\pp2\week8\imgs\Enemy.png")

# Шрифт и счет
font = pygame.font.SysFont("Verdana", 30)
count = 0
N = 5  # Количество монет для увеличения скорости врага

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_im
        # self.image = pygame.Surface((30, 60))
        # self.image.fill((255, 0, 0))
        # self.image = pygame.draw.rect(screen, (50, 50, 50), player_im) #изображение игрока
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10)) #задаёт позицию внизу экрана
        self.speed = 5 # скорость игрока
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        # if keys[pygame.K_UP]:
        #     self.rect.move_ip(0, -self.speed)
        # if keys[pygame.K_DOWN]:
        #     self.rect.move_ip(0, self.speed)
        
        self.rect.clamp_ip(screen.get_rect()) #не позволяет выйти за границы экрана

# Класс монеты с разным весом
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(coin_i, (80, 80)) # уменьшает монету до 30x30
        self.rect = self.image.get_rect()
        self.generate()
    
    def generate(self):
        self.rect.topleft = (random.randint(0, WIDTH - self.rect.width), 0) # помещает монету в случайное место сверху
        self.value = random.randint(1, 3)  # Вес монеты от 1 до 3
    
    def move(self):
        self.rect.move_ip(0, 5) # заставляет монету двигаться вниз
        if self.rect.top > HEIGHT:
            self.generate()

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_im
        self.speed = 5 # скорость врага
        self.rect = self.image.get_rect()
        self.generate()
    
    def generate(self):
        self.rect.topleft = (random.randint(0, WIDTH - self.rect.width), 0)
    
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()

# Создание объектов
player = Player()
coin = Coin()
enemy = Enemy()
all_sprites = pygame.sprite.Group(player, coin, enemy)
coin_sprites = pygame.sprite.Group(coin)
enemy_sprites = pygame.sprite.Group(enemy)

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    player.move()
    coin.move()
    enemy.move()
    
    # Проверка сбора монет
    if pygame.sprite.spritecollideany(player, coin_sprites):
        count += coin.value
        coin.generate()
        
        # Увеличение скорости врага при достижении N очков
        if count % N == 0:
            enemy.speed += 1
    
    # Проверка столкновения с врагом
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        screen.fill((255, 0, 0))
        game_over_text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    
    # Отрисовка экрана
    screen.blit(road, (0, 0)) # рисует дорогу
    all_sprites.draw(screen) # рисует все спрайты
    
    score_text = font.render(f"Score: {count}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)