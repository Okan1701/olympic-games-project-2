import pygame
import sys
from classes.Screen import Screen
from classes.Color import Color
import classes.Asset as Asset
import games.diskShooting.Start
import games.hordelopen.Start
import games.zeilen.Zeilen
import games.gewichtheffen.main
import games.zwemmen.game_loop
import games.skiing.skien_game

import classes.EndScreen as EndScreen
from classes.Image import Image

pygame.init()
games_sprites = pygame.sprite.Group()

pygame.mixer.music.load(Asset.loadpath('homescreen', 'sound', 'background.mp3'))
pygame.mixer.music.play(-1)

# Start Pygame clock
clock = pygame.time.Clock()

# Set window in a variable
window = Screen(800, 600)

diskShooting = games.diskShooting.Start.Start(window)

game_running = True
state = 'start'
gamename = ''
score = 1

class homeScreen():
    def __init__(self):
        self.clicked = False
        self.games = {
            'diskShooting': '',
            'hordelopen': '',
            'zwemmen': '',
            'skiing': '',
            'gewichtheffen': '',
            'zeilen': '',
        }

    def updateGames(self, game, score):
        self.games[game] = score

    def getMedal(self, medal, pos):
        if medal == 'bronze':
            return Image(Asset.loadpath('homescreen', 'img', 'bronze.png'), pos)
        elif medal == 'silver':
            return Image(Asset.loadpath('homescreen', 'img', 'silver.png'), pos)
        elif medal == 'gold':
            return Image(Asset.loadpath('homescreen', 'img', 'gold.png'), pos)

        return None

    def displayScores(self, screen):
        if self.games['diskShooting'] != '':
            displayMedalIMG = self.getMedal(self.games['diskShooting'], [25, 450])
            if displayMedalIMG != None:
                screen.gameDisplay.blit(displayMedalIMG.image, displayMedalIMG.rect)
        if self.games['zeilen'] != '':
            displayMedalIMG = self.getMedal(self.games['zeilen'], [350, 450])
            if displayMedalIMG != None:
                screen.gameDisplay.blit(displayMedalIMG.image, displayMedalIMG.rect)
        if self.games['hordelopen'] != '':
            displayMedalIMG = self.getMedal(self.games['hordelopen'], [190, 450])
            if displayMedalIMG != None:
                screen.gameDisplay.blit(displayMedalIMG.image, displayMedalIMG.rect)
        if self.games['skiing'] != '':
            displayMedalIMG = self.getMedal(self.games['skiing'], [510, 450])
            if displayMedalIMG != None:
                screen.gameDisplay.blit(displayMedalIMG.image, displayMedalIMG.rect)
        if self.games['zwemmen'] != '':
            displayMedalIMG = self.getMedal(self.games['zwemmen'], [670, 450])
            if displayMedalIMG != None:
                screen.gameDisplay.blit(displayMedalIMG.image, displayMedalIMG.rect)
        if self.games['gewichtheffen'] != '':
            displayMedalIMG = self.getMedal(self.games['gewichtheffen'], [670, 270])
            if displayMedalIMG != None:
                screen.gameDisplay.blit(displayMedalIMG.image, displayMedalIMG.rect)

    def startingScreen(self, screen):
        pygame.display.set_caption("Olympische Spelen")
        imgBackground = Image(Asset.loadpath('homescreen', 'img', 'background.png'), [0, 0])
        scoreBackground = Image(Asset.loadpath('homescreen', 'img', 'scoreboard.png'), [0, 235])

        # Zeilen
        btnZeilen = Image(Asset.loadpath('homescreen', 'img', 'btnZeilen.png'), [241, 350])
        btnZeilenHover = Image(Asset.loadpath('homescreen', 'img', 'btnZeilenHover.png'), [241, 350])

        # Disk shooting
        btnDiskshooting = Image(Asset.loadpath('homescreen', 'img', 'btnDiskShooting.png'), [102, 253])
        btnDiskshootingHover = Image(Asset.loadpath('homescreen', 'img', 'btnDiskShootingHover.png'), [102, 253])

        # Hordelopen
        btnHordelopen = Image(Asset.loadpath('homescreen', 'img', 'btnHordelopen.png'), [622, 160])
        btnHordelopenHover = Image(Asset.loadpath('homescreen', 'img', 'btnHordelopenHover.png'), [622, 160])

        # Skiing
        btnSkiing = Image(Asset.loadpath('homescreen', 'img', 'btnBoksen.png'), [320, 202])
        btnSkiingHover = Image(Asset.loadpath('homescreen', 'img', 'btnBoksenHover.png'), [320, 202])

        btnZwemmen = Image(Asset.loadpath('homescreen', 'img', 'btnZwemmen.png'), [39, 75])
        btnZwemmenHover = Image(Asset.loadpath('homescreen', 'img', 'btnZwemmenHover.png'), [39, 75])

        btnGewichtsheffen = Image(Asset.loadpath('homescreen', 'img', 'btnGewichtsheffen.png'), [392, 81])
        btnGewichtsheffenHover = Image(Asset.loadpath('homescreen', 'img', 'btnGewichtsheffenHover.png'), [392, 81])

        while True:
            self.clicked = False
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    global clicked
                    self.clicked = True

            screen.gameDisplay.fill((Color.BLACK.getRGB()))
            screen.gameDisplay.blit(imgBackground.image, imgBackground.rect)
            screen.gameDisplay.blit(scoreBackground.image, scoreBackground.rect)

            # Working games
            btnHordelopenRect = screen.gameDisplay.blit(btnHordelopen.image, btnHordelopen.rect)
            btnDiskshootingRect = screen.gameDisplay.blit(btnDiskshooting.image, btnDiskshooting.rect)
            btnZeilenRect = screen.gameDisplay.blit(btnZeilen.image, btnZeilen.rect)
            btnSkiingRect = screen.gameDisplay.blit(btnSkiing.image, btnSkiing.rect)
            btnZwemmenRect = screen.gameDisplay.blit(btnZwemmen.image, btnZwemmen.rect)

            # Games that will be tzken out of the game if needed
            btnGewichtsheffenRect = screen.gameDisplay.blit(btnGewichtsheffen.image, btnGewichtsheffen.rect)

            self.displayScores(screen)

            # Check if button is clicked
            if btnHordelopenRect.collidepoint(pygame.mouse.get_pos()) and self.clicked:
                return 'hordelopen'
            elif btnDiskshootingRect.collidepoint(pygame.mouse.get_pos()) and self.clicked:
                return 'diskShooting'
            elif btnZeilenRect.collidepoint(pygame.mouse.get_pos()) and self.clicked:
                return 'zeilen'
            elif btnSkiingRect.collidepoint(pygame.mouse.get_pos()) and self.clicked:
                return 'skiing'
            elif btnZwemmenRect.collidepoint(pygame.mouse.get_pos()) and self.clicked:
                return 'zwemmen'
            elif btnGewichtsheffenRect.collidepoint(pygame.mouse.get_pos()) and self.clicked:
                return 'gewichtheffen'

            # On hover effect
            if btnDiskshootingRect.collidepoint(pygame.mouse.get_pos()):
                btnDiskshootingRect = screen.gameDisplay.blit(btnDiskshootingHover.image, btnDiskshootingHover.rect)
            elif btnHordelopenRect.collidepoint(pygame.mouse.get_pos()):
                btnHordelopenRect = screen.gameDisplay.blit(btnHordelopenHover.image, btnHordelopenHover.rect)
            elif btnZeilenRect.collidepoint(pygame.mouse.get_pos()):
                btnZeilenRect = screen.gameDisplay.blit(btnZeilenHover.image, btnZeilenHover.rect)
            elif btnZwemmenRect.collidepoint(pygame.mouse.get_pos()):
                btnZwemmenRect = screen.gameDisplay.blit(btnZwemmenHover.image, btnZwemmenHover.rect)
            elif btnSkiingRect.collidepoint(pygame.mouse.get_pos()):
                btnSkiingRect = screen.gameDisplay.blit(btnSkiingHover.image, btnSkiingHover.rect)
            elif btnGewichtsheffenRect.collidepoint(pygame.mouse.get_pos()):
                btnGewichtsheffenRect = screen.gameDisplay.blit(btnGewichtsheffenHover.image,
                                                                btnGewichtsheffenHover.rect)

            # If no button has been pressed then stay in start screen
            return 'start'

homeScreen = homeScreen()

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.display.quit()
            pygame.quit()
            sys.exit(0)
    if state == 'start':
        state = homeScreen.startingScreen(window)
    elif state == 'diskShooting':
        window.defaultCursor()
        result = diskShooting.play(window)
        if isinstance(result, list):
            state = result[0]
            gamename = result[1]
            score = result[2]
        else:
            state = 'start'
    elif state == 'zeilen':
        window.defaultCursor()
        zeilen_obj = games.zeilen.Zeilen.Start()
        result = zeilen_obj.start(window)
        if isinstance(result, list):
            state = result[0]
            gamename = result[1]
            score = result[2]
        else:
            state = 'start'
    elif state == 'gewichtheffen':
        window.defaultCursor()
        gewichtheffen_obj = games.gewichtheffen.main.Start()
        result = gewichtheffen_obj.Start(window)
        if isinstance(result, list):
            state = result[0]
            gamename = result[1]
            score = result[2]
        else:
            state = 'start'
    elif state == 'hordelopen':
        window.defaultCursor()
        hordelopen_obj = games.hordelopen.Start.Start()
        result = hordelopen_obj.play(window)
        if isinstance(result, list):
            state = result[0]
            gamename = result[1]
            score = result[2]
        else:
            state = 'start'
    elif state == 'skiing':
        window.defaultCursor()
        skiing_obj = games.skiing.skien_game.Start()
        result = skiing_obj.Start(window)
        if isinstance(result, list):
            state = result[0]
            gamename = result[1]
            score = result[2]
        else:
            state = 'start'
    elif state == 'zwemmen':
        window.defaultCursor()
        zwemmen_obj = games.zwemmen.game_loop.Start()
        result = zwemmen_obj.Start(window)
        if isinstance(result, list):
            state = result[0]
            gamename = result[1]
            score = result[2]
        else:
            state = 'start'
    elif state == 'score':
        window.defaultCursor()
        pygame.mouse.set_visible(True)
        result = EndScreen.endscreen(window, gamename, score)
        if result == None:
            break
        else:
            state = result[0]
            homeScreen.updateGames(result[1], result[2])
    elif state == 'quit':
        pygame.display.quit()
        pygame.quit()
        sys.exit(0)

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
pygame.quit()
sys.exit(0)
