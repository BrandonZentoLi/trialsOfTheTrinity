import pygame

class InputBox:
    def __init__(self, x, y, width, height, font, window, text, update_text, index):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text        
        self.color = '#354B5E'
        self.font = font       
        self.window = window
        self.active = False
        self.update_text = update_text
        self.index = index


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.update_text(self.index, self.text)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                
              
    
    def draw_textbox(self):
        pygame.draw.rect(self.window, self.color, self.rect, 2)
        font_surface = self.font.render(self.text, True, self.color)
        self.window.blit(font_surface, (self.rect.x, self.rect.y))
