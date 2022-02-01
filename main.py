from os import stat
import pygame
from ball import Ball
from platform_class import Platform

pygame.init()
screen = pygame.display.set_mode([640,640])
screen.fill((200,200,200))
pygame.display.set_caption("Pong")
Clock = pygame.time.Clock()

balls_remaining = 3
current_ball = pygame.sprite.Group()
current_ball.add(Ball())
platform = Platform()

#Add a point system that adds a point when the ball touches the top of the screen
#Make it viuslly obvious, how many points the player has and also how many balls it has left
#Trail renderer for the path the ball took. It should slowly grow smaller and dimmer.
#The ball should speed up as the game progresses


class GameController():
    @staticmethod
    def doUpdate() -> None:
        screen.fill((200,200,200)) #Start with a freshly filled in screen
        GameController.__ballUpdate()
        GameController.__platformUpdate()
        GameController.__doCollisonLogic()

        current_ball.draw(screen)
        screen.blit(platform.image,platform.rect)

    @staticmethod
    def __ballUpdate() -> None:
        global current_ball,balls_remaining
        for ball in current_ball:
            if ball.isAlive:
                ball.move()
            else:
                pygame.sprite.Sprite.kill(ball)
                if balls_remaining > 0: #Has the player balls left?
                    current_ball.add(Ball()) #If yes, spawn a new one
                    balls_remaining -= 1
                else: #If no, it's game over
                    pass
                    #Game Over goes here

    @staticmethod
    def __platformUpdate() -> None:
        global platform
        platform.move(GameController.__getMouseX())

    @staticmethod
    def __getMouseX() -> int:
        if pygame.mouse.get_focused():
            return pygame.mouse.get_pos()[0] #If the mouse is inside the window -> return the x-position of the mouse

    @staticmethod
    def __doCollisonLogic() -> None:
        global current_ball, platform

        if pygame.sprite.spritecollideany(platform,current_ball):
            for ball in current_ball:
                ball.speed[1] = -ball.speed[1]


active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    Clock.tick(60)
    GameController.doUpdate()
    pygame.display.flip()

pygame.quit()