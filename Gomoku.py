import pygame
import sys

#Set constant value
EMPTY = 0
BLACK = 1
WHITE = 2
COLOR_BLACK = [0, 0, 0]
COLOR_WHITE = [225, 225, 225]
COLOR_YELLOW = [220, 179, 92]
NUM_1 = 34
NUM_2 = 600-34

#Initialize the game
pygame.init()

#Set screen size
screen = pygame.display.set_mode((600, 600))


#refresh the screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #fill the background color
    screen.fill(COLOR_YELLOW)

    #draw lines
    for i in range(34, 600, 38):
        if i == NUM_1 or i == NUM_2:
            pygame.draw.line(screen, COLOR_BLACK, [i, NUM_1], [i, NUM_2], 2)
        else:
            pygame.draw.line(screen, COLOR_BLACK, [i, NUM_1], [i, NUM_2], 1)

        if i == NUM_1 or i == NUM_2:
            pygame.draw.line(screen, COLOR_BLACK, [NUM_1, i], [NUM_2, i], 2)
        else:
            pygame.draw.line(screen, COLOR_BLACK, [NUM_1, i], [NUM_2, i], 1)

    #draw special points
    pygame.draw.rect(screen, COLOR_BLACK, [25, 25, 552, 552], 5)
    pygame.draw.circle(screen, COLOR_BLACK, [NUM_1+38*7, NUM_1+38*7], 6, 0)
    pygame.draw.circle(screen, COLOR_BLACK, [NUM_1 + 38 * 3, NUM_1 + 38 * 3], 4, 0)
    pygame.draw.circle(screen, COLOR_BLACK, [NUM_1 + 38 * 11, NUM_1 + 38 * 11], 4, 0)
    pygame.draw.circle(screen, COLOR_BLACK, [NUM_1 + 38 * 3, NUM_1 + 38 * 11], 4, 0)
    pygame.draw.circle(screen, COLOR_BLACK, [NUM_1 + 38 * 11, NUM_1 + 38 * 3], 4, 0)

    pygame.display.update()







