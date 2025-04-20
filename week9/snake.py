import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Направления движения
directions = {
    "UP": (0, -CELL_SIZE),
    "DOWN": (0, CELL_SIZE),
    "LEFT": (-CELL_SIZE, 0),
    "RIGHT": (CELL_SIZE, 0)
}

# Инициализация змейки
snake = [(WIDTH // 2, HEIGHT // 2)]  # Начальная позиция
snake_dir = "RIGHT"  # Начальное направление
speed = 10  # Начальная скорость
score = 0
level = 1

# Функция генерации еды в свободной клетке
def generate_food():
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:
            return x, y, random.choice([1, 2, 3])  # Вес еды 1, 2 или 3 очка

food_x, food_y, food_value = generate_food()
food_timer = pygame.time.get_ticks()  # Засекаем время появления еды
FOOD_LIFETIME = 5000  # Время исчезновения еды (5 сек)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    
    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, BLACK, (*segment, CELL_SIZE, CELL_SIZE))  # Проходим по каждому сегменту змейки и рисуем чёрный квадрат
    
    # Проверка таймера еды
    if pygame.time.get_ticks() - food_timer > FOOD_LIFETIME:  # прошло больше 5 секунд — создаём новую еду
        food_x, food_y, food_value = generate_food()
        food_timer = pygame.time.get_ticks()
    
    # Отрисовка еды
    pygame.draw.rect(screen, RED, (food_x, food_y, CELL_SIZE, CELL_SIZE))
    
    # Отображение очков и уровня
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != "DOWN":
                snake_dir = "UP"
            elif event.key == pygame.K_DOWN and snake_dir != "UP":
                snake_dir = "DOWN"
            elif event.key == pygame.K_LEFT and snake_dir != "RIGHT":
                snake_dir = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_dir != "LEFT":
                snake_dir = "RIGHT"
    
    # Движение змейки
    new_head = (snake[0][0] + directions[snake_dir][0], snake[0][1] + directions[snake_dir][1])

    # Телепортация при выходе за границы экрана
    x, y = new_head
    if x < 0:
        x = WIDTH - CELL_SIZE
    elif x >= WIDTH:
        x = 0
    if y < 0:
        y = HEIGHT - CELL_SIZE
    elif y >= HEIGHT:
        y = 0
    new_head = (x, y)

    # Проверка на столкновение с собой
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    # Проверка на съедение еды
    if new_head == (food_x, food_y):
        score += food_value
        food_x, food_y, food_value = generate_food()
        food_timer = pygame.time.get_ticks()
        if score % 4 == 0:
            level += 1
            speed += 2  # Увеличение скорости на новом уровне
    else:
        snake.pop()
    
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
