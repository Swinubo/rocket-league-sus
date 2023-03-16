import pygame
from tkinter import *
from tkinter import messagebox

window = Tk()
window.eval('tk::PlaceWindow %s Center' % window.winfo_toplevel())

pygame.init()
pygame.font.init()

X = 1850
Y = 1000
scrn = pygame.display.set_mode((X, Y))

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 128,   0)
PURPLE = (134, 19, 144)
YELLOW = (212, 195, 27)

size = (1850, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rocket League Sus in Python")

def FallAnimation(CharacterX, CharacterY):
    OutFallAnimation = False
    while OutFallAnimation == False:
        CharacterY += 20
        LevelDispl(CharacterX, CharacterY)
        if CharacterY > 1000:
            screen.fill(WHITE)
            pygame.draw.rect(scrn, BLACK, pygame.Rect(0, 500, 600, 750))
            pygame.draw.rect(scrn, BLACK, pygame.Rect(800, 500, 1850, 750))
            pygame.draw.rect(scrn, BLACK, pygame.Rect(1100, 0, 400, 400))
            scrn.blit(HomeDispl, (1650, 0))
            scrn.blit(PresidentDispl, (0, 300))
            pygame.display.flip()
            OutFallAnimation = True 
        clock.tick(30)

def LevelDispl(CharacterX, CharacterY):
    screen.fill(WHITE)
    pygame.draw.rect(scrn, BLACK, pygame.Rect(0, 500, 600, 750))
    pygame.draw.rect(scrn, BLACK, pygame.Rect(800, 500, 1850, 750))
    pygame.draw.rect(scrn, BLACK, pygame.Rect(1100, 0, 400, 400))
    scrn.blit(HomeDispl, (1650, 0))
    scrn.blit(PresidentDispl, (CharacterX, CharacterY))
    pygame.display.flip()

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
        CROUCH_IMAGE_SIZE = (200, 100)

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

        PresidentDisp = pygame.image.load("C:\\Users\\fmend\\Documents\\Gaspar\\Python Projects\\Images\\President.jpg").convert()
        PresidentDispl = pygame.transform.scale(PresidentDisp, DEFAULT_IMAGE_SIZE)
        CrouchedDispl = pygame.transform.scale(PresidentDisp, CROUCH_IMAGE_SIZE)

        font = pygame.font.SysFont('Comic Sans M',  200)
        Goats = font.render('GOATS', True, BLACK, YELLOW)
        Boxes = font.render('BOXES', True, BLACK, YELLOW)
        Buy = font.render('BUY', True, BLACK, GREEN)


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
                        scrn.blit(BoxBlueDispl, (50, 300))
                        scrn.blit(BoxRedDispl, (700, 300))
                        scrn.blit(BoxYellowDispl, (1300, 300))
                        scrn.blit(HomeDispl, (1650, 0))
                        scrn.blit(Boxes, (700, 100))
                        pygame.draw.rect(scrn, GREEN, pygame.Rect(50, 700, 500, 250))
                        scrn.blit(Buy, (130, 750))
                        pygame.draw.rect(scrn, GREEN, pygame.Rect(700, 700, 500, 250))
                        scrn.blit(Buy, (800, 750))
                        pygame.draw.rect(scrn, GREEN, pygame.Rect(1300, 700, 500, 250))
                        scrn.blit(Buy, (1400, 750))
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
                    OutPlay = False
                    CharacterX = 0
                    CharacterY = 300
                    while OutPlay == False:
                        LevelDispl(CharacterX, CharacterY)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            screen.fill(WHITE)
                            pygame.draw.rect(scrn, BLACK, pygame.Rect(0, 500, 600, 750))
                            pygame.draw.rect(scrn, BLACK, pygame.Rect(800, 500, 1850, 750))
                            scrn.blit(HomeDispl, (1650, 0))
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    CharacterX -= 100
                                    if CharacterX < 0:
                                        CharacterX = 0 
                                    scrn.blit(PresidentDispl, (CharacterX, CharacterY))
                                    pygame.display.flip()
                                elif event.key == pygame.K_RIGHT:
                                    CharacterX += 100
                                    scrn.blit(PresidentDispl, (CharacterX, CharacterY))
                                    pygame.display.flip()
                                elif event.key == pygame.K_UP:
                                    OutJumpAnimation = False
                                    OutUp = False
                                    OutDown = False

                                    while OutJumpAnimation == False:
                                        while OutUp == False:
                                            CharacterY -= 20
                                            LevelDispl(CharacterX, CharacterY)
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_LEFT:
                                                        CharacterX -= 100
                                                        if CharacterX == 1400:
                                                            CharacterX = 1500
                                                            LevelDispl(CharacterX, CharacterY)
                                                    elif event.key == pygame.K_RIGHT:
                                                        CharacterX += 100
                                                        if CharacterX == 1000:
                                                            CharacterX = 900
                                                        LevelDispl(CharacterX, CharacterY)
                                            clock.tick(30)

                                            if CharacterY < 0:
                                                OutUp = True
                                        
                                        while OutDown == False:
                                            CharacterY += 20
                                            LevelDispl(CharacterX, CharacterY)
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_LEFT:
                                                        CharacterX -= 100
                                                        if CharacterX == 1400:
                                                            CharacterX = 1500
                                                            LevelDispl(CharacterX, CharacterY)
                                                    elif event.key == pygame.K_RIGHT:
                                                        CharacterX += 100
                                                        if CharacterX == 1000:
                                                            CharacterX = 900
                                                            LevelDispl(CharacterX, CharacterY)
                                            clock.tick(30)

                                            if CharacterY > 300:
                                                OutDown = True
                                                CharacterY = 300
                                        OutJumpAnimation = True
                                        clock.tick(30)

                                elif event.key == pygame.K_DOWN:
                                    OutCrouch = False
                                    while OutCrouch == False:
                                        screen.fill(WHITE)
                                        pygame.draw.rect(scrn, BLACK, pygame.Rect(0, 500, 600, 750))
                                        pygame.draw.rect(scrn, BLACK, pygame.Rect(800, 500, 1850, 750))
                                        pygame.draw.rect(scrn, BLACK, pygame.Rect(1100, 0, 400, 400))
                                        scrn.blit(HomeDispl, (1650, 0))
                                        scrn.blit(CrouchedDispl, (CharacterX, CharacterY + 100))
                                        pygame.display.flip()
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYUP:
                                                if event.key == pygame.K_DOWN:
                                                    if (CharacterX > 900) and (CharacterX < 1500):
                                                        messagebox.showwarning('Warning!', 'You can not do that right now! You are crouched!')
                                                        CharacterX = 900
                                                        LevelDispl(CharacterX, CharacterY)
                                                    OutCrouch = True
                                            elif event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_LEFT:
                                                    CharacterX -= 100
                                                    if CharacterX == 600:
                                                        FallAnimation(CharacterX, CharacterY)
                                                        CharacterX = 0
                                                        CharacterY = 300
                                                    elif CharacterX < 0:
                                                        CharacterX = 0
                                                        LevelDispl(CharacterX, CharacterY)
                                                if event.key == pygame.K_RIGHT:
                                                    CharacterX += 100
                                                    if CharacterX == 600:
                                                        FallAnimation(CharacterX, CharacterY)
                                                        CharacterX = 0
                                                        CharacterY = 300
                                                    elif CharacterX < 0:
                                                        CharacterX = 0
                                                        LevelDispl(CharacterX, CharacterY)

                            if CharacterX > 1800:
                                LevelDispl(CharacterX, CharacterY)
                                messagebox.showinfo('Congratulations', 'You just beat this level!')
                                OutPlay = True
                            elif CharacterX == 600:
                                FallAnimation(CharacterX, CharacterY)
                                CharacterX = 0
                                CharacterY = 300
                            elif CharacterX == 1000:
                                CharacterX = 900
                                LevelDispl(CharacterX, CharacterY)
                            elif CharacterX == 1400:
                                CharacterX = 1500
                                LevelDispl(CharacterX, CharacterY)
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                                if ((x < 1851) and (x > 1649) and (y < 201) and (y > 0)):
                                    OutPlay = True

        # This limits the while loop to a max of 60 times per second.
        clock.tick(60)

pygame.quit()
quit()
