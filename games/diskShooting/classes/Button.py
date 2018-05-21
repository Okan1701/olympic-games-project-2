import pygame
from games.diskShooting.classes.textObject import textObject
import classes.Asset as Asset
from classes.Color import Color

class Button():
    def setButton(self, msg, x, y, w, h, ic, ac, screen, action=None):
        # Button click action
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # mouse[0] = x coordinates of mouse,
        # mouse[1] = y coordinates of mouse,
        # x = position button | horizontal
        # y = position button | vertical
        # w = width button
        # h = height button
        # ic = background-color
        # ac = background-color on hover
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            # You are hovering over the button
            pygame.draw.rect(screen.gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                return action
        else:
            pygame.draw.rect(screen.gameDisplay, ic, (x, y, w, h))

        text_Object = textObject()
        # Button text
        smallText = pygame.font.Font(Asset.loadpath('font', 'roboto', 'Roboto-Medium.ttf'), 20)
        self.textSurf, self.textRect = text_Object.textObjects(msg, smallText, Color.WHITE.getRGB(), (y + (h / 2)), (x + (w / 2)))
        self.textRect.center = ((x + (w / 2)), (y + (h / 2)))
        screen.gameDisplay.blit(self.textSurf, self.textRect)
