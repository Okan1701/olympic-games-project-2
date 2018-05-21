import sys

import pygame
import games.gewichtheffen.sprites as sprites
from games.gewichtheffen.modules import *
from classes.Image import Image
import classes.Asset as Asset
from games.diskShooting.classes.Button import Button
from games.gewichtheffen import colors
from classes.Color import Color

class Start():
    def __init__(self):
        print()

    def Start(self, screen):

        # screen
        widthscreen = 800
        heightscreen = 600
        gameDisplay = screen.gameDisplay
        # decorate game window
        pygame.display.set_caption('Olympische Spelen - Weightlifting')
        clock = pygame.time.Clock()
        crashed = False
        pygame.font.init()
        pygame.mixer.init()

        # count
        liftcounter = 0
        updatescore = False
        score_positiony = heightscreen - 30
        font = pygame.font.SysFont('Arial', 30)
        # lift
        startgame = False

        above_text = font.render('', False, (0, 0, 0))
        fail_text = font.render('U Failed...', False, (0, 0, 0))
        lift = 20
        time_goal = 10
        medallevel = 0
        backup = sprites.personstartrect

        def game_intro(screen):
            # Main screen text
            logo = Image(Asset.loadpath('gewichtheffen', 'img', 'logo.jpg'), [0, 0])
            background = Image(Asset.loadpath('gewichtheffen', 'img', 'homescherm.jpg'), [0, 75])
            # intructions = Image(Asset.loadpath('gewichtheffen', 'img', 'background_intro.png'), [150, 50])

            # Buttons
            start_btn = Button()
            quit_btn = Button()

            clock = pygame.time.Clock()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return 'quit'

                screen.gameDisplay.blit(background.image, background.rect)
                # screen.gameDisplay.blit(intructions.image, intructions.rect)
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

        while not crashed:
            clock.tick(30)

            print(startgame)
            while startgame == False:
                if (game_intro(screen) == 'game'):
                    startgame = True
                    start_ticks = pygame.time.get_ticks()
                else:
                    return 'start'
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        startgame = True
                        start_ticks = pygame.time.get_ticks()
                    if event.key == pygame.K_SPACE and startgame == True and gamepause == False:
                        liftcounter = liftcounter + 1
                        if score_positiony > 100:
                            score_positiony = score_positiony - 10
                            if liftcounter == (lift / 2):
                                sprites.personstartrect = sprites.personliftrect
                            if liftcounter == lift:
                                sprites.personstartrect = sprites.personliftedrect
                        else:
                            score_positiony = heightscreen - 30
                        print(liftcounter)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE and startgame == True and gamepause == False:
                        updatescore = True
                        # sprites.personstartrect = backup
            gameDisplay.blit(sprites.backgroundrect, (0, 0))
            gameDisplay.blit(sprites.personstartrect, (widthscreen // 2 - sprites.personstartrect.get_size()[0], 300))
            gameDisplay.blit(above_text, (10, 0))
            lifttext = str(lift) + ' lifts in ' + str(time_goal) + '. keep pressing SPACE to lift.'
            lift_text = font.render(lifttext, False, (0, 0, 0))
            gameDisplay.blit(lift_text, (230, 500))
            gamepause = False
            if startgame == True:
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
                above_text = font.render('Time: ' + str(int(seconds)), False, (0, 0, 0))
                gameDisplay.blit(above_text, (10, 0))
                if liftcounter >= lift:
                    liftcounter = 0
                    medallevel = medallevel + 1
                    time_goal = time_goal - 2
                    lift = lift + 20
                    score_positiony = heightscreen - 30
                    lift_text = font.render('Lift passed, be ready for the next!', False, (0, 0, 0))
                    gamepause = True
                    gameDisplay.blit(lift_text, (200, 100))
                    pygame.display.update()
                    sprites.personstartrect = backup
                    pygame.time.wait(2000)
                    start_ticks = pygame.time.get_ticks()
                elif seconds >= time_goal or medallevel >= 3:
                    return ['score', 'gewichtheffen', medallevel]
                if updatescore == True:
                    updatescore = False
                    score_text = font.render(str(liftcounter), False, (0, 0, 0))
                    gameDisplay.blit(score_text, (10, score_positiony))
            pygame.display.update()
        pygame.quit()
        quit()
