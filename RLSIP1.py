import pygame

pygame.init()
pygame.font.init()

X = 600
Y = 600
scrn = pygame.display.set_mode((X, Y))

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
PURPLE = (134, 19, 144)
YELLOW = (212, 195, 27)

size = (1850, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rocket League Sus in Python")

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        screen.fill(YELLOW)
        DEFAULT_IMAGE_SIZE = (200, 200)
        BOX_IMAGE_SIZE = (502, 376)
        PLAY_IMAGE_SIZE = (428, 249)
        CARD_IMAGE_SIZE = (300, 450)

        ShopDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Images\\Shop.jpg").convert()
        ShopDispl = pygame.transform.scale(ShopDisp, DEFAULT_IMAGE_SIZE)

        PlayersDisp = pygame.image.load("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Images\\Players.jpg").convert()
        PlayersDispl = pygame.transform.scale(PlayersDisp, DEFAULT_IMAGE_SIZE)
        
        PlayDisp = pygame.image.load("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Images\\Play.jpg").convert()
        PlayDispl = pygame.transform.scale(PlayDisp, PLAY_IMAGE_SIZE)

        HomeDisp = pygame.image.load("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Images\\Home.png").convert()
        HomeDispl = pygame.transform.scale(HomeDisp, DEFAULT_IMAGE_SIZE)

        BoxBlueDisp = pygame.image.load("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Images\\BoxBlue.jpg").convert()
        BoxBlueDispl = pygame.transform.scale(BoxBlueDisp, BOX_IMAGE_SIZE)

        BoxRedDisp = pygame.image.load("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Images\\BoxRed.jpg").convert()
        BoxRedDispl = pygame.transform.scale(BoxRedDisp, BOX_IMAGE_SIZE)

        BoxYellowDisp = pygame.image.load("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Images\\BoxYellow.jpg").convert()
        BoxYellowDispl = pygame.transform.scale(BoxYellowDisp, BOX_IMAGE_SIZE)

        RonaldoDisp = pygame.image.load("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Images\\Ronaldo.png").convert()
        RonaldoDispl = pygame.transform.scale(RonaldoDisp, CARD_IMAGE_SIZE)

        MessiDisp = pygame.image.load("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Images\\Messi.png").convert()
        MessiDispl = pygame.transform.scale(MessiDisp, CARD_IMAGE_SIZE)

        NeymarDisp = pygame.image.load("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Images\\Neymar.png").convert()
        NeymarDispl = pygame.transform.scale(NeymarDisp, CARD_IMAGE_SIZE)

        font=pygame.font.SysFont('Comic Sans M',  200)
        Goats = font.render('GOATS', True, BLACK, YELLOW)
        Boxes = font.render('BOXES', True, BLACK, YELLOW)

        scrn.blit(ShopDispl, (0, 150))
        scrn.blit(PlayersDispl, (0, 400))
        scrn.blit(PlayDispl, (1400, 700))

        pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            
            #print(x, y)

            #Buttons
            if ((x < 201) and (x > 0)):
                if ((y < 351) and (y > 149)):
                    OutShop = False
                    while OutShop == False:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        screen.fill(YELLOW)
                        screen.fill(YELLOW)
                        scrn.blit(BoxBlueDispl, (50, 400))
                        scrn.blit(BoxRedDispl, (700, 400))
                        scrn.blit(BoxYellowDispl, (1300, 400))
                        scrn.blit(HomeDispl, (1650, 0))
                        scrn.blit(Boxes, (700, 100))
                        pygame.display.flip()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            if ((x < 1851) and (x > 1649) and (y < 201) and (y > 0)):
                                OutShop = True
                        clock.tick(60) 
                elif ((y < 601) and (y > 399)):
                    OutPlayers = False
                    while OutPlayers == False:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        screen.fill(YELLOW)
                        scrn.blit(RonaldoDispl, (300, 250))
                        scrn.blit(MessiDispl, (800, 250))
                        scrn.blit(NeymarDispl, (1300, 250))
                        scrn.blit(HomeDispl, (1650, 0))
                        scrn.blit(Goats, (700, 100))
                        pygame.display.flip()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            if ((x < 1851) and (x > 1649) and (y < 201) and (y > 0)):
                                OutPlayers = True
                        clock.tick(60) 
            elif ((x < 1831) and (x > 1399) and (y < 951) and (y > 699)):
                    print('clicked on Play')

        # This limits the while loop to a max of 60 times per second.
        clock.tick(60)

pygame.quit()
quit()
