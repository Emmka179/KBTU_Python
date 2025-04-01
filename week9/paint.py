import pygame
import math

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
    
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0))
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                # Exit conditions
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Color selection
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                
                # Tool selection
                if event.key == pygame.K_p:
                    tool = 'pen'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_m:
                    tool = 'rectangle'
                elif event.key == pygame.K_s:  # Square
                    tool = 'square'
                elif event.key == pygame.K_t:  # Right triangle
                    tool = 'right_triangle'
                elif event.key == pygame.K_q:  # Equilateral triangle
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_h:  # Rhombus
                    tool = 'rhombus'
            
            # Mouse button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    start_pos = event.pos
                    drawing = True
                    if tool == 'pen' or tool == 'eraser':
                        points = [event.pos]
                elif event.button == 3:  # Right click to decrease radius
                    radius = max(1, radius - 1)
            
            # Mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:
                    end_pos = event.pos
                    # Draw shapes on canvas when mouse is released
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
                    elif tool == 'square':
                        size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                        rect = pygame.Rect(min(start_pos[0], end_pos[0]), 
                                        min(start_pos[1], end_pos[1]), size, size)
                        pygame.draw.rect(canvas, get_color(mode), rect, 2)
                    elif tool == 'right_triangle':
                        draw_right_triangle(canvas, start_pos, end_pos, get_color(mode))
                    elif tool == 'equilateral_triangle':
                        draw_equilateral_triangle(canvas, start_pos, end_pos, get_color(mode))
                    elif tool == 'rhombus':
                        draw_rhombus(canvas, start_pos, end_pos, get_color(mode))
                    start_pos = None
                    drawing = False
            
            # Mouse movement for free drawing
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if drawing and (tool == 'pen' or tool == 'eraser'):
                    points.append(position)
                    drawLineBetween(canvas, len(points)-2, points[-2], points[-1], radius, mode if tool == 'pen' else 'black')

        # Clear screen and draw canvas
        screen.fill((0, 0, 0))
        screen.blit(canvas, (0, 0))
        
        # Preview shapes while drawing
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
            elif tool == 'square':
                size = max(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                rect = pygame.Rect(min(start_pos[0], current_pos[0]), 
                                 min(start_pos[1], current_pos[1]), size, size)
                pygame.draw.rect(screen, get_color(mode), rect, 2)
            elif tool == 'right_triangle':
                draw_right_triangle(screen, start_pos, current_pos, get_color(mode))
            elif tool == 'equilateral_triangle':
                draw_equilateral_triangle(screen, start_pos, current_pos, get_color(mode))
            elif tool == 'rhombus':
                draw_rhombus(screen, start_pos, current_pos, get_color(mode))
        
        pygame.display.flip()
        clock.tick(60)

# Helper function to get color values
def get_color(color_mode):
    colors = {
        'blue': (0, 0, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'black': (0, 0, 0)
    }
    return colors.get(color_mode, (255, 255, 255))

# Helper function to draw lines for pen/eraser
def drawLineBetween(screen, index, start, end, width, color_mode):
    color = get_color(color_mode)
    pygame.draw.line(screen, color, start, end, width * 2)

# Function to draw a right triangle
def draw_right_triangle(surface, start, end, color):
    points = [
        start,  # First point (start)
        (end[0], start[1]),  # Second point (right angle base)
        end  # Third point (hypotenuse end)
    ]
    pygame.draw.polygon(surface, color, points, 2)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(surface, start, end, color):
    base_length = ((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5
    height = base_length * (math.sqrt(3) / 2)
    mid_x = (start[0] + end[0]) / 2
    apex_y = start[1] - height if start[1] > end[1] else start[1] + height
    points = [
        start,
        end,
        (int(mid_x), int(apex_y))
    ]
    pygame.draw.polygon(surface, color, points, 2)

# Function to draw a rhombus
def draw_rhombus(surface, start, end, color):
    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2
    points = [
        (start[0], mid_y),  # Left point
        (mid_x, start[1]),  # Top point
        (end[0], mid_y),    # Right point
        (mid_x, end[1])     # Bottom point
    ]
    pygame.draw.polygon(surface, color, points, 2)

main()