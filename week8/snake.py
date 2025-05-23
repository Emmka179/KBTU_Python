import pygame
import random
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
            return x, y

food = generate_food()
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    
    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, BLACK, (*segment, CELL_SIZE, CELL_SIZE))
    
    # Отрисовка еды
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    
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
    

    # Змейка выходит за границу
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

    # Проверка на столкновение со стеной или собой
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    # Проверка на съедение еды
    if new_head == food:
        score += 1
        food = generate_food()
        if score % 4 == 0:
            level += 1
            speed += 2  # Увеличение скорости на новом уровне
    else:
        snake.pop()
    
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
