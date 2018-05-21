import pygame
import classes.Asset as Asset

background = pygame.image.load(Asset.loadpath('gewichtheffen', 'img', 'background.jpg'))
backgroundrect = pygame.transform.scale(background, (800, 600))
homescherm = pygame.image.load(Asset.loadpath('gewichtheffen', 'img', 'homescherm.jpg'))
homeschermrect = pygame.transform.scale(homescherm, (800, 600))
personstart = pygame.image.load(Asset.loadpath('gewichtheffen', 'img', 'personstart.png'))
personlift = pygame.image.load(Asset.loadpath('gewichtheffen', 'img', 'personlift.png'))
personlifted = pygame.image.load(Asset.loadpath('gewichtheffen', 'img', 'personlifted.png'))
personstartrect = pygame.transform.scale(personstart, (100, 200))
personliftrect = pygame.transform.scale(personlift, (100, 200))
personliftedrect = pygame.transform.scale(personlifted, (100, 200))
