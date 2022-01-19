import pygame
from pygame import mixer

mixer.init()
click_channel = mixer.Channel(1)
click_sound = mixer.Sound('music/click.mp3')
click_sound.set_volume(0.4)


class Button:
    def __init__(self, text, width, height, pos, elevation, window, font, page_id, update_page_id, callback=None):
        # core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.window = window
        self.font = font
        self.page_id = page_id
        self.update_page_id = update_page_id
        self.callback = callback

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'

        # text
        self.text_surf = self.font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.window, self.bottom_color,
                         self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.window, self.top_color,
                         self.top_rect, border_radius=12)
        self.window.blit(self.text_surf, self.text_rect)

        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#648db5'

            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True

                click_channel.play(click_sound)

            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    self.pressed = False

                    if self.page_id is not None:
                        self.update_page_id(self.page_id)
                    if self.callback is not None:
                        self.callback()
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'


class ItemButton:
    def __init__(self, image, width, height, pos, elevation, window, callback=None):
        # core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.window = window
        self.callback = callback

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'

        # text
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.image_rect = self.image.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.image_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.window, self.bottom_color,
                         self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.window, self.top_color,
                         self.top_rect, border_radius=12)
        self.window.blit(self.image, self.image_rect)

        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#648db5'

            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True

                click_channel.play(click_sound)

            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    self.pressed = False

                    if self.callback is not None:
                        self.callback()
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#57728c'
