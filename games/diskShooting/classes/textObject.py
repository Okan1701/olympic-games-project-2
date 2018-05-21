class textObject():
    def textObjects(self, text, font, color, pos_x, pos_y):
        textSurface = font.render(text, True, color)
        textSurface.get_rect().center = (pos_x, pos_y)
        return textSurface, textSurface.get_rect()