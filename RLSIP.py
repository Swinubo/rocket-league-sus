import pygame
pygame.init()

X = 600
Y = 600
scrn = pygame.display.set_mode((X, Y))

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
PURPLE = (134, 19, 144)
YELLOW = (212, 195, 27)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rocket League Sus in Python")

done = False
clock = pygame.time.Clock()

done = False
clock = pygame.time.Clock()

while not done:

    screen.fill(WHITE)
    CharacterImg = pygame.image.load("C:\\Users\\silgas\\Documents\\Dev\\Character.png").convert()
    scrn.blit(CharacterImg, (0, 0))

    pygame.display.flip()
    # This limits the while loop to a max of 60 times per second.
    clock.tick(60) 