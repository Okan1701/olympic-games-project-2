import pygame
import time
from random import randint
import classes.Asset as Asset
from classes.Image import Image
from classes.Color import Color
from games.diskShooting.classes.Button import Button

class Start():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.state = 'intro'

    def Start(self, screen):
        # define colors
        black = (0, 0, 0)
        white = (255, 255, 255)
        blue = (28, 163, 236)
        green = (0, 200, 0)
        red = (200, 0, 0)
        yellow = (255, 255, 0)

        # display size
        display_width = 800
        display_height = 600
        gameDisplay = screen.gameDisplay

        # images
        crowdImg = pygame.image.load(Asset.loadpath('zwemmen', 'img', 'crowd.png'))
        swimmerImg = pygame.image.load(Asset.loadpath('zwemmen', 'img', 'swimmer.png'))
        finishImg = pygame.image.load(Asset.loadpath('zwemmen', 'img', 'finish.png'))
        waterImg = pygame.image.load(Asset.loadpath('zwemmen', 'img', 'water.jpg'))
        tilesImg = pygame.image.load(Asset.loadpath('zwemmen', 'img', 'tiles.jpg'))

        # transform image sizes to match display
        crowdImg = pygame.transform.scale(crowdImg, (800, 150))
        waterImg = pygame.transform.scale(waterImg, (700, 350))
        tilesImg = pygame.transform.scale(tilesImg, (800, 600))

        # decorate game window
        pygame.display.set_caption('Olympische Spelen - Swimming')

        # text - font
        largeText = pygame.font.Font(Asset.loadpath('font', 'roboto', 'Roboto-Medium.ttf'), 35)
        smallText = pygame.font.Font(Asset.loadpath('font', 'roboto', 'Roboto-Medium.ttf'), 20)

        # players energy bar

        def energy_bar(player_energy):

            # energy bar color states
            if player_energy > 75:
                player_energy_color = green
            elif player_energy > 50:
                player_energy_color = yellow
            else:
                player_energy_color = red

            pygame.draw.rect(gameDisplay, player_energy_color, (680, 25, player_energy, 25))

        # trigger to finish the game
        def win_condition(finish, player):
            if finish.colliderect(player):
                print('Finished!')
                return True

        # create random array of keys that must be pressed to move player
        def randomKey():
            random = randint(0, 25)
            if random == 0:
                return 'q'
            elif random == 1:
                return 'w'
            elif random == 2:
                return 'e'
            elif random == 3:
                return 'r'
            elif random == 4:
                return 't'
            elif random == 5:
                return 'y'
            elif random == 6:
                return 'u'
            elif random == 7:
                return 'i'
            elif random == 8:
                return 'o'
            elif random == 9:
                return 'p'
            elif random == 10:
                return 'a'
            elif random == 11:
                return 's'
            elif random == 12:
                return 'd'
            elif random == 13:
                return 'f'
            elif random == 14:
                return 'g'
            elif random == 15:
                return 'h'
            elif random == 16:
                return 'j'
            elif random == 17:
                return 'k'
            elif random == 18:
                return 'l'
            elif random == 19:
                return 'z'
            elif random == 20:
                return 'x'
            elif random == 21:
                return 'c'
            elif random == 22:
                return 'v'
            elif random == 23:
                return 'b'
            elif random == 24:
                return 'n'
            elif random == 25:
                return 'm'

        # main game loop
        def game_loop(screen):

            gameExit = False

            # begin coordinates of player character
            lead_x = 20
            lead_y = 300

            # set level of player's energy
            player_energy = 101

            counter, text = 0, '0'.rjust(3)
            pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
            font = pygame.font.SysFont(Asset.loadpath('font', 'roboto', 'Roboto-Medium.tff'), 30)

            # define score
            count = 0

            # define movement
            moved = randomKey()
            key_pressed = None

            print(moved)

            while not gameExit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True

                    if event.type == pygame.KEYDOWN:
                        key_pressed = pygame.key.name(event.key)

                    if key_pressed == moved and player_energy > 15:
                        lead_x += 20
                        player_energy -= 15
                        moved = randomKey()

                        # energy regeneration
                if player_energy < 100:
                    player_energy += 0.4
                else:
                    player_energy = 101

                pygame.display.update()
                count += 1  # SCORE

                # tiles
                # gameDisplay.fill((169,169,169))
                gameDisplay.blit(tilesImg, (0, 0))

                # crowd background
                gameDisplay.blit(crowdImg, (0, 0))

                # pool background
                # pygame.draw.rect(gameDisplay, blue, (50,200,700,350))
                gameDisplay.blit(waterImg, (50, 200))

                # timer background
                pygame.draw.rect(gameDisplay, white, (24, 40, 135, 40))

                # energy background
                pygame.draw.rect(gameDisplay, white, (675, 20, 111, 35))

                # key_pressed background
                pygame.draw.rect(gameDisplay, white, (375, 50, 50, 50))

                # energy bar
                energy_bar(player_energy)

                # finish image
                finish_rect = gameDisplay.blit(finishImg, (750, 150))

                # key must press
                gameDisplay.blit(font.render(moved, True, (0, 0, 0)), (390, 60))

                # swimmer / player
                player_rect = gameDisplay.blit(swimmerImg, [lead_x, lead_y, 10, 20])

                # calling finish trigger function
                if (win_condition(finish_rect, player_rect)):
                    return ['end', count]
                # return score (count)

                # < 2400 SCORE = GOLD MEDAL
                # < 2750 SCORE = SILVER MEDAL
                # < 3250 SCORE = BRONZE MEDAL
                # > 3250 SCORE = NO MEDAL

                # blitting score on screen
                textSurface = font.render(str(count), False, (0, 0, 0))
                gameDisplay.blit(textSurface, (32, 48))

                pygame.display.update()

            pygame.quit()
            quit()

        def game_intro(screen):
            # Main screen text
            logo = Image(Asset.loadpath('zwemmen', 'img', 'logo.jpg'), [0, 0])
            background = Image(Asset.loadpath('zwemmen', 'img', 'background.jpg'), [0, 0])
            intructions = Image(Asset.loadpath('zwemmen', 'img', 'instructions.jpg'), [150, 200])

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
                return ['score', 'zwemmen', result[1]]
            elif self.state == 'quit':
                pygame.display.quit()
                pygame.quit()
            elif self.state == 'return':
                return 'start'

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()
