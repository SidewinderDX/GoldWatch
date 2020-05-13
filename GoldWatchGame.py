import pygame
pygame.init()
pygame.display.set_caption("GoldWatch - The Game")

win = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

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



# Loading all relevant sprites
ship = makeSprite("sprites/PirateShip.png", 1)
pirate1 = makeSprite("sprites/Pirate1_walk.png", 12)
pirate1Idle = makeSprite("sprites/Pirate1_Idle.png", 6)
water1 = makeSprite("sprites/waterBG_1.png",1)
water2 = makeSprite("sprites/waterBG_2.png",1)
water = False
waterCount = 0
x = 50
y = 50
width = 40
height = 60
vel = 5
idle = 0
run = True
while run:
    clock.tick(24)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel

    if water and (waterCount % 5 == 0):
        win.blit(water1[0], (0,0))
        win.blit(ship[0], (100,150))
        water = False
    elif waterCount % 5 == 0:
        win.blit(water2[0], (0,0))
        win.blit(ship[0], (100,146))
        water = True

    win.blit(pirate1Idle[idle], (x,y))
    if idle < 5:
        idle += 1
    else:
        idle = 0
    # pygame.draw.rect(win, (255, 0, 0), (x,y,width,height))
    pygame.display.update()
    waterCount += 1

pygame.quit()