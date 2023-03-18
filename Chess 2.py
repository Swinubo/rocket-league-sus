import pygame

pygame.init()

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
pygame.display.set_caption("Chess 2")

DEFAULT_IMAGE_SIZE = (80, 80)

PawnDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\pawn.png").convert()
PawnDispl = pygame.transform.scale(PawnDisp, DEFAULT_IMAGE_SIZE)

Pawn1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\pawn1.png").convert()
Pawn1Displ = pygame.transform.scale(Pawn1Disp, DEFAULT_IMAGE_SIZE)

KnightDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\knight.png").convert()
KnightDispl = pygame.transform.scale(KnightDisp, DEFAULT_IMAGE_SIZE)

Knight1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\knight1.png").convert()
Knight1Displ = pygame.transform.scale(Knight1Disp, DEFAULT_IMAGE_SIZE)

BishopDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\bishop.png").convert()
BishopDispl = pygame.transform.scale(BishopDisp, DEFAULT_IMAGE_SIZE)

Bishop1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\bishop1.png").convert()
Bishop1Displ = pygame.transform.scale(Bishop1Disp, DEFAULT_IMAGE_SIZE)

RookDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\rook.png").convert()
RookDispl = pygame.transform.scale(RookDisp, DEFAULT_IMAGE_SIZE)

Rook1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\rook1.png").convert()
Rook1Displ = pygame.transform.scale(Rook1Disp, DEFAULT_IMAGE_SIZE)

KingDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\king.png").convert()
KingDispl = pygame.transform.scale(KingDisp, DEFAULT_IMAGE_SIZE)

King1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\king1.png").convert()
King1Displ = pygame.transform.scale(King1Disp, DEFAULT_IMAGE_SIZE)

QueenDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\queen.png").convert()
QueenDispl = pygame.transform.scale(QueenDisp, DEFAULT_IMAGE_SIZE)

Queen1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\queen1.png").convert()
Queen1Displ = pygame.transform.scale(Queen1Disp, DEFAULT_IMAGE_SIZE)

fontPieces = pygame.font.SysFont('Comic Sans M',  200)
WhiteBlack = fontPieces.render('White pieces captured by black', True, BLACK, GREEN)
BlackWhite = fontPieces.render('Black pieces captured by white', True, BLACK, GREEN)

fontLetter = pygame.font.SysFont('Comic Sans M',  50)
a = fontLetter.render('a', True, BLACK, GREEN)
b = fontLetter.render('b', True, BLACK, GREEN)

def Board():
    InitBoardX = 475
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX, 50, 100, 100)) #a8
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX, 150, 100, 100)) #a7
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX, 250, 100, 100)) #a6
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX, 350, 100, 100)) #a5
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX, 450, 100, 100)) #a4
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX, 550, 100, 100)) #a3
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX, 650, 100, 100)) #a2
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX, 750, 100, 100)) #a1

    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 100, 50, 100, 100)) #b8
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 100, 150, 100, 100)) #b7
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 100, 250, 100, 100)) #b6
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 100, 350, 100, 100)) #b5
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 100, 450, 100, 100)) #b4
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 100, 550, 100, 100)) #b3
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 100, 650, 100, 100)) #b2
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 100, 750, 100, 100)) #b1

    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 200, 50, 100, 100)) #c8
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 200, 150, 100, 100)) #c7
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 200, 250, 100, 100)) #c6
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 200, 350, 100, 100)) #c5
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 200, 450, 100, 100)) #c4
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 200, 550, 100, 100)) #c3
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 200, 650, 100, 100)) #c2
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 200, 750, 100, 100)) #c1

    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 300, 50, 100, 100)) #d8
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 300, 150, 100, 100)) #d7
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 300, 250, 100, 100)) #d6
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 300, 350, 100, 100)) #d5
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 300, 450, 100, 100)) #d4
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 300, 550, 100, 100)) #d3
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 300, 650, 100, 100)) #d2
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 300, 750, 100, 100)) #d1

    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 400, 50, 100, 100)) #e8
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 400, 150, 100, 100)) #e7
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 400, 250, 100, 100)) #e6
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 400, 350, 100, 100)) #e5
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 400, 450, 100, 100)) #e4
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 400, 550, 100, 100)) #e3
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 400, 650, 100, 100)) #e2
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 400, 750, 100, 100)) #e1    

    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 500, 50, 100, 100)) #f8
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 500, 150, 100, 100)) #f7
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 500, 250, 100, 100)) #f6
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 500, 350, 100, 100)) #f5
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 500, 450, 100, 100)) #f4
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 500, 550, 100, 100)) #f3
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 500, 650, 100, 100)) #f2
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 500, 750, 100, 100)) #f1

    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 600, 50, 100, 100)) #g8
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 600, 150, 100, 100)) #g7
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 600, 250, 100, 100)) #g6
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 600, 350, 100, 100)) #g5
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 600, 450, 100, 100)) #g4
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 600, 550, 100, 100)) #g3
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 600, 650, 100, 100)) #g2
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 600, 750, 100, 100)) #g1

    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 700, 50, 100, 100)) #h8
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 700, 150, 100, 100)) #h7
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 700, 250, 100, 100)) #h6
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 700, 350, 100, 100)) #h5
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 700, 450, 100, 100)) #h4
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 700, 550, 100, 100)) #h3
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 700, 650, 100, 100)) #h2
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 700, 750, 100, 100)) #h1

    pygame.display.flip()

def AllPieces():
    PawnA2(PawnA2x, PawnA2y)
    PawnB2(PawnB2x, PawnB2y)
    PawnC2(PawnC2x, PawnC2y)
    PawnD2(PawnD2x, PawnD2y)
    PawnE2(PawnE2x, PawnE2y)
    PawnF2(PawnF2x, PawnF2y)
    PawnG2(PawnG2x, PawnG2y)
    PawnH2(PawnH2x, PawnH2y)
    Pawn1A7(Pawn1A7x, Pawn1A7y)
    Pawn1B7(Pawn1B7x, Pawn1B7y)
    Pawn1C7(Pawn1C7x, Pawn1C7y)
    Pawn1D7(Pawn1D7x, Pawn1D7y)
    Pawn1E7(Pawn1E7x, Pawn1E7y)
    Pawn1F7(Pawn1F7x, Pawn1F7y)
    Pawn1G7(Pawn1G7x, Pawn1G7y)
    Pawn1H7(Pawn1H7x, Pawn1H7y)
    KnightB1(KnightB1x, KnightB1y)
    KnightG1(KnightG1x, KnightG1y)
    Knight1B8(Knight1B8x, Knight1B8y)
    Knight1G8(Knight1G8x, Knight1G8y)
    BishopC1(BishopC1x, BishopC1y)
    BishopF1(BishopF1x, BishopF1y)
    Bishop1C8(Bishop1C8x, Bishop1C8y)
    Bishop1F8(Bishop1F8x, Bishop1F8y)
    RookA1(RookA1x, RookA1y)
    RookH1(RookH1x, RookH1y)
    Rook1A8(Rook1A8x, Rook1A8y)
    Rook1H8(Rook1H8x, Rook1H8y)
    King(Kingx, Kingy)
    King1(King1x, King1y)
    Queen(Queenx, Queeny)
    Queen1(Queen1x, Queen1y)

def PawnA2(PawnA2x, PawnA2y):
    scrn.blit(PawnDispl, (PawnA2x, PawnA2y))
    pygame.display.flip()

def PawnB2(PawnB2x, PawnB2y):
    scrn.blit(PawnDispl, (PawnB2x, PawnB2y))
    pygame.display.flip()

def PawnC2(PawnC2x, PawnC2y):
    scrn.blit(PawnDispl, (PawnC2x, PawnC2y))
    pygame.display.flip()

def PawnD2(PawnD2x, PawnD2y):
    scrn.blit(PawnDispl, (PawnD2x, PawnD2y))
    pygame.display.flip()

def PawnE2(PawnE2x, PawnE2y):
    scrn.blit(PawnDispl, (PawnE2x, PawnE2y))
    pygame.display.flip()

def PawnF2(PawnF2x, PawnF2y):
    scrn.blit(PawnDispl, (PawnF2x, PawnF2y))
    pygame.display.flip()

def PawnG2(PawnG2x, PawnG2y):
    scrn.blit(PawnDispl, (PawnG2x, PawnG2y))
    pygame.display.flip()

def PawnH2(PawnH2x, PawnH2y):
    scrn.blit(PawnDispl, (PawnH2x, PawnH2y))
    pygame.display.flip()

def Pawn1A7(Pawn1A7x, Pawn1A7y):
    scrn.blit(Pawn1Displ, (Pawn1A7x, Pawn1A7y))
    pygame.display.flip()

def Pawn1B7(Pawn1B7x, Pawn1B7y):
    scrn.blit(Pawn1Displ, (Pawn1B7x, Pawn1B7y))
    pygame.display.flip()

def Pawn1C7(Pawn1C7x, Pawn1C7y):
    scrn.blit(Pawn1Displ, (Pawn1C7x, Pawn1C7y))
    pygame.display.flip()

def Pawn1D7(Pawn1D7x, Pawn1D7y):
    scrn.blit(Pawn1Displ, (Pawn1D7x, Pawn1D7y))
    pygame.display.flip()

def Pawn1E7(Pawn1E7x, Pawn1E7y):
    scrn.blit(Pawn1Displ, (Pawn1E7x, Pawn1E7y))
    pygame.display.flip()

def Pawn1F7(Pawn1F7x, Pawn1F7y):
    scrn.blit(Pawn1Displ, (Pawn1F7x, Pawn1F7y))
    pygame.display.flip()

def Pawn1G7(Pawn1G7x, Pawn1G7y):
    scrn.blit(Pawn1Displ, (Pawn1G7x, Pawn1G7y))
    pygame.display.flip()

def Pawn1H7(Pawn1H7x, Pawn1H7y):
    scrn.blit(Pawn1Displ, (Pawn1H7x, Pawn1H7y))
    pygame.display.flip()

def KnightB1(KnightB1x, KnightB1y):
    scrn.blit(KnightDispl, (KnightB1x, KnightB1y))
    pygame.display.flip()

def KnightG1(KnightG1x, KnightG1y):
    scrn.blit(KnightDispl, (KnightG1x, KnightG1y))
    pygame.display.flip()

def Knight1B8(Knight1B8x, Knight1B8y):
    scrn.blit(Knight1Displ, (Knight1B8x, Knight1B8y))
    pygame.display.flip()

def Knight1G8(Knight1G8x, Knight1G8y):
    scrn.blit(Knight1Displ, (Knight1G8x, Knight1G8y))
    pygame.display.flip()

def BishopC1(BishopC1x, BishopC1y):
    scrn.blit(BishopDispl, (BishopC1x, BishopC1y))
    pygame.display.flip()

def BishopF1(BishopF1x, BishopF1y):
    scrn.blit(BishopDispl, (BishopF1x, BishopF1y))
    pygame.display.flip()

def Bishop1C8(Bishop1C8x, Bishop1C8y):
    scrn.blit(Bishop1Displ, (Bishop1C8x, Bishop1C8y))
    pygame.display.flip()

def Bishop1F8(Bishop1F8x, Bishop1F8y):
    scrn.blit(Bishop1Displ, (Bishop1F8x, Bishop1F8y))
    pygame.display.flip()

def RookA1(RookA1x, RookA1y):
    scrn.blit(RookDispl, (RookA1x, RookA1y))
    pygame.display.flip()

def RookH1(RookH1x, RookH1y):
    scrn.blit(RookDispl, (RookH1x, RookH1y))
    pygame.display.flip()

def Rook1A8(Rook1A8x, Rook1A8y):
    scrn.blit(Rook1Displ, (Rook1A8x, Rook1A8y))
    pygame.display.flip()

def Rook1H8(Rook1H8x, Rook1H8y):
    scrn.blit(Rook1Displ, (Rook1H8x, Rook1H8y))
    pygame.display.flip()

def King(Kingx, Kingy):
    scrn.blit(KingDispl, (Kingx, Kingy))
    pygame.display.flip()

def King1(King1x, King1y):
    scrn.blit(King1Displ, (King1x, King1y))
    pygame.display.flip()

def Queen(Queenx, Queeny):
    scrn.blit(QueenDispl, (Queenx, Queeny))
    pygame.display.flip()    

def Queen1(Queen1x, Queen1y):
    scrn.blit(Queen1Displ, (Queen1x, Queen1y))
    pygame.display.flip()

done = False
clock = pygame.time.Clock()

PawnA2x, PawnA2y = 490, 650
PawnB2x, PawnB2y = 590, 650
PawnC2x, PawnC2y = 690, 650
PawnD2x, PawnD2y = 790, 650
PawnE2x, PawnE2y = 890, 650
PawnF2x, PawnF2y = 990, 650
PawnG2x, PawnG2y = 1090, 650
PawnH2x, PawnH2y = 1190, 650
Pawn1A7x, Pawn1A7y = 490, 150
Pawn1B7x, Pawn1B7y = 590, 150
Pawn1C7x, Pawn1C7y = 690, 150
Pawn1D7x, Pawn1D7y = 790, 150
Pawn1E7x, Pawn1E7y = 890, 150
Pawn1F7x, Pawn1F7y = 990, 150
Pawn1G7x, Pawn1G7y = 1090, 150
Pawn1H7x, Pawn1H7y = 1190, 150

KnightB1x, KnightB1y = 590, 750
KnightG1x, KnightG1y = 1090, 750
Knight1B8x, Knight1B8y = 590, 50
Knight1G8x, Knight1G8y = 1090, 50

BishopC1x, BishopC1y = 690, 750
BishopF1x, BishopF1y = 990, 750
Bishop1C8x, Bishop1C8y = 690, 50
Bishop1F8x, Bishop1F8y = 990, 50

RookA1x, RookA1y = 490, 750
RookH1x, RookH1y = 1190, 750
Rook1A8x, Rook1A8y = 490, 50
Rook1H8x, Rook1H8y = 1190, 50

Kingx, Kingy = 890, 750
King1x, King1y = 890, 50

Queenx, Queeny = 790, 750
Queen1x, Queen1y = 790, 50

screen.fill(GREEN)
Board()
AllPieces()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if ((x < PawnA2x + 100) and (x > PawnA2x) and (y < PawnA2y + 100) and (y > PawnA2y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            PawnA2(x, y)
                            PawnA2x, PawnA2y = x, y
                            PieceDropped = True

            elif ((x < PawnB2x + 100) and (x > PawnB2x) and (y < PawnB2y + 100) and (y > PawnB2y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            PawnB2(x, y)
                            PawnB2x, PawnB2y = x, y
                            PieceDropped = True
            elif ((x < PawnC2x + 100) and (x > PawnC2x) and (y < PawnC2y + 100) and (y > PawnC2y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            PawnC2(x, y)
                            PawnC2x, PawnC2y = x, y
                            PieceDropped = True
            elif ((x < PawnD2x + 100) and (x > PawnD2x) and (y < PawnD2y + 100) and (y > PawnD2y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            PawnD2(x, y)
                            PawnD2x, PawnD2y = x, y
                            PieceDropped = True
            elif ((x < PawnE2x + 100) and (x > PawnE2x) and (y < PawnE2y + 100) and (y > PawnE2y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            PawnE2(x, y)
                            PawnE2x, PawnE2y = x, y
                            PieceDropped = True
            elif ((x < PawnF2x + 100) and (x > PawnF2x) and (y < PawnF2y + 100) and (y > PawnF2y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            PawnF2(x, y)
                            PawnF2x, PawnF2y = x, y
                            PieceDropped = True
            elif ((x < PawnG2x + 100) and (x > PawnG2x) and (y < PawnG2y + 100) and (y > PawnG2y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            PawnG2(x, y)
                            PawnG2x, PawnG2y = x, y
                            PieceDropped = True
            elif ((x < PawnH2x + 100) and (x > PawnH2x) and (y < PawnH2y + 100) and (y > PawnH2y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            PawnH2(x, y)
                            PawnH2x, PawnH2y = x, y
                            PieceDropped = True
            if ((x < Pawn1A7x + 100) and (x > Pawn1A7x) and (y < Pawn1A7y + 100) and (y > Pawn1A7y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Pawn1A7(x, y)
                            Pawn1A7x, Pawn1A7y = x, y
                            PieceDropped = True

            elif ((x < Pawn1B7x + 100) and (x > Pawn1B7x) and (y < Pawn1B7y + 100) and (y > Pawn1B7y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Pawn1B7(x, y)
                            Pawn1B7x, Pawn1B7y = x, y
                            PieceDropped = True
            elif ((x < Pawn1C7x + 100) and (x > Pawn1C7x) and (y < Pawn1C7y + 100) and (y > Pawn1C7y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Pawn1C7(x, y)
                            Pawn1C7x, Pawn1C7y = x, y
                            PieceDropped = True
            elif ((x < Pawn1D7x + 100) and (x > Pawn1D7x) and (y < Pawn1D7y + 100) and (y > Pawn1D7y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Pawn1D7(x, y)
                            Pawn1D7x, Pawn1D7y = x, y
                            PieceDropped = True
            elif ((x < Pawn1E7x + 100) and (x > Pawn1E7x) and (y < Pawn1E7y + 100) and (y > Pawn1E7y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Pawn1E7(x, y)
                            Pawn1E7x, Pawn1E7y = x, y
                            PieceDropped = True
            elif ((x < Pawn1F7x + 100) and (x > Pawn1F7x) and (y < Pawn1F7y + 100) and (y > Pawn1F7y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Pawn1F7(x, y)
                            Pawn1F7x, Pawn1F7y = x, y
                            PieceDropped = True
            elif ((x < Pawn1G7x + 100) and (x > Pawn1G7x) and (y < Pawn1G7y + 100) and (y > Pawn1G7y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Pawn1G7(x, y)
                            Pawn1G7x, Pawn1G7y = x, y
                            PieceDropped = True
            elif ((x < Pawn1H7x + 100) and (x > Pawn1H7x) and (y < Pawn1H7y + 100) and (y > Pawn1H7y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Pawn1H7(x, y)
                            Pawn1H7x, Pawn1H7y = x, y
                            PieceDropped = True
            elif ((x < KnightB1x + 100) and (x > KnightB1x) and (y < KnightB1y + 100) and (y > KnightB1y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            KnightB1(x, y)
                            KnightB1x, KnightB1y = x, y
                            PieceDropped = True
            elif ((x < KnightG1x + 100) and (x > KnightG1x) and (y < KnightG1y + 100) and (y > KnightG1y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            KnightG1(x, y)
                            KnightG1x, KnightG1y = x, y
                            PieceDropped = True
            elif ((x < Knight1B8x + 100) and (x > Knight1B8x) and (y < Knight1B8y + 100) and (y > Knight1B8y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Knight1B8(x, y)
                            Knight1B8x, Knight1B8y = x, y
                            PieceDropped = True
            elif ((x < Knight1G8x + 100) and (x > Knight1G8x) and (y < Knight1G8y + 100) and (y > Knight1G8y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Knight1G8(x, y)
                            Knight1G8x, Knight1G8y = x, y
                            PieceDropped = True
            elif ((x < BishopC1x + 100) and (x > BishopC1x) and (y < BishopC1y + 100) and (y > BishopC1y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            BishopC1(x, y)
                            BishopC1x, BishopC1y = x, y
                            PieceDropped = True
            elif ((x < BishopF1x + 100) and (x > BishopF1x) and (y < BishopF1y + 100) and (y > BishopF1y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            Bishop1C8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            BishopF1(x, y)
                            BishopF1x, BishopF1y = x, y
                            PieceDropped = True
            elif ((x < Bishop1C8x + 100) and (x > Bishop1C8x) and (y < Bishop1C8y + 100) and (y > Bishop1C8y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Bishop1C8(x, y)
                            Bishop1C8x, Bishop1C8y = x, y
                            PieceDropped = True
            elif ((x < Bishop1F8x + 100) and (x > Bishop1F8x) and (y < Bishop1F8y + 100) and (y > Bishop1F8y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1F8(Bishop1C8x, Bishop1C8y)
                            RookA1(RookA1x, RookA1y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Bishop1F8(x, y)
                            Bishop1F8x, Bishop1F8y = x, y
                            PieceDropped = True
            elif ((x < RookA1x + 100) and (x > RookA1x) and (y < RookA1y + 100) and (y > RookA1y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1F8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookH1(RookH1x, RookH1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            RookA1(x, y)
                            RookA1x, RookA1y = x, y
                            PieceDropped = True
            elif ((x < RookH1x + 100) and (x > RookH1x) and (y < RookH1y + 100) and (y > RookH1y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1F8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            RookH1(x, y)
                            RookH1x, RookH1y = x, y
                            PieceDropped = True
            elif ((x < Rook1A8x + 100) and (x > Rook1A8x) and (y < Rook1A8y + 100) and (y > Rook1A8y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1F8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookH1(RookH1x, RookH1y)
                            RookA1(RookA1x, RookA1y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Rook1A8(x, y)
                            Rook1A8x, Rook1A8y = x, y
                            PieceDropped = True
            elif ((x < Rook1H8x + 100) and (x > Rook1H8x) and (y < Rook1H8y + 100) and (y > Rook1H8y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1F8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            RookH1(RookH1x, RookH1y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Rook1H8(x, y)
                            Rook1H8x, Rook1H8y = x, y
                            PieceDropped = True
            elif ((x < Kingx + 100) and (x > Kingx) and (y < Kingy + 100) and (y > Kingy)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1F8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            RookH1(RookH1x, RookH1y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            King(x, y)
                            Kingx, Kingy = x, y
                            PieceDropped = True
            elif ((x < King1x + 100) and (x > King1x) and (y < King1y + 100) and (y > King1y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1F8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            RookH1(RookH1x, RookH1y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            Queen(Queenx, Queeny)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            King1(x, y)
                            King1x, King1y = x, y
                            PieceDropped = True
            elif ((x < Queenx + 100) and (x > Queenx) and (y < Queeny + 100) and (y > Queeny)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1F8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            RookH1(RookH1x, RookH1y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen1(Queen1x, Queen1y)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Queen(x, y)
                            Queenx, Queeny = x, y
                            PieceDropped = True
            elif ((x < Queen1x + 100) and (x > Queen1x) and (y < Queen1y + 100) and (y > Queen1y)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            screen.fill(GREEN)
                            Board()
                            PawnA2(PawnA2x, PawnA2y)
                            PawnB2(PawnB2x, PawnB2y)
                            PawnC2(PawnC2x, PawnC2y)
                            PawnD2(PawnD2x, PawnD2y)
                            PawnE2(PawnE2x, PawnE2y)
                            PawnF2(PawnF2x, PawnF2y)
                            PawnG2(PawnG2x, PawnG2y)
                            PawnH2(PawnH2x, PawnH2y)
                            Pawn1A7(Pawn1A7x, Pawn1A7y)
                            Pawn1B7(Pawn1B7x, Pawn1B7y)
                            Pawn1C7(Pawn1C7x, Pawn1C7y)
                            Pawn1D7(Pawn1D7x, Pawn1D7y)
                            Pawn1E7(Pawn1E7x, Pawn1E7y)
                            Pawn1F7(Pawn1F7x, Pawn1F7y)
                            Pawn1G7(Pawn1G7x, Pawn1G7y)
                            Pawn1H7(Pawn1H7x, Pawn1H7y)
                            KnightB1(KnightB1x, KnightB1y)
                            KnightG1(KnightG1x, KnightG1y)
                            Knight1B8(Knight1B8x, Knight1B8y)
                            Knight1G8(Knight1G8x, Knight1G8y)
                            BishopC1(BishopC1x, BishopC1y)
                            BishopF1(BishopF1x, BishopF1y)
                            Bishop1F8(Bishop1C8x, Bishop1C8y)
                            Bishop1F8(Bishop1F8x, Bishop1F8y)
                            RookA1(RookA1x, RookA1y)
                            Rook1A8(Rook1A8x, Rook1A8y)
                            RookH1(RookH1x, RookH1y)
                            Rook1H8(Rook1H8x, Rook1H8y)
                            King(Kingx, Kingy)
                            King1(King1x, King1y)
                            Queen(Queenx, Queeny)
                            x = round(x, -2) - 15
                            y = round(y, -2) - 50
                            Queen1(x, y)
                            Queen1x, Queen1y = x, y
                            PieceDropped = True
    clock.tick(60)
   
pygame.quit()
quit()