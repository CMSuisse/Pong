import pygame
from main import *

class GameController():
    @staticmethod
    def doUpdate():
        global current_ball,balls_remaining
        screen.fill((200,200,200)) #Start with a freshly filled in screen

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

        screen.blit(current_ball.image,current_ball.rect)
