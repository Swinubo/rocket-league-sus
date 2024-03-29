import pygame, easygui, pathlib, DisplStuff

pygame.init()

pygame.display.set_caption("Rocket League Sus in Python")

def FallAnimation(CharacterX, CharacterY, Limit):
    OutFallAnimation = False
    while OutFallAnimation == False:
        CharacterY += 20
        LevelDispl(CharacterX, CharacterY, Character)
        if CharacterY > Limit:
            OutFallAnimation = True 
        clock.tick(30)

def LevelDispl(CharacterX, CharacterY, Image):
    if CurrentLevel == 1:
        DisplStuff.scrn.fill(DisplStuff.WHITE)
        pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(0, 500, 600, 750))
        pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(800, 500, 1850, 750))
        pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(1100, 0, 400, 400))
        pygame.draw.polygon(DisplStuff.scrn, DisplStuff.PURPLE, ((1550, 300), (1550, 400), (1700, 400), (1700, 450), (1850, 350), (1700, 250), (1700, 300)))
        DisplStuff.scrn.blit(DisplStuff.HomeDispl, (1650, 0))
        DisplStuff.scrn.blit(Image, (CharacterX, CharacterY))
        DisplStuff.scrn.blit(DisplStuff.Level1Name, (900, 800))
        pygame.display.flip()
    elif CurrentLevel == 2:
        DisplStuff.scrn.fill(DisplStuff.WHITE)
        pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(0, 200, 200, 1800))
        pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(200, 350, 200, 1800))
        pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(400, 500, 200, 1800))
        pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(1100, 0, 400, 600))
        pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(800, 700, 1850, 750))
        pygame.draw.polygon(DisplStuff.scrn, DisplStuff.PURPLE, ((1550, 500), (1550, 600), (1700, 600), (1700, 650), (1850, 550), (1700, 450), (1700, 500)))
        DisplStuff.scrn.blit(DisplStuff.HomeDispl, (1650, 0))
        DisplStuff.scrn.blit(Image, (CharacterX, CharacterY))
        DisplStuff.scrn.blit(DisplStuff.Level2Name, (900, 800))
        if CharacterX > 199:
            pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(0, 0, 200, 1920))
        if CharacterX > 399:
            pygame.draw.rect(DisplStuff.scrn, DisplStuff.BLACK, pygame.Rect(200, 0, 200, 1920))        

        pygame.display.flip()

def Jump(CharacterX, CharacterY, CurrentLevel):

    if (CharacterX < 101) and (CurrentLevel == 2):
        return CharacterX, CharacterY

    OutUp = False
    OutDown = False

    while OutUp == OutUpCheck(CharacterY, CurrentLevel):
        CharacterY -= 20
        LevelDispl(CharacterX, CharacterY, Character)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    CharacterX -= 100
                    CharacterX, CharacterY, CurrentLevel, OutPlay = Limits(CharacterX, CharacterY, CurrentLevel)
                elif event.key == pygame.K_RIGHT:
                    CharacterX += 100
                    CharacterX, CharacterY, CurrentLevel, OutPlay = Limits(CharacterX, CharacterY, CurrentLevel)
        clock.tick(30)

    while OutDown == OutDownCheck(CharacterY, CurrentLevel):
        CharacterY += 20
        LevelDispl(CharacterX, CharacterY, Character)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    CharacterX -= 100
                    CharacterX, CharacterY, CurrentLevel, OutPlay = Limits(CharacterX, CharacterY, CurrentLevel)
                elif event.key == pygame.K_RIGHT:
                    CharacterX += 100
                    CharacterX, CharacterY, CurrentLevel, OutPlay = Limits(CharacterX, CharacterY, CurrentLevel)
        clock.tick(30)
    return CharacterX, CharacterY - 20

def OutUpCheck(CharacterY, CurrentLevel):
    if CurrentLevel == 1:
        if CharacterY < 0:
            return True
        else:
            return False
    elif CurrentLevel == 2:
        if CharacterY < 0:
            return True
        else:
            return False
    
def OutDownCheck(CharacterY, CurrentLevel):
    if CurrentLevel == 1:
        if CharacterY > 300:
            return True
        else:
            return False
    elif CurrentLevel == 2:
        if CharacterY > 500:
            return True
        else:
            return False
    
def Crouch(CharacterX, CharacterY):
    OutCrouch = False
    CharacterY += 100
    while OutCrouch == False:
        LevelDispl(CharacterX, CharacterY, CrouchedDispl)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    if (CharacterX > 900) and (CharacterX < 1500):
                        easygui.msgbox('You can not do that right now! You are crouched!' , 'Warning!')
                        CharacterX = 900
                    OutCrouch = True
                    CharacterY -= 100
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    CharacterX -= 100
                    if CharacterX == 600:
                        FallAnimation(CharacterX, CharacterY, 1000)
                        CharacterX = 0
                        CharacterY = 400
                    elif CharacterX < 0:
                        CharacterX = 0
                if event.key == pygame.K_RIGHT:
                    CharacterX += 100
                    if CharacterX == 600:
                        FallAnimation(CharacterX, CharacterY, 1000)
                        CharacterX = 0
                        CharacterY = 400
                    elif CharacterX < 0:
                        CharacterX = 0
    return CharacterX, CharacterY

def RegKeys(CurrentLevel):
    OutPlay = False
    CharacterX, CharacterY = initXY(CurrentLevel)
    while OutPlay == False:
        LevelDispl(CharacterX, CharacterY, Character)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    CharacterX -= 100
                    if CharacterX < 0:
                        CharacterX = 0 
                    DisplStuff.scrn.blit(Character, (CharacterX, CharacterY))
                    pygame.display.flip()
                elif event.key == pygame.K_RIGHT:
                    CharacterX += 100
                    DisplStuff.scrn.blit(Character, (CharacterX, CharacterY))
                    pygame.display.flip()
                elif event.key == pygame.K_UP:
                    CharacterX, CharacterY = Jump(CharacterX, CharacterY, CurrentLevel)

                elif event.key == pygame.K_DOWN:
                    CharacterX, CharacterY = Crouch(CharacterX, CharacterY)
                    
            CharacterX, CharacterY, CurrentLevel, OutPlay = Limits(CharacterX, CharacterY, CurrentLevel)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ((x < 1851) and (x > 1649) and (y < 201) and (y > 0)):
                    OutPlay = True
    return CharacterX, CharacterY, CurrentLevel

def Limits(CharacterX, CharacterY, CurrentLevel):
    if CurrentLevel == 1:
        if CharacterX > 1800:
            LevelDispl(CharacterX, CharacterY, Character)
            easygui.msgbox('You just beat this level!' , 'Congratulations')
            CurrentLevel += 1
            return CharacterX, CharacterY, CurrentLevel, True
        elif CharacterX == 600:
            if CharacterY == 300:
                FallAnimation(CharacterX, CharacterY, 1000)
                CharacterX = 0
                CharacterY = 300
        elif CharacterX == 1000:
            CharacterX = 900
            LevelDispl(CharacterX, CharacterY, Character)
        elif CharacterX == 1400:
            CharacterX = 1500
            LevelDispl(CharacterX, CharacterY, Character)
        elif CharacterX < 0:
            CharacterX = 0
        return CharacterX, CharacterY, CurrentLevel, False
    elif CurrentLevel == 2:
        if CharacterX > 1800:
            LevelDispl(CharacterX, CharacterY, Character)
            easygui.msgbox('You just beat this level!' , 'Congratulations')
            CurrentLevel += 1
            return CharacterX, CharacterY, CurrentLevel, True
        elif CharacterX == 200:
            FallAnimation(CharacterX, CharacterY, 200)
            CharacterX = 200
            CharacterY = 150
        elif CharacterX == 400:
            FallAnimation(CharacterX, CharacterY, 400)
            CharacterX = 400
            CharacterY = 300
        elif (CharacterX == 600) and ((CharacterY == 300) or (CharacterY == 500)):
            FallAnimation(CharacterX, CharacterY, 1080)
            CharacterX, CharacterY = initXY(CurrentLevel)
        elif (CharacterX == 100) and (CharacterY != 0):
            CharacterX = 200
        elif (CharacterX == 300) and (CharacterY != 350):
            CharacterX = 400
        elif CharacterX < 0:
            CharacterX = 0
        elif CharacterX == 1000:
            CharacterX = 900
            LevelDispl(CharacterX, CharacterY, Character)
        elif CharacterX == 1400:
            CharacterX = 1500
        
        return CharacterX, CharacterY, CurrentLevel, False

    elif CurrentLevel == 3:
        return CharacterX, CharacterY, CurrentLevel, True
    
def initXY(CurrentLevel):
    if CurrentLevel == 1:
        return 0, 300
    elif CurrentLevel == 2:
        return 0, 0
    elif CurrentLevel == 3:
        easygui.msgbox('I unfortunately do not have any more levels programmed :(' , 'Levels')
        return 0, 0
    
def Help():
    easygui.msgbox('Use the left and right to move the character. \n Use the up arrow to jump. \n Use the down arrow to crouch. \n You can change characters when you press on PLAYERS. \n And if you forget any of this, you can press H on the main menu.', 'Help')
        

done = False
clock = pygame.time.Clock()
RealName = 'Guest'
CurrentLevel = 1
Character = DisplStuff.PresidentDispl #Default character stats if none are selected
CrouchedDispl = DisplStuff.CrouchedPresidentDispl #Default character stats if none are selected
MenuDispl = DisplStuff.MenuPresidentDispl #Default character stats if none are selected

Help()

#Main game loop
#Do you think that the code should have more comments?

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        DisplStuff.scrn.fill(DisplStuff.YELLOW)

        MenuFont = pygame.font.SysFont('timsnewroman',  100)
        LevelMenuDispl = MenuFont.render('Level: ' + str(CurrentLevel), True, DisplStuff.BLACK, DisplStuff.YELLOW)
        NameMenuDispl = MenuFont.render('Name: ' + RealName, True, DisplStuff.BLACK, DisplStuff.YELLOW)
   
        DisplStuff.scrn.blit(DisplStuff.HelpDispl, (0, 150))
        DisplStuff.scrn.blit(DisplStuff.PlayersDispl, (0, 400))
        DisplStuff.scrn.blit(DisplStuff.PlayDispl, (1400, 700))
        DisplStuff.scrn.blit(DisplStuff.LogInDispl, (1350, 10))
        DisplStuff.scrn.blit(DisplStuff.CreateAccountDispl, (1600, 10))
        DisplStuff.scrn.blit(DisplStuff.ExitDispl, (1870, 0))
        DisplStuff.scrn.blit(DisplStuff.CreditsDispl, (1870, 60))
        DisplStuff.scrn.blit(MenuDispl, (500, 200))
        DisplStuff.scrn.blit(LevelMenuDispl, (550, 20))
        DisplStuff.scrn.blit(NameMenuDispl, (50, 20))

        pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos

            #Buttons
            if ((x < 201) and (x > 0)):
                if ((y < 351) and (y > 149)):
                    Help()
                elif ((y < 601) and (y > 399)):
                    OutPlayers = False
                    while OutPlayers == False:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        DisplStuff.scrn.fill(DisplStuff.YELLOW)
                        DisplStuff.scrn.blit(DisplStuff.SelectPresidentDispl, (300, 350))
                        DisplStuff.scrn.blit(DisplStuff.SelectPMDispl, (800, 350))
                        DisplStuff.scrn.blit(DisplStuff.SelectMayorDispl, (1300, 350))
                        DisplStuff.scrn.blit(DisplStuff.HomeDispl, (1650, 0))
                        DisplStuff.scrn.blit(DisplStuff.Characters, (600, 100))
                        DisplStuff.scrn.blit(DisplStuff.Use, (375, 760))
                        DisplStuff.scrn.blit(DisplStuff.Use, (850, 760))
                        DisplStuff.scrn.blit(DisplStuff.Use, (1350, 760))
                        pygame.display.flip()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            if ((x < 1851) and (x > 1649) and (y < 201) and (y > 0)):
                                OutPlayers = True
                            elif ((x < 650) and (x > 375) and (y < 900) and (y > 500)):
                                Character = DisplStuff.PresidentDispl
                                CrouchedDispl = DisplStuff.CrouchedPresidentDispl
                                MenuDispl = DisplStuff.MenuPresidentDispl
                                OutPlayers = True
                            elif ((x < 1125) and (x > 850) and (y < 900) and (y > 500)):
                                Character = DisplStuff.PMDispl
                                CrouchedDispl = DisplStuff.CrouchedPMDispl
                                MenuDispl = DisplStuff.MenuPMDispl
                                OutPlayers = True
                            elif ((x < 1625) and (x > 1350) and (y < 900) and (y > 500)):
                                Character = DisplStuff.MayorDispl
                                CrouchedDispl = DisplStuff.CrouchedMayorDispl
                                MenuDispl = DisplStuff.MenuMayorDispl
                                OutPlayers = True
                        clock.tick(60) 
            elif ((x < 1831) and (x > 1399) and (y < 951) and (y > 699)):
                    CharacterX, CharacterY, CurrentLevel = RegKeys(CurrentLevel)
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
                                easygui.msgbox('We have not found your account.' , 'Account')
                                FoundPlayer = True
                            QNYPass += 1
            elif ((x < 1826) and (x > 1599) and (y < 136) and (y > 9)):
                Name = easygui.enterbox("What is do you want your account name to be?")
                
                if Name:
                    with open(str(pathlib.Path(DisplStuff.current_dir, 'Accounts.txt')), 'a') as Accounts:
                        Accounts.write("\n" + str(CurrentLevel) + ' ' +  Name)
                        Accounts.close()
                    easygui.msgbox('Your account has been created succesfully!' , 'Account')
                
                    RealName = Name

            elif ((x < 1920) and (x > 1869) and (y < 50) and (y > 0)):
                pygame.quit()
                quit()
            elif ((x < 1920) and (x > 1869) and (y < 111) and (y > 59)):
                easygui.msgbox('Made by Gaspar Silva Mendes from VMC. All code and images are original.', 'Credits')
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                Help()

        # This limits the while loop to a max of 60 times per second.
        clock.tick(60)

pygame.quit()
quit()