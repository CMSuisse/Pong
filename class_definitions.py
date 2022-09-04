from pygame import sprite, font, mouse, draw, Surface
font.init()

class Ball(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)

        #Creates a square with sidelengths 50 to be drawn onto the screen
        self.image = Surface((50, 50))
        self.image.fill((200, 200, 200))
        #Makes the square itself transparent. Done to avoid clipping issues with trail
        self.image.set_colorkey((200, 200, 200))
        #Draws a yellow circle onto that square
        draw.circle(self.image, (220, 220, 0), (25, 25), 25, 0)
        self.rect = self.image.get_rect()

        self.rect.left,self.rect.top = 300, 50
        self.speed = [2, 2]
        self.isAlive = True

        self.framesAlive = 0

    def move(self):
        self.rect = self.rect.move(self.speed)

        #Speeds up the ball every 1000 frames in the x and y direction
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
            return True
        
        #Very funny. Refactoring me still thinks this is very funny.
        if self.rect.bottom >= 690:
            self.isAlive = False

class Platform(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)

        #Creates a black surface
        self.image = Surface([100, 30])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.left, self.rect.top = 300, 550

    def move(self, target):
        #Target means the player's cursor's x position
        #Don't let the platform move outside the screen
        if self.rect.left < 0:
            self.rect.left = 0
            return
        #Don't let the platform move outside the screen
        elif self.rect.right > 640:
            self.rect.right = 640
            return

        #The +- 10 is there to not make the platform react too sensitively to tiny cursor movements
        if self.rect.centerx < target - 10 or self.rect.centerx > target + 10:
            #Move towards the player's cursor
            if self.rect.centerx < target:
                self.rect = self.rect.move((2, 0))
            else:
                self.rect = self.rect.move((-2, 0))

class TrailBall(sprite.Sprite):
    def __init__(self,origin_pos, step):
        sprite.Sprite.__init__(self)

        #Trail balls get spawned at the position of a trail ball in the previous frame
        #There are 100 balls in the trail, with the ball with index 0 having the size and transparency
        #Of the real trail ball and the ball with index 99 in the sprite group being almost invisible

        self.image = Surface((50, 50))
        self.image.fill((200, 200, 200))
        #Colorkeying to avoid clipping with other trail balls
        self.image.set_colorkey((200, 200, 200))
        #Determining what size the ball should have depending on it's distance away from the original ball
        draw.circle(self.image, (200, 200, 2*step), (25, 25), 20 - 0.2*step)

        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = origin_pos[0], origin_pos[1]
        self.step = step
        self.origin_pos = origin_pos

class Button(sprite.Sprite):
    def __init__(self, button_pos, button_length, button_color, button_text, button_name):
        sprite.Sprite.__init__(self)

        self.image = Surface(button_length)
        self.image.fill(button_color)
        self.rect = self.image.get_rect()
        #Making the centerx and centery coordinates correspond to the inputed coordinates is more intuitive
        self.rect.centerx, self.rect.centery = button_pos
        self.button_name = button_name
        self.pressed = False

        button_text_rect = button_text.get_rect()
        #Centering the button text inside the button
        button_text_rect.centerx, button_text_rect.centery = button_length[0]/2, button_length[1]/2

        self.image.blit(button_text, button_text_rect)
    
    def check_for_press(self):
        #Is LMB pressed
        if mouse.get_pressed()[0]:
            mouse_pos = mouse.get_pos()
            #Is the mouse within the x dimension of the button?
            if mouse_pos[0] > self.rect.left and mouse_pos[0] < self.rect.right:
                #Is the mosue within the y dimension of the button?
                if mouse_pos[1] > self.rect.top and mouse_pos[1] < self.rect.bottom:
                    self.pressed = True