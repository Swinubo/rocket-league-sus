import pygame, easygui, pathlib, DisplStuff

pygame.init()

pygame.display.set_caption("Rocket League Sus in Python")

def FallAnimation(CharacterX, CharacterY):
    OutFallAnimation = False
    while OutFallAnimation == False:
        CharacterY += 20
        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
        if CharacterY > 1000:
            LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
            pygame.display.flip()
            OutFallAnimation = True 
        clock.tick(30)

def LevelDispl(CharacterX, CharacterY, Image):
    DisplStuff.scrn.fill(DisplStuff.WHITE)
    pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(0, 500, 600, 750))
    pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(800, 500, 1850, 750))
    pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(1100, 0, 400, 400))
    DisplStuff.scrn.blit(DisplStuff.HomeDispl, (1650, 0))
    DisplStuff.scrn.blit(Image, (CharacterX, CharacterY))
    pygame.display.flip()

def OutUpCheck(CharacterY):
    if CharacterY < 0:
        return True
    else:
        return False
    
def OutDownCheck(CharacterY):
    if CharacterY > 300:
        return True
    else:
        return False

done = False
clock = pygame.time.Clock()
RealName = 'Guest'
CurrentLevel = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        DisplStuff.scrn.fill(DisplStuff.YELLOW)

        MenuFont = pygame.font.SysFont('timsnewroman',  100)
        LevelMenuDispl = MenuFont.render('Level: ' + str(CurrentLevel), True, DisplStuff.BLACK, DisplStuff.YELLOW)
        NameMenuDispl = MenuFont.render('Name: ' + RealName, True, DisplStuff.BLACK, DisplStuff.YELLOW)
   
        DisplStuff.scrn.blit(DisplStuff.ShopDispl, (0, 150))
        DisplStuff.scrn.blit(DisplStuff.PlayersDispl, (0, 400))
        DisplStuff.scrn.blit(DisplStuff.PlayDispl, (1400, 700))
        DisplStuff.scrn.blit(DisplStuff.LogInDispl, (1350, 10))
        DisplStuff.scrn.blit(DisplStuff.CreateAccountDispl, (1600, 10))
        DisplStuff.scrn.blit(DisplStuff.ExitDispl, (1870, 0))
        DisplStuff.scrn.blit(LevelMenuDispl, (550, 20))
        DisplStuff.scrn.blit(NameMenuDispl, (50, 20))

        pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos

            #Buttons
            if ((x < 201) and (x > 0)):
                if ((y < 351) and (y > 149)):
                    OutShop = False
                    while OutShop == False:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        DisplStuff.scrn.fill(DisplStuff.YELLOW)
                        DisplStuff.scrn.blit(DisplStuff.BoxBlueDispl, (50, 300))
                        DisplStuff.scrn.blit(DisplStuff.BoxRedDispl, (700, 300))
                        DisplStuff.scrn.blit(DisplStuff.BoxYellowDispl, (1300, 300))
                        DisplStuff.scrn.blit(DisplStuff.HomeDispl, (1650, 0))
                        DisplStuff.scrn.blit(DisplStuff.Boxes, (700, 100))
                        pygame.draw.rect(DisplStuff.scrn, DisplStuff.GREEN, pygame.Rect(50, 700, 500, 250))
                        DisplStuff.scrn.blit(DisplStuff.Buy, (130, 750))
                        pygame.draw.rect(DisplStuff.scrn, DisplStuff.GREEN, pygame.Rect(700, 700, 500, 250))
                        DisplStuff.scrn.blit(DisplStuff.Buy, (800, 750))
                        pygame.draw.rect(DisplStuff.scrn, DisplStuff.GREEN, pygame.Rect(1300, 700, 500, 250))
                        DisplStuff.scrn.blit(DisplStuff.Buy, (1400, 750))
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
                        DisplStuff.scrn.fill(DisplStuff.YELLOW)
                        DisplStuff.scrn.blit(DisplStuff.RonaldoDispl, (300, 250))
                        DisplStuff.scrn.blit(DisplStuff.MessiDispl, (800, 250))
                        DisplStuff.scrn.blit(DisplStuff.NeymarDispl, (1300, 250))
                        DisplStuff.scrn.blit(DisplStuff.HomeDispl, (1650, 0))
                        DisplStuff.scrn.blit(DisplStuff.Goats, (700, 100))
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
                        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    CharacterX -= 100
                                    if CharacterX < 0:
                                        CharacterX = 0 
                                    DisplStuff.scrn.blit(DisplStuff.PresidentDispl, (CharacterX, CharacterY))
                                    pygame.display.flip()
                                elif event.key == pygame.K_RIGHT:
                                    CharacterX += 100
                                    DisplStuff.scrn.blit(DisplStuff.PresidentDispl, (CharacterX, CharacterY))
                                    pygame.display.flip()
                                elif event.key == pygame.K_UP:
                                    OutUp = False
                                    OutDown = False

                                    while OutUp == OutUpCheck(CharacterY):
                                        CharacterY -= 20
                                        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_LEFT:
                                                    CharacterX -= 100
                                                    if CharacterX == 1400:
                                                        CharacterX = 1500
                                                        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                                                elif event.key == pygame.K_RIGHT:
                                                    CharacterX += 100
                                                    if CharacterX == 1000:
                                                        CharacterX = 900
                                                        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                                        clock.tick(30)

                                    while OutDown == OutDownCheck(CharacterY):
                                        CharacterY += 20
                                        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_LEFT:
                                                    CharacterX -= 100
                                                    if CharacterX == 1400:
                                                        CharacterX = 1500
                                                        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                                                elif event.key == pygame.K_RIGHT:
                                                    CharacterX += 100
                                                    if CharacterX == 1000:
                                                        CharacterX = 900
                                                        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                                        clock.tick(30)

                                    CharacterY = 300
                                    #clock.tick(30)

                                elif event.key == pygame.K_DOWN:
                                    OutCrouch = False
                                    CharacterY += 100
                                    while OutCrouch == False:
                                        LevelDispl(CharacterX, CharacterY, DisplStuff.CrouchedDispl)
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYUP:
                                                if event.key == pygame.K_DOWN:
                                                    if (CharacterX > 900) and (CharacterX < 1500):
                                                        easygui.msgbox('You can not do that right now! You are crouched!' , 'Warning!')
                                                        CharacterX = 900
                                                        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                                                    OutCrouch = True
                                                    CharacterY -= 100
                                            elif event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_LEFT:
                                                    CharacterX -= 100
                                                    if CharacterX == 600:
                                                        FallAnimation(CharacterX, CharacterY)
                                                        CharacterX = 0
                                                        CharacterY = 300
                                                    elif CharacterX < 0:
                                                        CharacterX = 0
                                                        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                                                if event.key == pygame.K_RIGHT:
                                                    CharacterX += 100
                                                    if CharacterX == 600:
                                                        FallAnimation(CharacterX, CharacterY)
                                                        CharacterX = 0
                                                        CharacterY = 300
                                                    elif CharacterX < 0:
                                                        CharacterX = 0
                                                        LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl, DisplStuff.PresidentDispl)

                            if CharacterX > 1800:
                                LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                                easygui.msgbox('You just beat this level!' , 'Congratulations')
                                CurrentLevel += 1
                                OutPlay = True
                            elif CharacterX == 600:
                                FallAnimation(CharacterX, CharacterY)
                                CharacterX = 0
                                CharacterY = 300
                            elif CharacterX == 1000:
                                CharacterX = 900
                                LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                            elif CharacterX == 1400:
                                CharacterX = 1500
                                LevelDispl(CharacterX, CharacterY, DisplStuff.PresidentDispl)
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                                if ((x < 1851) and (x > 1649) and (y < 201) and (y > 0)):
                                    OutPlay = True
            elif ((x < 1576) and (x > 1349) and (y < 136) and (y > 9)):
                Player = easygui.enterbox("What is your account name?")
                Accounts = open(str(pathlib.Path(DisplStuff.current_dir, 'Accounts.txt')), 'r')
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
                            if Confirmation:
                                CurrentLevel = Level
                                RealName = Name
                            FoundPlayer = True
                        elif Name == 'QNY':
                            if QNYPass == 1:
                                easygui.msgbox('We have not found your account' , 'Account')
                                FoundPlayer = True
                            QNYPass += 1
            elif ((x < 1826) and (x > 1599) and (y < 136) and (y > 9)):
                Name = easygui.enterbox("What is do you want your account name to be?")

                with open(str(pathlib.Path(DisplStuff.current_dir, 'Accounts.txt')), 'a') as Accounts:
                    Accounts.write("\n" + str(CurrentLevel) + ' ' +  Name)
                    Accounts.close()
                easygui.msgbox('Your account has been created succesfully!' , 'Account') 

            elif ((x < 1920) and (x > 1869) and (y < 50) and (y > 0)):
                pygame.quit()
                quit()
        # This limits the while loop to a max of 60 times per second.
        clock.tick(60)

pygame.quit()
quit()