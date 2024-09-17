import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Project")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with a color (RGB)
    screen.fill((0, 128, 255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()