import pygame
pygame.font.init()

font = pygame.font.Font(pygame.font.get_default_font(),50)
def game_over(points,screen):

    screen.fill((200,200,200))
    text1 = font.render("Congrats! You made",False,(0,0,0))
    text2 = font.render(str(points),False,(0,0,0))
    text3 = font.render("Points",False,(0,0,0))

    screen.blit(text1,((640-font.size("Congrats! You made")[0])/2,(480-font.size("Congrats! You made")[1])/2))
    screen.blit(text2,((font.size("Congrats! You made:")[0]+100 - font.size(str(points))[0])/2,(480-font.size("Congrats! You made:")[1])/2+50))
    screen.blit(text3,((font.size("Congrats! You made:")[0]+100 - font.size("Points")[0])/2,(480-font.size("Congrats! You made:")[1])/2+100))