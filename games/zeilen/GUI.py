import pygame, os
import games.zeilen.Globals as globals
import games.zeilen.Resources as resources
import games.zeilen.GameLogic as logic

main = None

gui_position_main_x = 0
gui_position_main_y = 500

str_line1 = "Bij dit minigame ben je een zeilboot."
str_line2 = "Jou taak is om alle inkomende obstakels te vermijden door de zeilboot te bewegen."
str_line3 = "Je kan de zeilboot met de pijltoetsen bewegen."


class GUI():
    time_minutes = None
    time_seconds = None
    rect_main = None
    surface = None

    kill_effect_ondraw_tick = None
    kill_effect_can_draw = False

    def __init__(self, surf):
        global main
        self.rect_main = pygame.Rect(gui_position_main_x, gui_position_main_y, globals.window_width, 100)
        self.surface = surf
        main = self

    def draw_main(self):
        pygame.draw.rect(self.surface, globals.DARK_GREY, self.rect_main)
        self.draw_text("Times hit", (50,510), globals.WHITE, 20, False)
        if globals.times_hit < 10:
            self.draw_text(str(globals.times_hit), (70, 530), globals.WHITE, 50, False)
        elif globals.times_hit >= 10:
            self.draw_text(str(globals.times_hit), (60, 530), globals.WHITE, 50, False)
        self.draw_text("Times untill finish:", (325, 510), globals.WHITE, 20, False)
        self.draw_text(format_time(), (355, 530), globals.WHITE, 50, False)

        if self.kill_effect_can_draw:
            if pygame.time.get_ticks() - self.kill_effect_ondraw_tick <= 100:
                rect = pygame.Rect(0, 0, globals.window_width, globals.window_height)
                pygame.draw.rect(self.surface, globals.RED, rect)
            else:
                self.kill_effect_ondraw_tick = None
                self.kill_effect_can_draw = False

    def draw_gameover(self):
        keys = pygame.key.get_pressed()

        rect = pygame.Rect(globals.window_width/6, globals.window_height/6, globals.window_width - (2*(globals.window_width / 6)), globals.window_height - (2*(globals.window_height / 6)))
        pygame.draw.rect(self.surface, globals.DARK_GREY, rect)

        self.draw_text("You have reached the Finish!", (rect.x + (rect.x/2), rect.y + (rect.y / 4) + 10),globals.WHITE, 40, False)
        self.draw_text("Times hit:", (rect.x + (rect.width / 2) - 40, rect.y + (rect.height / 2) - 50), globals.WHITE, 30, False)
        if globals.times_hit < 10:
            self.draw_text(str(globals.times_hit), (rect.x + (rect.width / 2), rect.y + (rect.height / 2)), globals.WHITE, 50, False)
        elif globals.times_hit >= 10:
            self.draw_text(str(globals.times_hit), (rect.x + (rect.width / 2) - 25, rect.y + (rect.height / 2)), globals.WHITE, 50, False)
        self.draw_text("Press space to restart!", (rect.x + (rect.x / 2) + 30, rect.y + (rect.y / 4) + 300),globals.WHITE, 40, False)

        if keys[pygame.K_SPACE]:
            logic.restart()

    def draw_intro(self):
        keys = pygame.key.get_pressed()
        rect = pygame.Rect(0, 0, globals.window_width, globals.window_height)
        pygame.draw.rect(self.surface, globals.DARK_GREY, rect)
        self.draw_text("Zeilen", ((globals.window_width / 2) - 95, 25), globals.WHITE, 90, False)
        self.draw_text(str_line1, ((globals.window_width / 2) - 125, 250), globals.WHITE, 20, False)
        self.draw_text(str_line2, (100, 300), globals.WHITE, 20, False)
        self.draw_text(str_line3, (250, 350), globals.WHITE, 20, False)
        self.draw_text("Press space to start!", (275, 500), globals.WHITE, 30, False)

        if keys[pygame.K_SPACE]:
            globals.state = 1

    def draw_text(self, str, pos, color, size, bold):
        fnt = pygame.font.SysFont("arial", size)
        fnt.set_bold(bold)
        label = fnt.render(str, 1, color)
        self.surface.blit(label, pos)


def draw_kill_effect():
    resources.play_sound(resources.sounds["snd_death"])
    main.kill_effect_can_draw = True
    main.kill_effect_ondraw_tick = pygame.time.get_ticks()


def format_time():
    time = globals.timer
    seconds = time // 1000
    minutes = seconds // 60

    seconds_final = (time - ((minutes * 60)*1000)) // 1000
    seconds_str = str(seconds_final)
    if seconds_final < 10:
        seconds_str = "0"+seconds_str
    if (globals.timer > 0):
        return (str(minutes) + ":" + seconds_str)
    elif (globals.timer <= 0):
        return "0:00"
    return (str(minutes) + ":" + seconds_str)


