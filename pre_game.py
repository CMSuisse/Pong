import pygame
from button_class import Button

def render_menu(screen, buttons):
    return_value = False
    for button in buttons:
        screen.fill([200, 200, 200])
        screen.blit(button.image, button.rect)
        button.check_for_press()
        pygame.display.flip()
        
        if button.button_name == "start_button" and button.pressed:
            return_value = True
    
    return return_value