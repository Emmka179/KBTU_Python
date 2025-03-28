import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    tool = 'pen'
    points = []
    start_pos = None
    drawing = False
    
    # Создаем поверхность для постоянного рисования
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0))
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Выбор цвета
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                
                # Выбор инструмента
                if event.key == pygame.K_p:
                    tool = 'pen'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_m:
                    tool = 'rectangle'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    start_pos = event.pos
                    drawing = True
                    if tool == 'pen' or tool == 'eraser':
                        points = [event.pos]
                elif event.button == 3:  # Правая кнопка мыши
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:
                    end_pos = event.pos
                    if tool == 'circle':
                        center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                        radius_circle = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
                        pygame.draw.circle(canvas, get_color(mode), center, radius_circle, 2)
                    elif tool == 'rectangle':
                        rect = pygame.Rect(min(start_pos[0], end_pos[0]), 
                                        min(start_pos[1], end_pos[1]),
                                        abs(end_pos[0] - start_pos[0]),
                                        abs(end_pos[1] - start_pos[1]))
                        pygame.draw.rect(canvas, get_color(mode), rect, 2)
                    start_pos = None
                    drawing = False
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if drawing:
                    if tool == 'pen':
                        points.append(position)
                        drawLineBetween(canvas, len(points)-2, points[-2], points[-1], radius, mode)
                    elif tool == 'eraser':
                        points.append(position)
                        drawLineBetween(canvas, len(points)-2, points[-2], points[-1], radius, 'black')

        # Отрисовка
        screen.fill((0, 0, 0))
        screen.blit(canvas, (0, 0))
        
        # Предварительный просмотр при рисовании фигур
        if drawing and start_pos:
            current_pos = pygame.mouse.get_pos()
            if tool == 'circle':
                center = ((start_pos[0] + current_pos[0]) // 2, (start_pos[1] + current_pos[1]) // 2)
                radius_circle = int(((current_pos[0] - start_pos[0]) ** 2 + (current_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
                pygame.draw.circle(screen, get_color(mode), center, radius_circle, 2)
            elif tool == 'rectangle':
                rect = pygame.Rect(min(start_pos[0], current_pos[0]), 
                                 min(start_pos[1], current_pos[1]),
                                 abs(current_pos[0] - start_pos[0]),
                                 abs(current_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, get_color(mode), rect, 2)
        
        pygame.display.flip()
        clock.tick(60)

def get_color(color_mode):
    colors = {
        'blue': (0, 0, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'black': (0, 0, 0)
    }
    return colors.get(color_mode, (255, 255, 255))

def drawLineBetween(screen, index, start, end, width, color_mode):
    color = get_color(color_mode)
    pygame.draw.line(screen, color, start, end, width * 2)

main()