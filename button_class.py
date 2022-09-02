import pygame
pygame.init()
pygame.font.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, x_length, y_length, button_color, button_text, button_name):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([x_length, y_length])
        self.image.fill(button_color)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x_pos, y_pos
        self.button_name = button_name
        self.pressed = False

        button_text_rect = button_text.get_rect()
        button_text_rect.centerx, button_text_rect.centery = x_length/2, y_length/2

        self.image.blit(button_text, button_text_rect) #Text should be centered...
    
    def check_for_press(self):
        if pygame.mouse.get_pressed()[0]: #Look for the status of the left mouse button
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] > self.rect.left and mouse_pos[0] < self.rect.right: #Is the mouse within the x dimension of the button?
                if mouse_pos[1] > self.rect.top and mouse_pos[1] < self.rect.bottom: #Is the mosue within the y dimension of the button?
                    self.pressed = True