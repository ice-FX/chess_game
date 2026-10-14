import pygame 

pygame.init()

#CREATE A NEW WINDOW
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("CHESS v1")

#CHESS BOARD COLORS
LIGHT = (240, 217, 181)
DARK = (181, 136, 99)

#EACH SQUARE IS 80 PIXELS WIDE AND TALL
SQUARE_SIZE = 80

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #DRAW THE CHESS BOARD
    for row in range(8):
        for col in range(8):

            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE

            if (row + col) % 2 == 0:
                color = LIGHT
            else:
                color = DARK

            pygame.draw.rect(
                screen,
                color,
                (x, y, SQUARE_SIZE, SQUARE_SIZE)
            )
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
