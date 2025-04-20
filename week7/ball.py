import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
done = False
ball_radius = 25
ball_x = 800 // 2 
ball_y = 600 // 2
ball_color = (255, 0, 0)
ball_speed = 5 
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and ball_y - ball_radius - ball_speed >= 0:
        ball_y -= ball_speed
        ball_speed += 0.1
    if pressed[pygame.K_DOWN] and ball_y + ball_radius + ball_speed <= 600:
        ball_y += ball_speed
        ball_speed += 0.1
    if pressed[pygame.K_RIGHT] and ball_x + ball_radius + ball_speed <= 800:
        ball_x += ball_speed
        ball_speed += 0.1
    if pressed[pygame.K_LEFT] and ball_x - ball_radius - ball_speed >= 0:
        ball_x -= ball_speed
        ball_speed += 0.1
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 25) # круг
    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(int(ball_x), int(ball_y), 50, 50)) # квадрат

    pygame.display.flip()
    clock.tick(60)
