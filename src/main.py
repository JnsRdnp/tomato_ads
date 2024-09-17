import pygame
import os
from image import Image



def main():
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tomaattikisa")

    # Create Image instances
    maalitaulu_path = os.path.join("assets", "maalitaulu.png")
    maalitaulu = Image(maalitaulu_path, 150, 150)  # Initial size 100x100
    maalitaulu.center_on_screen(width, height)


    # Ernesti
    ernesti_path = os.path.join("assets", "erne.png")
    ernesti = Image(ernesti_path, 100, 100)  # Initial size 100x100
    ernesti.random_location(width,height,width-200)
    ernesti.flip(True)

    # Kernesti
    kernesti_path = os.path.join("assets", "kerne.png")
    kernesti = Image(kernesti_path, 100, 100)  # Initial size 100x100
    kernesti.random_location(width/5,height)



    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color (RGB)
        screen.fill((0, 128, 255))

        # Draw the image
        maalitaulu.draw(screen)
        ernesti.draw(screen)
        kernesti.draw(screen)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()