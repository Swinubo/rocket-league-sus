import pygame, easygui, pathlib, os

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

current_dir = os.getcwd()
print(current_dir)
image_path = pathlib.Path(current_dir, 'Documents', 'Gaspar', 'Python Projects', 'Images')
reg_path = pathlib.Path(current_dir, 'Documents', 'Gaspar', 'Python Projects')


def FallAnimation(CharacterX, CharacterY):
    OutFallAnimation = False
    while OutFallAnimation == False:
        CharacterY += 20
        LevelDispl(CharacterX, CharacterY)
        if CharacterY > 1000:
            LevelDispl(CharacterX, CharacterY)
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
        RECT_IMAGE_SIZE = (225, 125)
        CARD_IMAGE_SIZE = (300, 450)
        CROUCH_IMAGE_SIZE = (200, 100)

        ShopDisp = pygame.image.load(str(pathlib.Path(image_path, "Shop.jpg"))).convert()
        ShopDispl = pygame.transform.scale(ShopDisp, DEFAULT_IMAGE_SIZE)

        PlayersDisp = pygame.image.load(str(pathlib.Path(image_path, "Players.jpg"))).convert()
        PlayersDispl = pygame.transform.scale(PlayersDisp, DEFAULT_IMAGE_SIZE)
        
        PlayDisp = pygame.image.load(str(pathlib.Path(image_path, "Play.jpg"))).convert()
        PlayDispl = pygame.transform.scale(PlayDisp, PLAY_IMAGE_SIZE)

        HomeDisp = pygame.image.load(str(pathlib.Path(image_path, "Home.png"))).convert()
        HomeDispl = pygame.transform.scale(HomeDisp, DEFAULT_IMAGE_SIZE)

        BoxBlueDisp = pygame.image.load(str(pathlib.Path(image_path, "BoxBlue.jpg"))).convert()
        BoxBlueDispl = pygame.transform.scale(BoxBlueDisp, BOX_IMAGE_SIZE)

        BoxRedDisp = pygame.image.load(str(pathlib.Path(image_path, "BoxRed.jpg"))).convert()
        BoxRedDispl = pygame.transform.scale(BoxRedDisp, BOX_IMAGE_SIZE)

        BoxYellowDisp = pygame.image.load(str(pathlib.Path(image_path, "BoxYellow.jpg"))).convert()
        BoxYellowDispl = pygame.transform.scale(BoxYellowDisp, BOX_IMAGE_SIZE)

        RonaldoDisp = pygame.image.load(str(pathlib.Path(image_path, "Ronaldo.png"))).convert()
        RonaldoDispl = pygame.transform.scale(RonaldoDisp, CARD_IMAGE_SIZE)

        MessiDisp = pygame.image.load(str(pathlib.Path(image_path, "Messi.png"))).convert()
        MessiDispl = pygame.transform.scale(MessiDisp, CARD_IMAGE_SIZE)

        NeymarDisp = pygame.image.load(str(pathlib.Path(image_path, "Neymar.png"))).convert()
        NeymarDispl = pygame.transform.scale(NeymarDisp, CARD_IMAGE_SIZE)

        PresidentDisp = pygame.image.load(str(pathlib.Path(image_path, "President.jpg"))).convert()
        PresidentDispl = pygame.transform.scale(PresidentDisp, DEFAULT_IMAGE_SIZE)
        CrouchedDispl = pygame.transform.scale(PresidentDisp, CROUCH_IMAGE_SIZE)

        LogInDisp = pygame.image.load(str(pathlib.Path(image_path, "LogIn.png"))).convert()
        LogInDispl = pygame.transform.scale(LogInDisp, RECT_IMAGE_SIZE)

        CreateAccountDisp = pygame.image.load(str(pathlib.Path(image_path, "CreateAccount.png"))).convert()
        CreateAccountDispl = pygame.transform.scale(CreateAccountDisp, RECT_IMAGE_SIZE)

        font = pygame.font.SysFont('Comic Sans M',  200)
        Goats = font.render('GOATS', True, BLACK, YELLOW)
        Boxes = font.render('BOXES', True, BLACK, YELLOW)
        Buy = font.render('BUY', True, BLACK, GREEN)

        Level = 0

        scrn.blit(ShopDispl, (0, 150))
        scrn.blit(PlayersDispl, (0, 400))
        scrn.blit(PlayDispl, (1400, 700))
        scrn.blit(LogInDispl, (1350, 10))
        scrn.blit(CreateAccountDispl, (1600, 10))

        pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            
            print(x, y)

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
                                                        easygui.msgbox('You can not do that right now! You are crouched!' , 'Warning!')
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
                                easygui.msgbox('You just beat this level!' , 'Congratulations')
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
            elif ((x < 1576) and (x > 1349) and (y < 136) and (y > 9)):
                Player = easygui.enterbox("What is your account name?")
                Accounts = open(str(pathlib.Path(reg_path, 'Accounts.txt')), 'r')
                AccountsR = Accounts.readlines()
                AccountList = []
                LevelList = []
                QNYPass = -1
                FoundPlayer = False

                while FoundPlayer == False:
                    if Player == '':
                        break
                    for line in AccountsR:
                        Name = line[2:]
                        Name = Name.strip()
                        Level = line[:1]
                        AccountList.append(Name)
                        LevelList.append(Level)
                        if Name == Player:
                            easygui.msgbox('We have found your account! You are on level ' + Level + ' and your name is ' + Name + '.' , 'Account')
                            Confirmation = easygui.ynbox('Are you sure you want to load this account?' , 'Loading Accounts')
                            #yes no if goes here
                            FoundPlayer = True
                        elif Name == 'QNY':
                            if QNYPass == 1:
                                easygui.msgbox('We have not found your account' , 'Account')
                                FoundPlayer = True
                            QNYPass += 1
            elif ((x < 1826) and (x > 1599) and (y < 136) and (y > 9)):
                Name = easygui.enterbox("What is do you want your account name to be?")

                with open(str(pathlib.Path(reg_path, 'Accounts.txt')), 'a') as Accounts:
                    Accounts.write("\n" + str(Level) + ' ' + Name)
                    Accounts.close()
                easygui.msgbox('Your account has been created succesfully!' , 'Account') 
        
        # This limits the while loop to a max of 60 times per second.
        clock.tick(60)

pygame.quit()
quit()