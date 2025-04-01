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
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Направления движения
directions = {"UP": (0, -CELL_SIZE), "DOWN": (0, CELL_SIZE), "LEFT": (-CELL_SIZE, 0), "RIGHT": (CELL_SIZE, 0)}

# Инициализация змейки
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_dir = "RIGHT"
speed = 10
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
        pygame.draw.rect(screen, BLACK, (*segment, CELL_SIZE, CELL_SIZE))
    
    # Проверка таймера еды
    if pygame.time.get_ticks() - food_timer > FOOD_LIFETIME:
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
    
    # Проверка на столкновение со стеной или собой
    if new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
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
