import pygame
import classes.Asset as Asset
from classes.Color import Color

# Person class
class Person:
    # Constructor
    def __init__(self, screen):
        # Shooter image
        self.personImg = pygame.image.load(Asset.loadpath('disk_shooting', 'img', 'shooter.png'))
        # Different rotations of the same image
        self.left_personImg = pygame.transform.rotate(self.personImg, 45)
        self.middle_personImg = pygame.transform.rotate(self.personImg, 0)
        self.right_personImg = pygame.transform.rotate(self.personImg, 315)
        # Set base settings
        self.x, self.y = (screen.WindowWidth * 0.40), (screen.WindowHeight * 0.8)
        self.score = 0
        self.bullets = 15
        # Gun shot sound
        self.shot = pygame.mixer.Sound(Asset.loadpath('disk_shooting', 'sound', 'pistol_shot.wav'))

    def blit(self, screen):
        Mouse_x, Mouse_y = screen.getMousePos()
        if Mouse_x <= (screen.WindowWidth / 3):
            person_img = self.left_personImg
        elif Mouse_x >= ((screen.WindowWidth / 3) * 2):
            person_img = self.right_personImg
        else:
            person_img = self.middle_personImg
        screen.gameDisplay.blit(person_img, (self.x, self.y))

    # remove 1 bullet of the clip
    def minBullet(self):
        if self.bullets != 0:
            self.bullets = self.bullets - 1
            self.shot.play()

    # Get the current amount of bullets as an int
    def getBullet(self):
        return self.bullets

    # Add a score
    def addScore(self):
        self.score = self.score + 1

    # Show the current score of the player
    def showScore(self, myfont, screen):
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        textsurface = myfont.render("score: " + str(self.score), False, Color.WHITE.getRGB())
        screen.gameDisplay.blit(textsurface, (20, 550))

    # Show the current amount of bullets
    def showBullets(self, myfont, screen):
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        textsurface = myfont.render("bullets: " + str(self.bullets), False, Color.WHITE.getRGB())
        screen.gameDisplay.blit(textsurface, (630, 550))

    def reset(self):
        self.score = 0
        self.bullets = 15
