import tools

class ENTITY():
    def __init__(self, spritesheet, n = 1, x = 0, y = 0):
        self.sprite = tools.makeSprite(spritesheet, n)
        self.x = x
        self.y = y
    pass

