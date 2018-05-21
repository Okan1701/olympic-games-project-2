import pygame
import games.zeilen.GameObjects
import games.zeilen.Globals as globals
from random import randint

class ObstacleController():
    prev_tick = pygame.time.get_ticks()
    delay = globals.obstacle_spawn_delay

    def update(self):
        if globals.disable_obstacles == False:
            now = pygame.time.get_ticks()
            if now - self.prev_tick >= self.delay:
                int1 = randint(1, 2)
                int2 = randint(1,4)
                int3 = randint(1, 2)
                x1 = randint(8, 775)
                x2 = randint(8, 775)
                x3 = randint(8, 775)
                #x4 = randint(8, 775)
                games.zeilen.GameObjects.Obstacle0(x1, -50)
                games.zeilen.GameObjects.Obstacle0(x3, -75)
                #GameObjects.Obstacle0(x2, -50)
                #GameObjects.Obstacle0(x3, -50)
                #GameObjects.Obstacle0(x4, -50)
                if int1 == 2:
                    games.zeilen.GameObjects.Obstacle0(x2, -50)
                if int2 == 4:
                    games.zeilen.GameObjects.Obstacle1(-50, randint(50, 400))
                if globals.timer < (globals.timer_start_value / 2) and int3 == 2:
                    games.zeilen.GameObjects.Obstacle0(x2, -50).speed *= 2

                self.prev_tick = pygame.time.get_ticks()

def incr_obstacle_spd(spd_incr):
    globals.obstacle_speed += spd_incr
    list = globals.obstacle_sprites.sprites()
    for sprite in list:
        sprite.speed = globals.obstacle_speed

def create_finish():
    for i in range(0, 800, 32):
        games.zeilen.GameObjects.Finish(i, -32)
    globals.finish_spawned = True

def restart():
    globals.state = 1
    games.zeilen.GameObjects.Player()
    globals.timer = globals.timer_start_value
    globals.times_hit = 0
    globals.obstacle_speed = globals.obstacle_default_speed
    globals.finish_spawned = False
