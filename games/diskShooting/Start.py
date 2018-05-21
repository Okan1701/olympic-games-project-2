import pygame
from games.diskShooting.classes.Person import Person
from games.diskShooting.classes.Disk import Disk
import games.diskShooting.classes.Loop as Loop

class Start():
    def __init__(self, screen):
        self.Active_sprites = pygame.sprite.Group()

        # Start Pygame clock
        self.clock = pygame.time.Clock()
        self.person = Person(screen)

        # Create 1 instance of a disk
        self.disk = Disk(self.person, screen)

        self.SPRITE_GROUP = pygame.sprite.Group()

        self.game_running = True
        # State= intro,game,end
        self.state = 'intro'

    def play(self, screen):
        self.state = 'intro'
        # decorate game window
        pygame.display.set_caption('Olympische Spelen - Diskshooting')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                    break
            if self.state == 'intro':
                self.person.reset()
                self.disk.hard_reset(self.person)
                screen.defaultCursor()
                result = Loop.game_intro(screen)
                if result == None:
                    break
                else:
                    self.state = result
            elif self.state == 'game':
                screen.hideCursor()
                self.person.reset()
                self.disk.hard_reset(self.person)
                result = Loop.game_loop(screen, self.disk, self.person)
                if result == None:
                    break
                else:
                    self.state = result
            elif self.state == 'end':
                self.state = 'intro'
                return ['score', 'diskShooting', self.person.score]
            elif self.state == 'quit':
                pygame.display.quit()
                pygame.quit()
            elif self.state == 'return':
                return 'start'

            pygame.display.update()
            self.clock.tick(60)

        pygame.display.quit()
        pygame.quit()
