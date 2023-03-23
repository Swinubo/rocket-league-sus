import pygame, pathlib, os, pyautogui

pygame.init()

X, Y = pyautogui.size()
scrn = pygame.display.set_mode(size=(X, Y))

current_dir = os.getcwd()
image_path = pathlib.Path(current_dir, 'RLSIP Images')

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 128,   0)
PURPLE = (134, 19, 144)
YELLOW = (212, 195, 27)

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