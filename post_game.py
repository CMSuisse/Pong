from operator import indexOf
import pygame
pygame.font.init()

def game_over(screen, new_highscore, text_elements, text_elements_rects):

    screen.fill((200,200,200))

    for text_element, text_element_rect in zip(text_elements, text_elements_rects):
        if indexOf(text_elements, text_element) < 3:
            screen.blit(text_element, text_element_rect)
            continue
        if new_highscore:
            #Add the New Highscore text element to the screen
            screen.blit(text_element, text_element_rect)

def handle_highscore(points_achieved):
    with open("highscore.txt", "r") as highscore_file:
        highscore = int(highscore_file.read())
    highscore_file.close()

    if highscore < points_achieved:
        with open("highscore.txt", "w") as highscore_file:
            highscore_file.write(str(points_achieved))
    
        highscore_file.close() 
        #Highscore updated successfully and new highscore has been achieved
        return True, True
    #Highscore check complete but no new highscore
    return True, False