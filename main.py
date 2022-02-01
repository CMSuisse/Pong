from os import stat
import pygame
from ball import Ball
from platform import Platform

pygame.init()
screen = pygame.display.set_mode([640,640])
screen.fill((200,200,200))
Clock = pygame.time.Clock()

balls_remaining = 3
current_ball = Ball()
platform = Platform()

#Add a new pygame.sprite.Sprite class: platform
#Give it the ability to follow a player's cursor's x-positon
#It shouldn't be able to just jump to the cursor. It should move quite slowly
#Add a point system that adds a point when the ball touches the top of the screen
#Make it viuslly obvious, how many points the player has and also how many balls it has left


class GameController():
    @staticmethod
    def __ballUpdate() -> None:
        global current_ball,balls_remaining
        if current_ball.isAlive:
            current_ball.move()
        else:
            pygame.sprite.Sprite.kill(current_ball)
            if balls_remaining > 0: #Has the player balls left?
                current_ball = Ball() #If yes, spawn a new one
                balls_remaining -= 1
            else: #If no, it's game over
                pass
                #Game Over goes here

    @staticmethod
    def doUpdate() -> None:
        screen.fill((200,200,200)) #Start with a freshly filled in screen
        GameController.__ballUpdate()

        screen.blit(current_ball.image,current_ball.rect)


    @staticmethod
    def getMouseX() -> int:
        if pygame.mouse.get_focused():
            return pygame.mouse.get_pos()[0] #If the mouse is inside the window -> return the x-position of the mouse

GameController.__ballUpdate()

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    Clock.tick(60)
    GameController.doUpdate()
    print(GameController.getMouseX())
    pygame.display.flip()

pygame.quit()