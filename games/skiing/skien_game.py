import pygame
import time
import random
from classes.Image import Image
import classes.Asset as Asset
from games.diskShooting.classes.Button import Button
from classes.Color import Color

class Start():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.state = 'intro'
        # decorate game window
        pygame.display.set_caption('Olympische Spelen - Skiing')

    def Start(self, screen):

        display_width = 800
        display_height = 600

        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (200, 0, 0)
        green = (0, 200, 0)
        bright_red = (255, 0, 0)
        bright_green = (0, 255, 0)

        skier_width = 73

        skierPng = pygame.image.load(Asset.loadpath('skiing', 'img', 'skier3.png'))
        BackgroundIntro = pygame.image.load(Asset.loadpath('skiing', 'img', 'background_intro.png'))
        gamebackground = pygame.image.load(Asset.loadpath('skiing', 'img', 'gamebackground.png'))
        BoomPng = pygame.image.load(Asset.loadpath('skiing', 'img', 'boom.png'))

        # crash = True

        # Bomen ontwijken en score optellen
        def poortje_dodged(screen, count):
            font = pygame.font.SysFont(None, 25)
            text = font.render("Dodged: " + str(count), True, black)
            screen, screen.gameDisplay.blit(text, (100, 0))

        # Boom image
        def poortje(screen, poortjex, poortjey, poortjew, poortjeh, color):
            screen.gameDisplay.blit(BoomPng, (poortjex, poortjey, poortjew, poortjeh))

        # skier image
        def skier(screen, x, y):
            screen.gameDisplay.blit(skierPng, (x, y))

        # background image
        def background(screen, x, y):
            screen.gameDisplay.blit(gamebackground, (0, 0))

        def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()

        def game_loop(screen):

            x = (display_width * 0.45)
            y = (display_height * 0)

            x_change = 0

            poortje_startx = random.randrange(100, display_width - 100)
            poortje_starty = 600
            poortje_speed = 6
            poortje_width = 110
            poortje_height = 98

            dodged = 0

            gameExit = False

            clock = pygame.time.Clock()

            while not gameExit:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x_change = -5
                        elif event.key == pygame.K_RIGHT:
                            x_change = 5

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            x_change = 0

                x += x_change
                screen.gameDisplay.fill(white)

                # poortje(poortjex, poortjey, poortjew, poortjeh, color)
                background(screen, x, y)
                poortje(screen, poortje_startx, poortje_starty, poortje_width, poortje_height, black)
                poortje_starty -= poortje_speed
                skier(screen, x, y)
                poortje_dodged(screen, dodged)

                if x > display_width - skier_width or x < 0:
                    return ['end', dodged]

                if poortje_starty < -300:
                    poortje_starty = 600 + poortje_height
                    poortje_startx = random.randrange(100, display_width - 200)
                    dodged += 1
                    poortje_speed += 0.75

                # wanneer je tegen poortje aan crasht
                if y < poortje_starty + poortje_height and y > poortje_starty:

                    if x > poortje_startx and x < poortje_startx + poortje_width or x + skier_width > poortje_startx and x + skier_width < poortje_startx + poortje_width:
                        return ['end', dodged]

                pygame.display.update()
                clock.tick(50)

        def game_intro(screen):
            # Main screen text
            logo = Image(Asset.loadpath('skiing', 'img', 'logo.jpg'), [0, 0])
            background = Image(Asset.loadpath('skiing', 'img', 'background.jpg'), [0, 0])
            intructions = Image(Asset.loadpath('skiing', 'img', 'background_intro.png'), [150, 50])

            # Buttons
            start_btn = Button()
            quit_btn = Button()

            clock = pygame.time.Clock()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return 'quit'

                screen.gameDisplay.blit(background.image, background.rect)
                screen.gameDisplay.blit(intructions.image, intructions.rect)
                screen.gameDisplay.blit(logo.image, logo.rect)

                check_start = start_btn.setButton("Start", 150, 450, 100, 50, Color.GREEN.getRGB(),
                                                  Color.DARK_GREEN.getRGB(),
                                                  screen, 'game')
                check_end = quit_btn.setButton("Return", 550, 450, 100, 50, Color.RED.getRGB(), Color.DARK_RED.getRGB(),
                                               screen,
                                               'return')

                # Return results of button clicked
                if check_start != None:
                    return 'game'
                elif check_end != None:
                    return 'return'
                else:
                    pygame.display.update()
                    clock.tick(15)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                    break
            if self.state == 'intro':
                result = game_intro(screen)
                if result == None:
                    break
                else:
                    self.state = result
            elif self.state == 'game':
                result = game_loop(screen)
                print(result)
                if result == None:
                    break
                else:
                    self.state = result[0]
            elif self.state == 'end':
                self.state = 'intro'
                return ['score', 'skiing', result[1]]
            elif self.state == 'quit':
                pygame.display.quit()
                pygame.quit()
            elif self.state == 'return':
                return 'start'

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()
