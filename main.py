import pygame

pygame.init()
screen = pygame.display.set_mode([640,640])
screen.fill([200,200,200])

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    pygame.display.flip()

pygame.quit()