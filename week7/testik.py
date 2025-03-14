import pygame
import time
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
WHITE = (255, 255, 255)

# Load Mickey image and hand images
mickey = pygame.image.load("images\mickeyclock.jpeg")  # Ensure the image is in the correct path
minute_hand = pygame.image.load("images\minutes.png")
second_hand = pygame.image.load("images\hours.png")

# Resize images
mickey = pygame.transform.scale(mickey, (WIDTH, HEIGHT))

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    screen.blit(mickey, (0, 0))
    
    # Get current time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    
    # Calculate angles
    sec_angle = -6 * seconds  # Each second moves by -6 degrees
    min_angle = -6 * minutes  # Each minute moves by -6 degrees
    
    # Rotate hands
    rotated_sec_hand = pygame.transform.rotate(second_hand, sec_angle)
    rotated_min_hand = pygame.transform.rotate(minute_hand, min_angle)
    
    # Get new rect to blit at center
    sec_rect = rotated_sec_hand.get_rect(center=CENTER)
    min_rect = rotated_min_hand.get_rect(center=CENTER)
    
    screen.blit(rotated_sec_hand, sec_rect.topleft)
    screen.blit(rotated_min_hand, min_rect.topleft)
    
    pygame.display.flip()
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(30)  # Limit FPS

pygame.quit()
