from enum import Enum

class Color(Enum):
    # Basic colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    # Buttons
    RED = (204, 0, 0)
    DARK_RED = (153, 51, 51)
    GREEN = (51, 204, 51)
    DARK_GREEN = (51, 102, 0)
    # Interface background
    DARK_GREY = (68, 68, 68)

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.rgb = (r, g, b)

    def getRGB(self):
        return self.rgb

    def getColor(self, r, g, b):
        return Color(r, g, b)
