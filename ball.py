import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50,50))
        self.image.fill((200,200,200))
        self.image.set_colorkey((200,200,200))
        pygame.draw.circle(self.image,(220,220,0),(25,25),25,0)
        self.rect = self.image.get_rect()

        self.rect.left,self.rect.top = 25,100
        self.speed = [2,2]
        self.isAlive = True

        self.framesAlive = 0

    def move(self) -> None or int:
        self.rect = self.rect.move(self.speed)

        if self.framesAlive % 1000 == 0 and self.framesAlive != 0:
            if self.speed[0] == abs(self.speed[0]):
                self.speed[0] += 1
            else:
                self.speed[0] -= 1
            if self.speed[1] == abs(self.speed[1]):
                self.speed[1] += 1
            else:
                self.speed[1] -= 1

        if self.rect.left <= 0 or self.rect.right >= 640:
            self.speed[0] = -self.speed[0]
        elif self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            return 1
        
        if self.rect.bottom >= 690: #Very funny
            self.isAlive = False