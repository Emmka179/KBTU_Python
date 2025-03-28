import pygame
import random
import sys

# Инициализация библиотеки pygame
pygame.init()

# Задание размеров экрана
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

# Шрифт для отображения счета
font = pygame.font.SysFont("Verdana", 30)
count = 0  # Очки игрока

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_im
        self.speed = 5  # Скорость движения
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 10)  # Начальная позиция внизу экрана
    
    def move(self):
        keys = pygame.key.get_pressed()  # Получение нажатий клавиш
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)  # Движение вправо
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)  # Движение влево
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)  # Движение вверх
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)  # Движение вниз

        # Ограничение выхода за границы экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_im
        self.speed = 7  # Скорость падения
        self.rect = self.image.get_rect()
        self.generate()  # Установка начального положения

    def generate(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)  # Случайная позиция по ширине
        self.rect.bottom = 0  # Начинает падать сверху

    def move(self):
        self.rect.move_ip(0, self.speed)  # Движение вниз
        if self.rect.top > HEIGHT:
            self.generate()  # Если монета вышла за экран — генерируем новую

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_im
        self.speed = 8  # Скорость падения
        self.rect = self.image.get_rect()
        self.generate()

    def generate(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)  # Случайное появление по ширине
        self.rect.bottom = 0  # Враг появляется сверху

    def move(self):
        self.rect.move_ip(0, self.speed)  # Движение вниз
        if self.rect.top > HEIGHT:
            self.generate()  # Если вышел за экран — создаем нового

# Создание объектов
player = Player()
coin = Coin()
enemy = Enemy()

# Создание групп спрайтов
all_sprites = pygame.sprite.Group(player, coin, enemy)
coin_sprites = pygame.sprite.Group(coin)
enemy_sprites = pygame.sprite.Group(enemy)

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Выход из игры
            pygame.quit()
            sys.exit()

    # Движение объектов
    player.move()
    coin.move()
    enemy.move()

    # Проверка столкновения игрока с монетой
    if pygame.sprite.spritecollideany(player, coin_sprites):
        count += 1  # Увеличение счета
        coin.generate()  # Новая монета

    # Проверка столкновения игрока с врагом (конец игры)
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        pygame.time.delay(1000)  # Пауза перед завершением игры
        screen.fill((255, 0, 0))  # Заливка экрана красным
        game_over_text = font.render("Game Over!", True, (0, 0, 0))  # Текст "Game Over"
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Задержка перед выходом
        pygame.quit()
        sys.exit()

    # Отрисовка фона и объектов
    screen.blit(road, (0, 0))
    all_sprites.draw(screen)

    # Отображение счета
    score_text = font.render(f"Score: {count}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)  # Ограничение FPS до 60 кадров в секунду
