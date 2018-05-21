from classes.Color import Color
import pygame
from classes.Image import Image
import classes.Asset as Asset

def endscreen(screen, game, score):
    textScore = ''

    def text_objects(text, font):
        textSurface = font.render(text, True, Color.WHITE.getRGB())
        return textSurface, textSurface.get_rect()

    def button(msg, x, y, w, h, ic, ac, action=None):
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

        # Button text
        smallText = pygame.font.Font(Asset.loadpath('font', 'roboto', 'Roboto-Medium.ttf'), 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        screen.gameDisplay.blit(textSurf, textRect)

    def get_medal(game):
        textScore = ''
        if game == 'diskShooting':
            if score >= 8 and score <= 10:
                medal = Image(Asset.loadpath('homescreen', 'img', 'bronze.png'), [350, 250])
                textScore = 'bronze'
            elif score > 10 and score < 15:
                medal = Image(Asset.loadpath('homescreen', 'img', 'silver.png'), [350, 250])
                textScore = 'silver'
            elif score == 15:
                medal = Image(Asset.loadpath('homescreen', 'img', 'gold.png'), [350, 250])
                textScore = 'gold'
            else:
                return "better luck next time"
        if game == 'hordelopen':
            if score >= 1000 and score <= 1200:
                medal = Image(Asset.loadpath('homescreen', 'img', 'bronze.png'), [350, 250])
                textScore = 'bronze'
            elif score > 1200 and score < 1400:
                medal = Image(Asset.loadpath('homescreen', 'img', 'silver.png'), [350, 250])
                textScore = 'silver'
            elif score >= 1400:
                medal = Image(Asset.loadpath('homescreen', 'img', 'gold.png'), [350, 250])
                textScore = 'gold'
            else:
                return "better luck next time"
        if game == 'zeilen':
            if score == 3 or score == 2:
                medal = Image(Asset.loadpath('homescreen', 'img', 'bronze.png'), [350, 250])
                textScore = 'bronze'
            elif score == 1:
                medal = Image(Asset.loadpath('homescreen', 'img', 'silver.png'), [350, 250])
                textScore = 'silver'
            elif score == 0:
                medal = Image(Asset.loadpath('homescreen', 'img', 'gold.png'), [350, 250])
                textScore = 'gold'
            else:
                return "better luck next time"
        if game == 'skiing':
            if score >= 4 and score <= 7:
                medal = Image(Asset.loadpath('homescreen', 'img', 'bronze.png'), [350, 250])
                textScore = 'bronze'
            elif score > 7 and score < 14:
                medal = Image(Asset.loadpath('homescreen', 'img', 'silver.png'), [350, 250])
                textScore = 'silver'
            elif score >= 14:
                medal = Image(Asset.loadpath('homescreen', 'img', 'gold.png'), [350, 250])
                textScore = 'gold'
            else:
                return "better luck next time"
        if game == 'zwemmen':
            if score < 2000 and score >= 1500:
                medal = Image(Asset.loadpath('homescreen', 'img', 'bronze.png'), [350, 250])
                textScore = 'bronze'
            elif score < 1500 and score >= 1200:
                medal = Image(Asset.loadpath('homescreen', 'img', 'silver.png'), [350, 250])
                textScore = 'silver'
            elif score < 1200:
                medal = Image(Asset.loadpath('homescreen', 'img', 'gold.png'), [350, 250])
                textScore = 'gold'
            else:
                return "better luck next time"
        if game == 'gewichtheffen':
            if score == 1:
                medal = Image(Asset.loadpath('homescreen', 'img', 'bronze.png'), [350, 250])
                textScore = 'bronze'
            elif score == 2:
                medal = Image(Asset.loadpath('homescreen', 'img', 'silver.png'), [350, 250])
                textScore = 'silver'
            elif score == 3:
                medal = Image(Asset.loadpath('homescreen', 'img', 'gold.png'), [350, 250])
                textScore = 'gold'
            else:
                return "better luck next time"

        return [medal, textScore]

    medal_array = get_medal(game)

    if isinstance(medal_array, str):
        medal = medal_array
    else:
        medal = medal_array[0]
        textScore = medal_array[1]

    if game == 'diskShooting':
        background = Image(Asset.loadpath('disk_shooting', 'img', 'background_intro.jpg'), [0, 0])
    if game == 'hordelopen':
        background = Image(Asset.loadpath('hordelopen', 'img', 'background.jpg'), [0, 0])
    if game == 'zeilen':
        background = Image(Asset.loadpath('zeilen', 'img', 'background.jpg'), [0, 0])
    if game == 'skiing':
        background = Image(Asset.loadpath('skiing', 'img', 'background.jpg'), [0, 0])
    if game == 'zwemmen':
        background = Image(Asset.loadpath('zwemmen', 'img', 'background.jpg'), [0, 0])
    if game == 'gewichtheffen':
        background = Image(Asset.loadpath('gewichtheffen', 'img', 'homescherm.jpg'), [0, 0])

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
        screen.gameDisplay.blit(background.image, background.rect)

        largeText = pygame.font.Font(Asset.loadpath('font', 'roboto', 'Roboto-Medium.ttf'), 50)
        TextSurf, TextRect = text_objects("Your score: " + str(score), largeText)
        TextRect.center = ((800 / 2), (600 / 4))
        screen.gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.Font(Asset.loadpath('font', 'roboto', 'Roboto-Medium.ttf'), 50)
        if isinstance(medal, str):
            TextSurf, TextRect = text_objects("Your Medal: " + medal, largeText)
        else:
            TextSurf, TextRect = text_objects("Your Medal: ", largeText)
            screen.gameDisplay.blit(medal.image, medal.rect)

        TextRect.center = ((800 / 2), (600 / 3))
        screen.gameDisplay.blit(TextSurf, TextRect)

        retry_btn = button("Retry", 150, 450, 100, 50, Color.GREEN.getRGB(), Color.DARK_GREEN.getRGB(), game)
        quit_btn = button("Go back", 550, 450, 100, 50, Color.RED.getRGB(), Color.DARK_RED.getRGB(), 'start')

        # Return results of button clicked
        if retry_btn != None:
            return [retry_btn, game, textScore]
        elif quit_btn != None:
            return [quit_btn, game, textScore]
        else:
            pygame.display.update()
            clock.tick(15)
