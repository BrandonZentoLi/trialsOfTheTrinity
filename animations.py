import pygame, sys


class BookOfInsights(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.flip_animation = True
        self.sprites = []
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_1.png'))
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_2.png'))
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_3.png'))
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_4.png'))
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_5.png'))
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_6.png'))
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_7.png'))
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_8.png'))
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_9.png'))
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_10.png'))
        self.sprites.append(pygame.image.load('animations/book_of_insights/book_11.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def flip_pages(self):
        self.flip_animation = True

    def update(self, speed):
        if self.flip_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.flip_animation = False

        self.image = self.sprites[int(self.current_sprite)]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")



