import pygame
import random
import os

class Image:
    def __init__(self, image_path, width=None, height=None, player=False):
        self.original_image = pygame.image.load(image_path)
        if width and height:
            self.image = pygame.transform.scale(self.original_image, (width, height))
        else:
            self.image = self.original_image
        self.rect = self.image.get_rect()

        self.isPlayer = player
        # Tomaatti 
        if self.isPlayer:


            self.tomaatti_path = os.path.join("assets", "tomaatti.png")
            self.splat_path = os.path.join("assets", "splat.png")

            self.tomaatti = pygame.image.load(self.tomaatti_path)
            self.splat = pygame.image.load(self.splat_path)

            self.tomaattiImage = pygame.transform.scale(self.tomaatti, (50, 50))
            self.splatImage = pygame.transform.scale(self.splat, (50, 50))

            self.tomaattiRect = self.tomaattiImage.get_rect()
            self.splatRect = self.splatImage.get_rect()

            self.tomaatti_in_motion = False
            self.tomaatti_speed = 0.5  # Slower speed

            self.splat_shown = False
            self.tomaatti_position = [0.0, 0.0]  # Use floating-point position

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()

    def center_on_screen(self, screen_width, screen_height):
        self.rect.center = (screen_width // 2, screen_height // 2)

    def random_location(self, screen_width, screen_height, min_x=None):
        max_x = screen_width - self.rect.width
        max_y = screen_height - self.rect.height

        minimum_x = min_x if min_x is not None else 0
        minimum_x = min(minimum_x, max_x)

        x_pos = random.randint(minimum_x, max_x)
        y_pos = random.randint(0, max_y)
        self.rect.topleft = (x_pos, y_pos)

        if self.isPlayer:
            self.tomaattiRect.topleft = (x_pos + 80, y_pos + 10)
            self.tomaatti_position = [float(x_pos + 80), float(y_pos + 10)]  # Initialize floating-point position

    def flip(self, horizontal=False, vertical=False):
        self.image = pygame.transform.flip(self.image, horizontal, vertical)
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


        if self.isPlayer:
            screen.blit(self.tomaattiImage, self.tomaattiRect.topleft)
            if self.splat_shown:
                screen.blit(self.splatImage, self.splatRect.topleft)


    def start_throw_tomato(self, target):
        """Initiates the tomato throw towards the target."""
        print("Tomaatti lentää")
        self.tomaatti_in_motion = True
        self.target = target
        self.splat_shown = False

    def update_tomato_position(self):
        """Updates the tomato's position if it's being thrown."""
        if self.tomaatti_in_motion:
            # Move the tomato towards the target
            target_x, target_y = self.target.rect.center
            current_x, current_y = self.tomaatti_position  # Use floating-point position
            
            direction_x = target_x - current_x
            direction_y = target_y - current_y
            
            # Normalize direction vector and move the tomato by its speed
            distance = (direction_x**2 + direction_y**2) ** 0.5
            if distance != 0:
                direction_x /= distance
                direction_y /= distance

            # Update tomato position (floating-point precision)
            self.tomaatti_position[0] += direction_x * self.tomaatti_speed
            self.tomaatti_position[1] += direction_y * self.tomaatti_speed

            # Update the rect with rounded integer position for drawing
            self.tomaattiRect.x = int(self.tomaatti_position[0])
            self.tomaattiRect.y = int(self.tomaatti_position[1])
            
            # Check for collision with the target
            if self.tomaattiRect.colliderect(self.target.rect):
                # Stop the tomato's motion
                self.tomaatti_in_motion = False
                self.splat_shown = True
                
                # Determine a random hit position within the top 40% of the target
                target_x, target_y = self.target.rect.topleft
                target_width, target_height = self.target.rect.size

                # Calculate the y-coordinate range for the top 40% of the target
                top_y = target_y
                bottom_y = target_y + int(target_height * 0.4)

                # Random hit position within the top 40% of the target
                hit_x = random.randint(target_x, target_x + target_width)
                hit_y = random.randint(top_y, bottom_y)
                
                # Set splash position to the random hit position
                self.splatRect.center = (hit_x, hit_y)
                
                # Reset tomato position next to the player after the splash
                self.tomaatti_position = [self.rect.x + 80, self.rect.y + 10]
                self.tomaattiRect.topleft = (int(self.tomaatti_position[0]), int(self.tomaatti_position[1]))


    def update(self, screen):
        """Update the image and tomato in the game loop."""
        self.draw(screen)
        self.update_tomato_position()