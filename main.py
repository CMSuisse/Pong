import pygame
from ball import Ball
from platform_class import Platform
from trail_ball import TrailBall
from game_over import game_over #That isn't confusing at all

pygame.init() #Initializes both the font renderer and the mixer
screen = pygame.display.set_mode([640,640])
screen.fill((200,200,200))
pygame.display.set_caption("Pong")
Clock = pygame.time.Clock()

#Initializing sound files for later use
Background = pygame.mixer.Sound("Sounds/Background.ogg")
Background.set_volume(0.2)
PointGained = pygame.mixer.Sound("Sounds/PointGained.wav")
PointGained.set_volume(0.7)
NewBall = pygame.mixer.Sound("Sounds/NewBall.wav")
NewBall.set_volume(1)
YouLost = pygame.mixer.Sound("Sounds/YouLost.wav")
YouLost.set_volume(1)

balls_remaining = 3
points = 0
isGameOver = False
current_ball = pygame.sprite.Group()
trail = pygame.sprite.Group()
current_ball.add(Ball())
platform = Platform()
font = pygame.font.Font(pygame.font.get_default_font(),30)

class GameController():
    @staticmethod
    def doUpdate():
        global points

        screen.fill((200,200,200)) #Start with a freshly filled in screen
        GameController.__ballUpdate()
        GameController.updateTrail()
        GameController.__platformUpdate()
        GameController.__doCollisonLogic()

        output_text = font.render("Points: " + str(points) + "      " + "Lives: " + str(balls_remaining),False,(0,0,0))

        trail.draw(screen)
        current_ball.draw(screen)
        screen.blit(platform.image,platform.rect)
        screen.blit(output_text,(10,10))

    @staticmethod
    def __ballUpdate():
        global current_ball,balls_remaining,points,isGameOver
        for ball in current_ball:
            if ball.isAlive:
                if ball.move() == 1: #The function will return 1 when the ball hits the ceiling
                    PointGained.play()
                    points += 1
                ball.framesAlive += 1
            else:
                pygame.sprite.Sprite.kill(ball)
                balls_remaining -= 1
                if balls_remaining > 0: #Has the player balls left?
                    NewBall.play()
                    current_ball.add(Ball()) #If yes, spawn a new one
                else: #If no, it's game over
                    Background.stop()
                    YouLost.play()
                    isGameOver = True

    @staticmethod
    def updateTrail():
        global current_ball,trail
        for ball in current_ball:
            trail.add(TrailBall((ball.rect.left,ball.rect.top),1))

        for trailBall in trail:
            oldPos,oldStep = trailBall.origin_pos,trailBall.step
            trailBall.kill()
            if oldStep < 100:
                trail.add(TrailBall(oldPos,oldStep + 1))

    @staticmethod
    def __platformUpdate():
        global platform
        platform.move(GameController.__getMouseX())

    @staticmethod
    def __getMouseX():
        if pygame.mouse.get_focused():
            return pygame.mouse.get_pos()[0] #If the mouse is inside the window -> return the x-position of the mouse

    @staticmethod
    def __doCollisonLogic():
        global current_ball, platform

        if pygame.sprite.spritecollideany(platform,current_ball):
            for ball in current_ball:
                ball.speed[1] = -ball.speed[1]


Background.play(-1) #Special value -1 will loop the sound indefinitely
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    Clock.tick(60)
    if not isGameOver:
        GameController.doUpdate()
    else:
        game_over(points,screen)
        GameController.updateTrail()
        trail.draw(screen)
    pygame.display.flip()

pygame.quit()