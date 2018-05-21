import pygame, os
import games.zeilen.Globals as globals
import classes.Asset as Asset

# All sprite images we load will be stored in this dictionary (cached) and made available to be used.
sprites = {}
sounds = {}

# Load resources
def init():
    load_image(Asset.loadpath('zeilen', 'img', 'player.png'), "spr_player", None)
    load_image(Asset.loadpath('zeilen', 'img', 'obstacle_0.png'), "spr_obstacle_0", None)
    load_image(Asset.loadpath('zeilen', 'img', 'obstacle_1.png'), "spr_obstacle_1", None)
    load_image(Asset.loadpath('zeilen', 'img', 'water.gif'), "spr_water", None)
    load_image(Asset.loadpath('zeilen', 'img', 'finish.png'), "spr_finish", None)
    load_sound(Asset.loadpath('zeilen', 'sound', 'death.wav'), "snd_death")
    load_sound(Asset.loadpath('zeilen', 'sound', 'finish.wav'), "snd_finish")

# load_image method (function)
# Used to load images from assets folder and store it in the dictionary so that it can be used later on.

# file : name of the file (including extension) to load from assets folder
# name : used to give new image a name inside the dictionary. This name is used to retrieve it again from the dictionary
# color_key : (Optional, use None if not needed) this is usefull if you want to remove the background color
def load_image(file, name, color_key):
    print("Loading image: " + file + " as " + name)
    img = pygame.image.load(file)
    img.convert()  # Convert it to pygame friendly format

    if color_key != None:
        img.set_colorkey(color_key)

    sprites[name] = img  # Add image to dictionary with with variable name as id.

def load_sound(file, name):
    print("Loading sound: " + file + " as " + name)
    sounds[name] = pygame.mixer.Sound(file)

def play_sound(name):
    print("Playing sound: " + str(name))
    name.play()
