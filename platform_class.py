import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([100,30])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

        self.rect.left, self.rect.top = 300,550

    def move(self, target: int) -> None:
        if target == None:
            return

        if self.rect.left < 0: #Don't let the platform move outside the screen
            self.rect.left = 0
            return
        elif self.rect.right > 640: #Dito
            self.rect.right = 640
            return

        if self.rect.centerx < target-10 or self.rect.centerx > target+10:
            if self.rect.centerx < target:
                self.rect = self.rect.move((2,0)) #Move towards the player's cursor
            else:
                self.rect = self.rect.move((-2,0))