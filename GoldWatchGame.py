import pygame

import tools

actWater = None
water = False
waterCount = 0
def intro():
    global water
    global waterCount
    global actWater

    if actWater:
        win.blit(actWater, (0,0))
        if water == False:
            win.blit(ship[0], (waterCount,150))
        else:
            win.blit(ship[0], (waterCount,146))
        # win.blit(ship[0], (waterCount,150))

    if water and (waterCount % 5 == 0):
        actWater = water1[0]
        win.blit(water1[0], (0,0))
        win.blit(ship[0], (waterCount,150))
        water = False
    elif waterCount % 5 == 0:
        actWater = water2[0]
        win.blit(water2[0], (0,0))
        win.blit(ship[0], (waterCount,146))
        water = True

    if waterCount > 250 and waterCount < 300:
        win.blit(speechBubble[0], (waterCount+30,130))
    waterCount += 1

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("GoldWatch - The Game")

    win = pygame.display.set_mode((500,500))
    clock = pygame.time.Clock()

    # Loading all relevant sprites
    ship = tools.makeSprite("sprites/PirateShip.png", 1)
    pirate1 = tools.makeSprite("sprites/Pirate1_walk.png", 12)
    pirate1Idle = tools.makeSprite("sprites/Pirate1_Idle.png", 6)
    cellar_rattle_roll = tools.makeSprite("sprites/cellar_rattle_roll.png", 3)
    water1 = tools.makeSprite("sprites/waterBG_1.png",1)
    water2 = tools.makeSprite("sprites/waterBG_2.png",1)
    speechBubble = tools.makeSprite("sprites/speech_bubble.png", 1)
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

        win.blit(pirate1Idle[idle], (x,y))
        if idle < 5:
            idle += 1
        else:
            idle = 0
        # pygame.draw.rect(win, (255, 0, 0), (x,y,width,height))
        intro()
        pygame.display.update()

    pygame.quit()
"""
Beim erstellen bzw. anzeigen der Bilder muss auf die Framerate geachtet werden um eine flüssige Animation zu bekommen

"""