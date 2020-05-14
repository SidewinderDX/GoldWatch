import pygame

def makeSprite(file, n):
    """
    n = Amount of pictures in the row for animation
    """
    img = pygame.image.load(file)
    orgWidth = img.get_width() // n
    orgHeight = img.get_height()
    img = img.convert_alpha()

    images = []

    frames = pygame.Surface((orgWidth, orgHeight), pygame.SRCALPHA, 32)
    x = 0
    for frame in range(n):
        frames = pygame.Surface((orgWidth, orgHeight), pygame.SRCALPHA, 32)
        frames.blit(img, (x,0))
        images.append(frames.copy())
        x -= orgWidth
    return images