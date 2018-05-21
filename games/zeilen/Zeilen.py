import pygame, os
import games.zeilen.GameObjects as GameObjects
import games.zeilen.Globals as globals
import games.zeilen.Resources as resources
import games.zeilen.BackgroundLayer as background
import games.zeilen.GUI as GUI
import games.zeilen.GameLogic as logic
from classes.Image import Image
import classes.Asset as Asset
from games.diskShooting.classes.Button import Button
from classes.Color import Color

class Start():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.state = 'intro'
        # decorate game window
        pygame.display.set_caption('Olympische Spelen - Sailing')

    def start(self, screen):

        # Main method contains initialization code and the main game loop.
        # It is executed (called) when starting the game.
        def main(screen):
            # ----Start of initialization----

            pygame.mouse.set_visible(False)
            active = True  # This variable controls the main loop. If set to false, main loop will terminate and game will exit.
            resources.init()
            clock = pygame.time.Clock()  # Creates a new clock object, used to control FPS later on.
            gui = GUI.GUI(screen.gameDisplay)

            pygame.time.set_timer(pygame.USEREVENT + 1, 1)

            # Create the player instance and create the background.
            GameObjects.Player()
            controller = logic.ObstacleController()
            background.create_background()

            # ----End of initialization----

            # Main Game loop.
            while active:
                clock.tick(globals.fps)  # Set framerate.

                # Check if user clicked the [x] button at the topright and quit if true.
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        active = False
                    if event.type == (pygame.USEREVENT + 1):
                        if globals.timer > 0:
                            globals.timer -= 9
                        elif globals.timer <= 0 and globals.finish_spawned == False:
                            logic.create_finish()
                        logic.incr_obstacle_spd(globals.obstacle_speed_incr_value)
                if globals.state == 0:
                    gui.draw_intro()
                elif globals.state == 1:
                    screen.gameDisplay.fill((0, 0, 0))
                    controller.update()
                    globals.player_sprites.update()
                    globals.background_sprites.update()
                    globals.obstacle_sprites.update()
                    globals.misc_sprites.update()

                    globals.background_sprites.draw(screen.gameDisplay)
                    globals.misc_sprites.draw(screen.gameDisplay)
                    globals.player_sprites.draw(screen.gameDisplay)
                    globals.obstacle_sprites.draw(screen.gameDisplay)
                    gui.draw_main()
                elif globals.state == 2:
                    return ["end", globals.times_hit]

                pygame.display.update()

            return globals.times_hit
            # pygame.quit() #When the main loop terminates, this line will be executed which quits the game.

        def game_intro(screen):
            # Main screen text
            logo = Image(Asset.loadpath('zeilen', 'img', 'logo.jpg'), [0, 0])
            background = Image(Asset.loadpath('zeilen', 'img', 'background.jpg'), [0, 0])
            intructions = Image(Asset.loadpath('zeilen', 'img', 'ZEILEN_instructions.png'), [0, 0])

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
                result = main(screen)
                print(result)
                if result == None:
                    break
                else:
                    self.state = result[0]
            elif self.state == 'end':
                logic.restart()
                self.state = 'intro'
                return ['score', 'zeilen', result[1]]
            elif self.state == 'quit':
                pygame.display.quit()
                pygame.quit()
            elif self.state == 'return':
                return 'start'

            pygame.display.update()
            self.clock.tick(60)
