import pygame
import classes.Asset as Asset
from random import randint
from classes.Color import Color

class Disk(pygame.sprite.Sprite):
    def __init__(self, person, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Asset.loadpath('disk_shooting', 'img', 'disk_pix.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (self.rnd())
        self.SPRITE_GROUP = pygame.sprite.Group()
        self.SPRITE_GROUP.add(self)

        # Amount of disks available = the total of bullets the person starts with
        self.amount = person.bullets
        # Direction
        self.dir_x = 1
        self.dir_y = 1
        # Speed
        self.speed = randint(1, 2)
        # Movement of the disk
        self.run = True  # Used fo threading
        self.game_end = False

        self.screen = screen

    # Randomize starting position + movement
    def rnd(self):
        rnd = randint(0, 10)
        if rnd > 5:
            disk = (850, randint(300, 400))
            self.dir_x = randint(-15, -10)
            self.dir_y = randint(-3, -2)
        else:
            disk = (-50, randint(300, 400))
            self.dir_x = randint(6, 7)
            self.dir_y = randint(-6, -4)
        return disk

    # Updates the movement of the disk | only when self.run is True
    def update(self):
        if self.run:
            self.rect.x += self.dir_x + self.speed  # links/ rechts
            self.rect.y += self.dir_y - self.speed  # beneden/ boven

    def getSpriteGroup(self):
        return self.SPRITE_GROUP

    # Thread updating location of the disk back to starting position when disk is out of bound
    def update_thread(self):
        if self.rect.bottom < 0 or self.rect.left < -170 or self.rect.right > (self.screen.WindowWidth + 170):
            print("STOP RUN _ update_test")
            # Stop movement of the disk
            self.run = False
            # Reset position of the disk
            self.reset()
            # Wait 0.5 to 1 sec until the next disk fires
            pygame.time.delay(randint(500, 1000))
            self.fire()

    # Start disk movement
    def fire(self):
        self.run = True

    # Check whether or not the disk is clicked
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    # Show the current amount of Disks
    def showAmount(self, myfont, screen):
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        textsurface = myfont.render("Disks left: " + str(self.amount), False, Color.WHITE.getRGB())
        screen.gameDisplay.blit(textsurface, (610, 500))

    # Reset the position of the disk | Left or Right
    def reset(self):
        self.amount = self.amount - 1
        if self.amount > 0:
            self.rect.center = (self.rnd())
        else:
            self.run = False
            # End the game
            self.game_end = True

    def hard_reset(self, person):
        # Amount of disks available = the total of bullets the person starts with
        self.amount = person.bullets
        # Direction
        self.dir_x = 1
        self.dir_y = 1
        # Speed
        self.speed = randint(1, 2)
        # Movement of the disk
        self.run = True
        self.game_end = False
        self.rect = self.image.get_rect()
        self.rect.center = (self.rnd())
