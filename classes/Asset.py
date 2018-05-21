import os

def loadpath(game, type, name):
    path = os.getcwd() + "/assets/" + game + "/" + type + "/" + name
    return path
