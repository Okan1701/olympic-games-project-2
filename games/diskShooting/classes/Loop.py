import pygame
import classes.Asset as Asset
from classes.Color import Color
from classes.Image import Image
from games.diskShooting.classes.Button import Button
import threading
from random import randint

def game_intro(screen):
    # Main screen text
    logo = Image(Asset.loadpath('disk_shooting', 'img', 'logo.jpg'), [0, 0])
    background = Image(Asset.loadpath('disk_shooting', 'img', 'background_intro.jpg'), [0, 0])
    instructions = Image(Asset.loadpath('disk_shooting', 'img', 'instructions.jpg'), [200, 125])

    # Buttons
    start_btn = Button()
    quit_btn = Button()

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'

        screen.gameDisplay.blit(background.image, background.rect)
        screen.gameDisplay.blit(instructions.image, instructions.rect)
        screen.gameDisplay.blit(logo.image, logo.rect)

        check_start = start_btn.setButton("Start", 150, 450, 100, 50, Color.GREEN.getRGB(), Color.DARK_GREEN.getRGB(),
                                          screen, 'game')
        check_end = quit_btn.setButton("Return", 550, 450, 100, 50, Color.RED.getRGB(), Color.DARK_RED.getRGB(), screen,
                                       'return')

        # Return results of button clicked
        if check_start != None:
            return 'game'
        elif check_end != None:
            return 'return'
        else:
            pygame.display.update()
            clock.tick(15)

def game_loop(screen, disk, person):
    # A tread that resets the disk whenever it goes out of bound
    class UpdateThread(threading.Thread):
        running = True

        def run(self):
            print("Update called")
            # Keep running this thread until the application is closed or crashed
            while self.running:
                # Update the disk
                disk.update_thread()
            print("Update ended")

        def close(self):
            self.running = False

    # A tread that is called whenever the player has show the disk
    class ShootingThread(threading.Thread):
        def run(self):
            print("Shooting called")
            # Stop movement of the disk
            disk.run = False

            # Reset position of the disk
            disk.reset()

            # Wait 0.5 to 1 sec until the next disk fires
            pygame.time.delay(randint(1000, 5000))
            disk.fire()
            print("Shooting ended")

    # Start the UpdateThread
    updateThread = UpdateThread()
    updateThread.start()

    # Font
    myFont = pygame.font.Font(Asset.loadpath('font', 'roboto', 'Roboto-Medium.ttf'), 30)

    # Beginning text
    myStartFont = pygame.font.Font(Asset.loadpath('font', 'roboto', 'Roboto-Medium.ttf'), 80)
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    getReady = myStartFont.render("Get Ready!", False, Color.WHITE.getRGB())
    countStart = 0

    # Mouse cursor image
    # mousec = pygame.image.load(Asset.loadpath('disk_shooting', 'img', 'cross.png'))
    # BackGround = Background('../assets/background_pix.jpg', [0, 0])

    mousec = pygame.image.load(Asset.loadpath('disk_shooting', 'img', 'cross.png'))
    backGround = Image(Asset.loadpath('disk_shooting', 'img', 'background_pix.jpg'), [0, 0])

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                updateThread.close()
                return None
            screen.gameDisplay.fill(Color.WHITE.getRGB())
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the player has some bullets left
                if person.getBullet() != 0:
                    # Check if the disk is clicked
                    if disk.is_clicked() == 1:
                        # Reset the disk with a delay of between 0.4 sec - 1 sec
                        ShootingThread().start()
                        # Add 1 to score
                        person.addScore()
                    # Remove 1 bullet
                    person.minBullet()
                else:
                    # Show the end screen with the appropriate score
                    return 'end'
            if person.getBullet() == 0:
                updateThread.close()
                return 'end'
            if disk.game_end:
                # Close Threads
                updateThread.close()
                return 'end'

        screen.gameDisplay.blit(backGround.image, backGround.rect)
        # Show the current score and bullets
        person.showScore(myFont, screen)
        person.showBullets(myFont, screen)
        disk.showAmount(myFont, screen)
        # Get the current mouse position (x, y)
        pos = pygame.mouse.get_pos()
        # Update the rotation of the person based on the x coordinates of the mouse
        person.blit(screen)

        if countStart < 1:
            screen.gameDisplay.blit(getReady, (200, 225))
            pygame.display.update()
            pygame.time.delay(1000)
            print('YES')
            countStart = countStart + 1

        # Update all the sprites
        disk.update()
        # Update all the sprites
        disk.getSpriteGroup().update()
        # Draw all the updated sprites on the window
        disk.getSpriteGroup().draw(screen.gameDisplay)
        # Split the pos (x, y) in 2 variables
        Mouse_x, Mouse_y = pos
        # Add a custom cursor
        screen.gameDisplay.blit(mousec, (Mouse_x - 23, Mouse_y - 23))
        # Update the display screen
        pygame.display.update()

        if disk.amount <= 0:
            updateThread.close()
            return 'end'

        # Clock speed
        clock.tick(60)
