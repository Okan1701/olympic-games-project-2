import pygame
import games.zeilen.Globals as globals
import games.zeilen.Resources as resources

tiles = list()

#Background class
#The background class is basicly the water tile. Several instances of this are created and used to fill the screen with water.
class Background(pygame.sprite.Sprite):
    scroll_speed = 1  # Speed at which a tile goes downwards.

    # The '__init__' method of a class is always automaticly executed when a new instance is created  (constructor)
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(
            self)  # Idk what this does, but it's needed to make the sprite behave as a pygame sprite.
        self.image = resources.sprites[
            "spr_water"]  # Sets the image of this sprite to the image of the water tile we loaded earlier
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        globals.background_sprites.add(self)  # Add this newly created instance to the globals.background_sprites Group
        tiles.append(self)

    # Update method is called ever single loop in order to ensure that the background behav
    def update(self):
        self.rect.y += self.scroll_speed

        if self.rect.top == globals.window_height:
            self.rect.top = -32

#This method is used to create the background water. The background consists of water tiles (32x32) that are used to fill the screen
#Each water tile is a seperate instance which is scripted to move downwards with a consistant speed to create the illusion of movement.
def create_background():
    screenx = globals.window_width

    for i in range(0,screenx,32):
        Background(i,-32)
        Background(i,32*0)
        Background(i,32*1)
        Background(i,32*2)
        Background(i,32*3)
        Background(i,32*4)
        Background(i,32*5)
        Background(i,32*6)
        Background(i,32*7)
        Background(i,32*8)
        Background(i,32*9)
        Background(i,32*10)
        Background(i,32*11)
        Background(i,32*12)
        Background(i,32*13)
        Background(i,32*14)
        Background(i,32*15)
        Background(i,32*16)
        Background(i,32*17)
        Background(i,32*18)
