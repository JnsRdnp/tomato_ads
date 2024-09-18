import pygame
import os
import threading
from image import Image
from button import Button

def throw_tomato(image, target, secondtarget):
    if image.score <= 1:
        image.start_throw_tomato(target)
    else:
        image.start_throw_tomato(secondtarget)


    while image.tomaatti_in_motion:
        image.update_tomato_position()
        pygame.time.delay(1)

def main():
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tomaattikisa")

    maalitaulu_path = os.path.join("assets", "maalitaulu.png")
    maalitaulu = Image(maalitaulu_path, 150, 150)
    maalitaulu.center_on_screen(width, height)

    ernesti_path = os.path.join("assets", "erne.png")
    ernesti = Image(ernesti_path, 100, 100, player=True)
    ernesti.random_location(width, height, width-200)
    ernesti.flip(True)
    ernestiPaikka = Button(width-200, height-48, 80, 40, "Liiku", (0, 0, 0), (255, 255, 255))
    ernestiPaikkaRect = ernestiPaikka.rect
    ernestiHeitto = Button(ernestiPaikkaRect.x + ernestiPaikkaRect.width + 10, height-48, 80, 40, "Heitä", (0, 0, 0), (255, 255, 255))

    kernesti_path = os.path.join("assets", "kerne.png")
    kernesti = Image(kernesti_path, 100, 100, player=True)
    kernesti.random_location(width / 5, height)
    kernestiPaikka = Button(width / 12, height-48, 80, 40, "Liiku", (0, 0, 0), (255, 255, 255))
    kernestiPaikkaRect = kernestiPaikka.rect
    kernestiHeitto = Button(kernestiPaikkaRect.x + kernestiPaikkaRect.width + 10, height-48, 80, 40, "Heitä", (0, 0, 0), (255, 255, 255))

    heitto = Button(width / 2.25, height-55, 150, 30, "< HEITTO >", (0, 0, 0), (255, 255, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if kernestiPaikka.is_clicked(event):
                kernesti.random_location(width / 4, height)

            if ernestiPaikka.is_clicked(event):
                ernesti.random_location(width, height, width-200)

            if ernestiHeitto.is_clicked(event):
                print("Ernesti heitti")
                threading.Thread(target=throw_tomato, args=(ernesti, maalitaulu, kernesti)).start()

            if kernestiHeitto.is_clicked(event):
                print("Kernesti heitti")
                threading.Thread(target=throw_tomato, args=(kernesti, maalitaulu, ernesti)).start()

            if heitto.is_clicked(event):
                threading.Thread(target=throw_tomato, args=(ernesti, maalitaulu, kernesti)).start()
                threading.Thread(target=throw_tomato, args=(kernesti, maalitaulu, ernesti)).start()

        screen.fill((0, 128, 255))

        maalitaulu.draw(screen)
        kernesti.draw(screen)
        ernesti.draw(screen)
        kernestiPaikka.draw(screen)
        ernestiPaikka.draw(screen)
        kernestiHeitto.draw(screen)
        ernestiHeitto.draw(screen)
        heitto.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
