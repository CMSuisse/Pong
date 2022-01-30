import pygame
from ball import Ball
from GameController import GameController

pygame.init()
screen = pygame.display.set_mode([640,640])
screen.fill((200,200,200))
Clock = pygame.time.Clock()

balls_remaining = 3
current_ball = Ball()

#Add a new pygame.sprite.Sprite class: platform
#Give it the ability to follow a player's cursor's x-positon
#It shouldn't be able to just jump to the cursor. It should move quite slowly
#Add a point system that adds a point when the ball touches the top of the screen
#Make it viuslly obvious, how many points the player has and also how many balls it has left

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    Clock.tick(60)
    GameController.doUpdate()
    pygame.display.flip()

pygame.quit()