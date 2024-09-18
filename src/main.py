import pygame
import os
from image import Image
from button import Button



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
    ernesti = Image(ernesti_path, 100, 100, player=True)  # Initial size 100x100
    ernesti.random_location(width,height,width-200)
    ernesti.flip(True)
    ernestiPaikka = Button(width-200, height-48, 80, 40, "Liiku", (0, 0, 0), (255, 255, 255))
    ernestiPaikkaRect = ernestiPaikka.rect
    ernestiHeitto = Button(ernestiPaikkaRect.x + ernestiPaikkaRect.width+10, height-48, 80, 40, "Heitä", (0, 0, 0), (255, 255, 255))

    # Kernesti
    kernesti_path = os.path.join("assets", "kerne.png")
    kernesti = Image(kernesti_path, 100, 100, player=True)  # Initial size 100x100
    kernesti.random_location(width/5,height)
    kernestiPaikka = Button(width/12, height-48, 80, 40, "Liiku", (0, 0, 0), (255, 255, 255))
    kernestiPaikkaRect = kernestiPaikka.rect
    kernestiHeitto = Button(kernestiPaikkaRect.x + kernestiPaikkaRect.width+10, height-48, 80, 40, "Heitä", (0, 0, 0), (255, 255, 255))


    heitto = Button(width/2.25, height-55, 150, 30, "< HEITTO >", (0, 0, 0), (255, 255, 255))


    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if kernestiPaikka.is_clicked(event):
                kernesti.random_location(width/5,height)

            if ernestiPaikka.is_clicked(event):
                ernesti.random_location(width,height,width-200)

            if ernestiHeitto.is_clicked(event):
                print("Ernesti heitti")

                ernesti.start_throw_tomato(maalitaulu)
                

            if kernestiHeitto.is_clicked(event):
                
                kernesti.start_throw_tomato(maalitaulu)

            # Throw together
            if heitto.is_clicked(event):
                ernesti.start_throw_tomato(maalitaulu)
                kernesti.start_throw_tomato(maalitaulu)




        # Fill the screen with a color (RGB)
        screen.fill((0, 128, 255))

        # Draw the image
        maalitaulu.draw(screen)
        # ernesti.draw(screen)
        # kernesti.draw(screen)

        # Draw the button
        kernestiPaikka.draw(screen)
        ernestiPaikka.draw(screen)

        ernestiHeitto.draw(screen)
        kernestiHeitto.draw(screen)

        heitto.draw(screen)

        


        kernesti.update(screen)
        ernesti.update(screen)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()