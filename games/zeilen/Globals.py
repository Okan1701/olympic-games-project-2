import pygame, os

fps = 30
title = "Zeilen"
window_width = 800
window_height = 600
resource_dir = (os.getcwd()+"\\Assets\\")
screen_boundry = 8
timer_start_value = 30000

obstacle_default_speed = 4
disable_obstacles = False
obstacle_speed_incr_value = 0.006
obstacle_spawn_delay = 2000

player_sprites = pygame.sprite.Group() #Contains the player sprites.
obstacle_sprites = pygame.sprite.Group() # Contains all obstacle sprites
background_sprites = pygame.sprite.Group() #Will contain all the background sprites.
misc_sprites = pygame.sprite.Group() #Misc

WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_GREY = (68, 68, 68)

#-----RUNTIME VARIABLES-----

state = 1
finish_spawned = False
obstacle_speed = obstacle_default_speed
timer = timer_start_value
times_hit = 0
