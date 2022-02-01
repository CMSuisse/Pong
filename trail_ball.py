import pygame

class TrailBall(pygame.sprite.Sprite):
    def __init__(self,origin_pos, step):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill((200,200,200))
        self.image.set_colorkey((200,200,200))
        pygame.draw.circle(self.image, (200,200,2*step),(25,25),20-0.2*step) #Doin some easy math to draw the circle based on how far away from the ball it is

        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = origin_pos[0], origin_pos[1]
        self.step = step
        self.origin_pos = origin_pos