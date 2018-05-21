from pygame import *
import random
from games.diskShooting.classes.Button import Button
import classes.Asset as Asset
from classes.Color import Color
from classes.Image import Image
import pygame

windowX = 800
windowY = 500

init()
clock = time.Clock()
window = display.set_mode((windowX, windowY))

ground = windowY - 70

gravity = 1

class PlayerClass:
    def __init__(self, scale, imageChangeSpeed, terminalVelocity):
        self.run1 = transform.scale(image.load(Asset.loadpath('hordelopen', 'img', 'runner1.png')),
                                    (7 * scale, 14 * scale))
        self.run2 = transform.scale(image.load(Asset.loadpath('hordelopen', 'img', 'runner2.png')),
                                    (7 * scale, 14 * scale))
        self.run3 = transform.scale(image.load(Asset.loadpath('hordelopen', 'img', 'runner3.png')),
                                    (7 * scale, 14 * scale))
        self.run4 = transform.scale(image.load(Asset.loadpath('hordelopen', 'img', 'runner4.png')),
                                    (7 * scale, 14 * scale))
        self.run5 = transform.scale(image.load(Asset.loadpath('hordelopen', 'img', 'runner5.png')),
                                    (7 * scale, 14 * scale))

        self.scale = scale
        self.imageChangeSpeed = imageChangeSpeed
        self.terminalVelocity = terminalVelocity

        self.height = 14 * scale
        self.width = 7 * scale

    dead = False

    def update(self):
        self.physics()

        if self.touchingHurdle():
            self.dead = True

        if not self.dead:
            self.playerInput()

        self.y += self.velocityY

        self.show()

    def touchingHurdle(self):
        for hurdle in hurdleManager.hurdleList:
            if self.x + self.width > hurdle.x:
                if self.x < hurdle.x + hurdle.width:
                    if self.y + self.height > hurdle.y:
                        return True

    x = 100
    y = 100

    velocityY = 0

    def playerInput(self):
        pressedKeys = key.get_pressed()

        if pressedKeys[K_SPACE]:
            if self.y + self.height == ground:
                self.velocityY -= 10
            else:
                self.velocityY -= gravity / 2

    def physics(self):
        if self.dead:
            if self.y < windowY:
                self.velocityY += 1


        elif self.y + self.height < ground:
            if self.velocityY < self.terminalVelocity:
                self.velocityY += gravity


        elif self.velocityY > 0:
            self.velocityY = 0
            self.y = ground - self.height

    runTick = 0

    def show(self):
        if self.runTick <= self.imageChangeSpeed:
            img = self.run1
        elif self.runTick <= self.imageChangeSpeed * 2:
            img = self.run2
        elif self.runTick <= self.imageChangeSpeed * 3:
            img = self.run3
        elif self.runTick <= self.imageChangeSpeed * 4:
            img = self.run4
        else:
            img = self.run5

        self.runTick += 1

        if self.runTick >= self.imageChangeSpeed * 5:
            self.runTick = 0

        window.blit(img, (self.x, self.y))

player = PlayerClass(5, 6, 10)

class HurdleManager:
    def __init__(self, scale, spawnRange):
        self.img = transform.scale(image.load(Asset.loadpath('hordelopen', 'img', 'obstacle_48x128.png')),
                                   (7 * scale, 15 * scale))

        self.spawnRange = spawnRange
        self.hurdleList = []
        self.scale = scale

    def update(self, doSpawn, moveSpeed):
        if doSpawn:
            self.spawn()
        self.manage(moveSpeed)

    def manage(self, moveSpeed):
        hurdles2 = []

        for hurdle in self.hurdleList:
            hurdle.update(moveSpeed)

            if hurdle.onScreen():
                hurdles2.append(hurdle)

        self.hurdleList = hurdles2

    spawnTick = 0

    def spawn(self):
        if self.spawnTick >= self.spawnRange[1]:
            newHurdle = HurdleClass(windowX, self.img, 7 * self.scale, 15 * self.scale)
            self.hurdleList.append(newHurdle)
            self.spawnTick = 0

        elif self.spawnTick > self.spawnRange[0]:
            if random.randint(0, self.spawnRange[1] - self.spawnRange[0]) == 0:
                newHurdle = HurdleClass(windowX, self.img, 7 * self.scale, 15 * self.scale)
                self.hurdleList.append(newHurdle)
                self.spawnTick = 0

        self.spawnTick += 1

hurdleManager = HurdleManager(3, (45, 90))

class HurdleClass:
    def __init__(self, x, img, width, height):
        self.x = x
        self.img = img
        self.width = width
        self.height = height
        self.y = ground - height

    def update(self, moveSpeed):
        self.move(moveSpeed)
        self.show()

    def move(self, moveSpeed):
        self.x -= moveSpeed

    def show(self):
        window.blit(self.img, (self.x, self.y))

    def onScreen(self):
        if self.x + self.width > 0:
            return True
        else:
            return False

def mainEventLoop():
    for events in event.get():
        if events.type == KEYDOWN:
            if events.key == K_ESCAPE:
                quit()

groundImg = transform.scale(image.load(Asset.loadpath('hordelopen', 'img', '491830606.jpg')),
                            (windowX, int(windowY)))

font1 = font.Font(Asset.loadpath('font', 'roboto', 'Roboto-Medium.ttf'), 20)
font2 = font.Font(Asset.loadpath('font', 'roboto', 'Roboto-Medium.ttf'), 20)
deathMessage1 = font1.render('NO MEDAL!', True, (0, 0, 0))
deathMessage2 = font2.render('Press Space to continue', True, (0, 0, 0))
deathMessage3 = font2.render('Press Escape to quit', True, (0, 0, 0))

bronzeMsg = font1.render('Bronze Medal!', True, (205, 127, 50))
silverMsg = font1.render('Silver Medal!', True, (192, 192, 192))
goldMsg = font1.render('Gold Medal!', True, (255, 215, 0))

message1Rect = deathMessage1.get_rect()
message1x = windowX / 2 - message1Rect.width / 2

message2Rect = deathMessage2.get_rect()
message2x = windowX / 2 - message2Rect.width / 2

message3Rect = deathMessage3.get_rect()
message3x = windowX / 2 - message3Rect.width / 2

def showMessage(y, score):
    # if score >= 1000 and score <= 1200:
    #     window.blit(bronzeMsg, (message1x, y))
    # elif score > 1200 and score <= 1400:
    #     window.blit(silverMsg, (message1x, y))
    # elif score > 1400 and score <= 10000:
    #     window.blit(goldMsg, (message1x, y))
    # else:
    #     window.blit(deathMessage1, (message1x, y))

    window.blit(deathMessage2, (message2x, y + message1Rect.height))
    # window.blit(deathMessage3, (message3x, y + message1Rect.height + message2Rect.height))

score = {'gameScore': 0}

def game():
    player.update()
    while True:
        if player.dead:
            fall(scoreStr)
            return ['end', score['gameScore']]

        mainEventLoop()
        window.fill((200, 240, 250))

        player.update()

        hurdleManager.update(True, score['gameScore'] / 50 + 3)
        window.blit(groundImg, (0, ground))

        clock.tick(60)

        scoreStr = font2.render(str(round(score['gameScore'])), True, (0, 0, 0))
        window.blit(scoreStr, (50, 50))
        display.update()

        score['gameScore'] += 1

def fall(scoreStr):
    space = 0
    while True:
        pressedKeys = key.get_pressed()

        oldSpace = space
        space = pressedKeys[K_SPACE]

        mainEventLoop()
        window.fill((200, 240, 250))

        player.update()

        hurdleManager.update(False, score['gameScore'] / 50 + 3)
        window.blit(groundImg, (0, ground))

        clock.tick(60)

        showMessage(50, score['gameScore'])

        window.blit(scoreStr, (50, 50))
        display.update()

        spaceEvent = space - oldSpace

        if spaceEvent == 1:
            # Reset Everything

            hurdleManager.hurdleList = []
            player.velocityY = 0
            player.dead = False
            player.y = ground - player.height
            # score['gameScore'] = 0

            break

# loop

class Start:
    def __init__(self):
        self.state = 'intro'
        self.clock = pygame.time.Clock()
        # decorate game window
        pygame.display.set_caption('Olympische Spelen - Hurdling')

    def play(self, screen):
        self.state = 'intro'
        self.clock = pygame.time.Clock()

        def game_intro(screen):
            # Main screen text
            logo = Image(Asset.loadpath('hordelopen', 'img', 'logo.jpg'), [0, 0])
            background = Image(Asset.loadpath('hordelopen', 'img', 'background.jpg'), [0, 0])
            intructions = Image(Asset.loadpath('hordelopen', 'img', 'intructions.jpg'), [215, 185])


            # Buttons
            start_btn = Button()
            quit_btn = Button()

            clock = pygame.time.Clock()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return 'quit'

                screen.gameDisplay.blit(background.image, background.rect)
                screen.gameDisplay.blit(intructions.image, intructions.rect)
                screen.gameDisplay.blit(logo.image, logo.rect)

                check_start = start_btn.setButton("Start", 150, 450, 100, 50, Color.GREEN.getRGB(),
                                                  Color.DARK_GREEN.getRGB(),
                                                  screen, 'game')
                check_end = quit_btn.setButton("Return", 550, 450, 100, 50, Color.RED.getRGB(), Color.DARK_RED.getRGB(),
                                               screen,
                                               'return')

                # Return results of button clicked
                if check_start != None:
                    return 'game'
                elif check_end != None:
                    return 'return'
                else:
                    pygame.display.update()
                    clock.tick(15)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                    break
            if self.state == 'intro':
                result = game_intro(screen)
                if result == None:
                    break
                else:
                    self.state = result
            elif self.state == 'game':
                score['gameScore'] = 0
                result = game()
                print(result)
                if result == None:
                    break
                else:
                    self.state = result[0]
            elif self.state == 'end':
                self.state = 'intro'
                return ['score', 'hordelopen', result[1]]
            elif self.state == 'quit':
                pygame.display.quit()
                pygame.quit()
            elif self.state == 'return':
                return 'start'


            pygame.display.update()
            self.clock.tick(60)

        pygame.display.quit()
        pygame.quit()
