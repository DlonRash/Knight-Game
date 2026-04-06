## Board Game Script[D'lon Rash]

# since im gonna want to visualize the project, I'm going to start implementing pygame to help me do so. "Dlon"

import pygame
# screen setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
# Drawing Board
cellSize = 80
board = pygame.Surface((cellSize * 8, cellSize * 8))
board_x = (1280 - (cellSize * 8)) // 2
board_y = (720 - (cellSize * 8)) // 2
for x in range(8):
    for y in range(8):
        if (x + y) % 2 == 0:
            color = ( (253, 253, 150)) 
        else:
            color = (100, 100, 100)  
        pygame.draw.rect(board, color,  (x * cellSize, y * cellSize, cellSize, cellSize))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Thistle")

    # RENDER YOUR GAME HERE
    screen.blit(board, (board_x, board_y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()    
    