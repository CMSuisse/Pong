import pygame
from operator import indexOf
pygame.font.init()

def game_over(screen, new_highscore, text_elements, text_elements_rects, buttons):
    screen.fill((200,200,200))

    for text_element, text_element_rect in zip(text_elements, text_elements_rects):
        if indexOf(text_elements, text_element) < 3:
            screen.blit(text_element, text_element_rect)
            continue
        if new_highscore:
            #Add the New Highscore text element to the screen
            screen.blit(text_element, text_element_rect)
    
    for button in buttons:
        screen.blit(button.image, button.rect)

    game_started = check_for_button_press(buttons)
    return game_started

def check_for_button_press(buttons):
    for button in buttons:
        button.check_for_press()
        if button.pressed:
            #If the to_menu_button gets pressed, game_started will be set to False, reverting the game back to the menu screen
            if button.button_name == "to_menu_button":
                button.pressed = False
                return False
        else:
            return True

def handle_highscore(points_achieved):
    #Briefly open the highscore file and store the value temporarily
    with open("highscore.txt", "r") as highscore_file:
        highscore = int(highscore_file.read())
    highscore_file.close()

    #If the current value in the txt file is less than the amount of points the player achieved
    #write the new highscore into the file
    if highscore < points_achieved:
        with open("highscore.txt", "w") as highscore_file:
            highscore_file.write(str(points_achieved))
    
        highscore_file.close() 
        #Highscore updated successfully and new highscore has been achieved
        return True, True
    #Highscore check complete but no new highscore
    return True, False