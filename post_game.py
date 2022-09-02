import pygame
pygame.font.init()

font = pygame.font.Font(pygame.font.get_default_font(), 50)
def game_over(points, screen, new_highscore): #Displaying total points on the screen

    screen.fill((200,200,200))
    text1 = font.render("Congrats! You made",False,(0,0,0))
    text2 = font.render(str(points),False,(0,0,0))
    text3 = font.render("Points",False,(0,0,0))
    text4 = font.render("New Highscore!", False, (0, 0, 0))

    screen.blit(text1,((640-font.size("Congrats! You made")[0])/2,(480-font.size("Congrats! You made")[1])/2)) #font.size gives back the size of the font. Used for centering text
    screen.blit(text2,((font.size("Congrats! You made:")[0]+100 - font.size(str(points))[0])/2,(480-font.size("Congrats! You made:")[1])/2+50))
    screen.blit(text3,((font.size("Congrats! You made:")[0]+100 - font.size("Points")[0])/2,(480-font.size("Congrats! You made:")[1])/2+100))
    if new_highscore:
        screen.blit(text4, (200, 400))

def handle_highscore(points_achieved):
    with open("highscore.txt", "r") as highscore_file:
        highscore = int(highscore_file.read())
    highscore_file.close()

    if highscore < points_achieved:
        with open("highscore.txt", "w") as highscore_file:
            highscore_file.write(str(points_achieved))
    
        highscore_file.close() 
        return True, True #Highscore updated successfully and new highscore has been achieved
    return True, False #Highscore check complete but no new highscore