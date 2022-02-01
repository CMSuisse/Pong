import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([50,10])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

        self.rect.left, self.rect.top = 300,500

    def move(self, target: int) -> None:
        if not self.rect.centerx == target and not target == None:
            if self.rect.centerx < target:
                self.rect = self.rect.move((5,0)) #Move towards the player's cursor
            else:
                self.rect = self.rect.move((-5,0))