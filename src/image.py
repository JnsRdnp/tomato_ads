import pygame
import random

class Image:
    def __init__(self, image_path, width=None, height=None):
        self.original_image = pygame.image.load(image_path)
        if width and height:
            self.image = pygame.transform.scale(self.original_image, (width, height))
        else:
            self.image = self.original_image
        self.rect = self.image.get_rect()

        self.button = None

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()

    def center_on_screen(self, screen_width, screen_height):
        self.rect.center = (screen_width // 2, screen_height // 2)

    def random_location(self, screen_width, screen_height, min_x=None):
        max_x = screen_width - self.rect.width
        max_y = screen_height - self.rect.height

        # Default minimum_x to 0 if not provided
        minimum_x = min_x if min_x is not None else 0

        # Ensure that minimum_x does not exceed max_x
        minimum_x = min(minimum_x, max_x)

        # Debug print statements
        print(f"Screen size: ({screen_width}, {screen_height})")
        print(f"Image size: ({self.rect.width}, {self.rect.height})")
        print(f"min_x: {minimum_x}, max_x: {max_x}")

        # Randomly position the image within the allowed range
        x_pos = random.randint(minimum_x, max_x)
        y_pos = random.randint(0, max_y)
        self.rect.topleft = (x_pos, y_pos)

        print(f"New position: {self.rect.topleft}")

    def flip(self, horizontal=False, vertical=False):
        # Flip the image and create a new image
        self.image = pygame.transform.flip(self.image, horizontal, vertical)
        
        # Update the rect to match the new size of the flipped image
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def set_button(self, button):
        self.button = button
        self.button.rect.topleft = self.rect.topleft