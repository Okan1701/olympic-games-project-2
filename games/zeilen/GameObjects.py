import pygame
import games.zeilen.Globals as globals
import games.zeilen.Resources as resources
import games.zeilen.GUI as gui

class Player(pygame.sprite.Sprite):
    speed = 4
    rotated = False

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = resources.sprites["spr_player"]
        self.rect = self.image.get_rect()
        self.rect.center = (globals.window_width / 2, globals.window_height / 2)
        globals.player_sprites.add(self)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # print("Key pressed!")
            if self.rect.top > globals.screen_boundry:
                self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            # print("Key pressed!")
            if self.rect.bottom < (globals.window_height - globals.screen_boundry - 100):
                self.rect.y += self.speed

        if keys[pygame.K_RIGHT]:
            # print("Key pressed!")
            if self.rect.right < (globals.window_width - globals.screen_boundry):
                self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            # print("Key pressed!")
            if self.rect.left > (globals.screen_boundry):
                self.rect.x -= self.speed

class Obstacle0(pygame.sprite.Sprite):
    speed = globals.obstacle_speed
    can_collide = True
    collide_delay = 20000
    prev_collision_tick = None

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = resources.sprites["spr_obstacle_0"]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        globals.obstacle_sprites.add(self)
        print("Spawned " + str(self) + " @ (" + str(x) + "," + str(y) + ")")

    def update(self):
        kill = False
        self.rect.y += self.speed

        if len(pygame.sprite.spritecollide(self, globals.player_sprites, False)) > 0 and self.can_collide == True:
            print("Player has been hit by " + str(self))
            globals.times_hit += 1
            gui.draw_kill_effect()
            self.kill()
            kill = True
            # for player in globals.player_sprites.sprites():
            # if player.rect.right > self.rect.left and player.rect.centerx < (self.rect.right):
            # player.rect.centerx -= 35
            # if player.rect.left < self.rect.right and player.rect.centerx > (self.rect.left):
            # player.rect.centerx += 35


            self.prev_collision_tick = pygame.time.get_ticks()
            self.can_collide = False

        if self.can_collide == False:
            if pygame.time.get_ticks() - self.prev_collision_tick >= 2000:
                self.can_collide = True

        if self.rect.top == globals.window_height:
            self.kill()
            kill = True

        if kill:
            del self

class Obstacle1(pygame.sprite.Sprite):
    speed = globals.obstacle_speed
    can_collide = True
    collide_delay = 20000
    prev_collision_tick = None

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = resources.sprites["spr_obstacle_1"]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        globals.obstacle_sprites.add(self)
        print("Spawned " + str(self) + " @ (" + str(x) + "," + str(y) + ")")

    def update(self):
        kill = False
        self.rect.x += self.speed

        if len(pygame.sprite.spritecollide(self, globals.player_sprites, False)) > 0 and self.can_collide == True:
            print("Player has been hit by " + str(self))
            globals.times_hit += 1
            gui.draw_kill_effect()
            self.kill()
            kill = True
            # for player in globals.player_sprites.sprites():
            # if player.rect.right > self.rect.left and player.rect.centerx < (self.rect.right):
            # player.rect.centerx -= 35
            # if player.rect.left < self.rect.right and player.rect.centerx > (self.rect.left):
            # player.rect.centerx += 35


            self.prev_collision_tick = pygame.time.get_ticks()
            self.can_collide = False

        if self.can_collide == False:
            if pygame.time.get_ticks() - self.prev_collision_tick >= 2000:
                self.can_collide = True

        if self.rect.top == globals.window_height:
            self.kill()
            kill = True

        if kill:
            del self

class Finish(pygame.sprite.Sprite):
    spd = 1

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = resources.sprites["spr_finish"]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        globals.misc_sprites.add(self)

    def update(self):
        self.rect.y += self.spd

        if len(pygame.sprite.spritecollide(self, globals.player_sprites, False)) > 0:
            print("Player has reached the finish!")
            globals.obstacle_sprites.empty()
            globals.misc_sprites.empty()
            globals.player_sprites.empty()
            globals.state = 2

def finish_snd():
    resources.sounds["snd_finish"].play()
