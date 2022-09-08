import pygame
import webbrowser
from class_definitions import *
from post_game import *

#Initializes both the font renderer and the mixer
pygame.init()
screen_size = [640, 640]
screen = pygame.display.set_mode(screen_size)
screen.fill((200, 200, 200))
pygame.display.set_caption("Pong")
Clock = pygame.time.Clock()

#Initializes sound files for later use
Background = pygame.mixer.Sound("Sounds/Background.ogg")
Background.set_volume(0.2)
PointGained = pygame.mixer.Sound("Sounds/PointGained.wav")
PointGained.set_volume(0.7)
NewBall = pygame.mixer.Sound("Sounds/NewBall.wav")
NewBall.set_volume(1)
YouLost = pygame.mixer.Sound("Sounds/YouLost.wav")
YouLost.set_volume(1)

#Initializes buttons for use in menu scen
button_font = pygame.font.Font(pygame.font.get_default_font(), 20)

button_text_elements = [button_font.render("START", False, (0, 0, 0)),
                    button_font.render("CODE", False, (0, 0, 0)),
                    button_font.render("QUIT", False, (0, 0, 0)),
                    #Here are the buttons for the game over screen,
                    button_font.render("MENU", False, (0, 0, 0))]
                    
button_coordinates = [(screen_size[0]/2, screen_size[1]/2 - 70),
                    (screen_size[0]/2, screen_size[1]/2),
                    (screen_size[0]/2, screen_size[1]/2 + 70),
                    #Here are the buttons for the game over screen
                    (screen_size[0]/2, screen_size[1]/2 + 200)]

button_names = ["start_button", 
            "to_repos_button", 
            "quit_button",
            "to_menu_button"]

buttons = []
for i in range(len(button_text_elements)):
    buttons.append(Button(button_coordinates[i], (200, 50), (0, 255, 0), button_text_elements[i], button_names[i]))

start_menu_buttons = buttons[:3]
end_menu_buttons = buttons[3:]

#Initializes text objects for game over screen
game_over_font = pygame.font.Font(pygame.font.get_default_font(), 50)
text_elements = [game_over_font.render("Congrats! You made", False ,(0, 0, 0)),
                game_over_font.render("Points", False, (0, 0, 0)),
                game_over_font.render("New Highscore!", False, (0, 0, 0))]

font = pygame.font.Font(pygame.font.get_default_font(), 30)

class GameController():
    @staticmethod
    def initialize_new_game():
        global is_game_over, highscore_updated, points, balls_remaining, current_ball, trail, platform, game_started, text_elements, text_elements_rects
        #Initializes other variables and constants
        balls_remaining = 1
        points = 0
        is_game_over = False
        highscore_updated = False
        game_started = False
        trail = pygame.sprite.Group()
        current_ball = Ball()
        platform = Platform()
        #Deletes the old points text element from the list if there is one
        if len(text_elements) == 4:
            del text_elements[1]
        #Rects are calculated after the points text element has been added to the list
        text_elements_rects = []
        #Special value -1 will loop the sound indefinitely
        Background.play(-1)

    @staticmethod
    def add_points_to_text_array():
        points_text_element = game_over_font.render(str(points), False, (0, 0, 0))
        text_elements.insert(1, points_text_element)
        return text_elements

    @staticmethod
    def calculate_text_elements_rects():
        text_elements_rects = []
        for text_element in text_elements:
            text_elements_rects.append(text_element.get_rect())

        for i, text_element_rect in enumerate(text_elements_rects):
            text_element_rect.centerx, text_element_rect.centery = screen_size[0]/2, screen_size[1]/2 - 50 + 50*i
        
        return text_elements_rects
        
    @staticmethod
    def do_menu_scene(screen, start_menu_buttons):
        global active
        should_game_start = False

        screen.fill([200, 200, 200])
        for button in start_menu_buttons:
            #Add every button to the screen
            screen.blit(button.image, button.rect)
            #Check every button if it has been pressed
            button.check_for_press()
            #Display the new screen
            
            if button.pressed and pygame.mouse.get_focused():
                if button.button_name == "start_button":
                    should_game_start = True
                elif button.button_name == "to_repos_button":
                    #Open the github repository for this project
                    webbrowser.open("https://github.com/CMSuisse/Pong")
                    pygame.time.delay(100)
                elif button.button_name == "quit_button":
                    active = False
                #Trust me, you do not want a new chrome tab every frame
                button.pressed = False

        return should_game_start

    @staticmethod
    def doUpdate():
        global points, platform, trail

        #Start with a freshly filled in screen each frame
        screen.fill((200, 200, 200))
        #Update the ball, then the trail, then the platform
        GameController.__ballUpdate()
        #No need to check for everything else when the player's dead
        if balls_remaining > 0:
            trail = GameController.__updateTrail()
            platform = GameController.__platformUpdate()
            #After everything has been moved to their new position check for collisions
            GameController.__doCollisonLogic()
        else:
            return

        #Render the text in the top left center of the screen
        output_text = font.render("Points: {} Lives: {}".format(str(points), str(balls_remaining)), False, (0, 0, 0))

        trail.draw(screen)
        screen.blit(current_ball.image, current_ball.rect)
        screen.blit(platform.image, platform.rect)
        screen.blit(output_text, (10, 10))

    @staticmethod
    def __ballUpdate():
        global current_ball, balls_remaining, points, is_game_over

        if current_ball.isAlive:
            #Ball.move() function return True when the ball hits the top of the screen
            if current_ball.move():
                PointGained.play()
                points += 1
            current_ball.framesAlive += 1
        else:
            del(current_ball)
            balls_remaining -= 1
            #If the player still has balls left after loosing one, spawn one in
            if balls_remaining > 0:
                NewBall.play()
                current_ball = Ball()
            #Otherwise, end the game
            else:
                Background.stop()
                YouLost.play()
                is_game_over = True

    @staticmethod
    def __updateTrail():
        trail.add(TrailBall((current_ball.rect.left, current_ball.rect.top), 1))

        for trailBall in trail:
            oldPos, oldStep = trailBall.origin_pos, trailBall.step
            trailBall.kill()
            #If the new ball would have size zero, don't draw that ball
            if oldStep < 100:
                trail.add(TrailBall(oldPos, oldStep + 1))

        return trail

    @staticmethod
    def __platformUpdate():
        platform.move(GameController.__getMouseX())
        return platform

    @staticmethod
    def __getMouseX():
        #Return x position of the mouse
        return pygame.mouse.get_pos()[0]

    @staticmethod
    def __doCollisonLogic():
        global current_ball, platform

        #Check for a collision between the platform and the current ball
        if pygame.sprite.collide_rect(platform, current_ball):
            #If collision occured, reverse both the x and y directions of the ball
            current_ball.speed[1] = -current_ball.speed[1]

GameController.initialize_new_game()
active = True
while active:
    for event in pygame.event.get():
        #Checks, whether the x button on the screen has been pressed
        if event.type == pygame.QUIT:
            active = False
    #Run the game at 60 fps
    Clock.tick(60)

    #Check if the game has started
    #False -> Display the menu
    #True -> Check if it's game over for the player
    #False -> Do a game tick
    #True -> Check if the program has checked, if the amount of points achieved are a new highscore
    #False -> Update the highscore and while you're at it, complete some other one time processes
    #True -> Check, if player wants to return to menu
    #False -> Continue checking
    #True -> Set game_started to False. Begin anew with the loop
    if not game_started:
        game_started = GameController.do_menu_scene(screen, start_menu_buttons)
    else:
        if not is_game_over:
            GameController.doUpdate()
        else:
            if not highscore_updated:
                highscore_updated, new_highscore = handle_highscore(points)
                #Because this part of the code will only run once, a few other things that only need
                #to run once are also here
                trail.remove()
                text_elements =  GameController.add_points_to_text_array()
                text_elements_rects = GameController.calculate_text_elements_rects()

            game_started = game_over(screen, new_highscore, text_elements, text_elements_rects, end_menu_buttons)
            #Here the initialize_new_game function gets called less frequently than in line 223
            if not game_started:
                GameController.initialize_new_game()
    #Display the new screen after each frame has been processed
    pygame.display.flip()

pygame.quit()