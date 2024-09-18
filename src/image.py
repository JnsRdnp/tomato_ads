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
            self.tomaatti_speed = 0.8

            self.splat_shown = False
            self.tomaatti_position = [0.0, 0.0]
            self.score = 0

            self.font = pygame.font.SysFont(None, 36)

            self.splatsound = pygame.mixer.Sound(os.path.join("assets", "splatsound.wav"))

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
            self.tomaatti_position = [float(x_pos + 80), float(y_pos + 10)]

    def flip(self, horizontal=False, vertical=False):
        self.image = pygame.transform.flip(self.image, horizontal, vertical)
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        if self.isPlayer:
            screen.blit(self.tomaattiImage, self.tomaattiRect.topleft)
            if self.splat_shown:
                screen.blit(self.splatImage, self.splatRect.topleft)
            
            if self.score > 2:
                score_text = self.font.render("Voittaja!", True, (255, 255, 255))
            else:
                score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            screen.blit(score_text, (self.rect.x, self.rect.y + self.rect.height + 10))

    def start_throw_tomato(self, target):
        print("Tomaatti lentää")
        self.tomaatti_in_motion = True
        self.target = target
        self.splat_shown = False

    def update_tomato_position(self):
        if self.tomaatti_in_motion:
            target_x, target_y = self.target.rect.center
            current_x, current_y = self.tomaatti_position
            
            direction_x = target_x - current_x
            direction_y = target_y - current_y
            
            distance = (direction_x**2 + direction_y**2) ** 0.5
            if distance != 0:
                direction_x /= distance
                direction_y /= distance

            self.tomaatti_position[0] += direction_x * self.tomaatti_speed
            self.tomaatti_position[1] += direction_y * self.tomaatti_speed

            self.tomaattiRect.x = int(self.tomaatti_position[0])
            self.tomaattiRect.y = int(self.tomaatti_position[1])
            
            if self.tomaattiRect.colliderect(self.target.rect):
                self.tomaatti_in_motion = False
                self.splat_shown = True
                self.splatsound.play()
                
                target_x, target_y = self.target.rect.topleft
                target_width, target_height = self.target.rect.size

                top_y = target_y
                bottom_y = target_y + int(target_height * 0.55)

                hit_x = random.randint(target_x, target_x + target_width)
                hit_y = random.randint(top_y, bottom_y)
                
                self.splatRect.center = (hit_x, hit_y)
                
                hit_probability = 0.40

                print('Osuman mahdollisuus: ', hit_probability)
                if random.random() < hit_probability:
                    self.score += 1

                self.tomaatti_position = [self.rect.x + 80, self.rect.y + 10]
                self.tomaattiRect.topleft = (int(self.tomaatti_position[0]), int(self.tomaatti_position[1]))

    def update(self, screen):
        self.draw(screen)
        self.update_tomato_position()
