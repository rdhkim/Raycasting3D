import pygame
import sys
import math

#const
SCREEN_HEIGHT = 480
SCREEN_WIDTH = SCREEN_HEIGHT * 2
MAP_SIZE = 8
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
FOV = math.pi / 3
HALF_FOV = FOV / 2

#global variables
player_x = (SCREEN_WIDTH / 2) / 2
player_y = (SCREEN_WIDTH / 2) / 2
player_angle = math.pi

#game map
MAP = (
    '########'
    '# # #  #'
    '# #    #'
    '#    ###'
    '# #    #'
    '#    ###'
    '# #    #'
    '########'
)

#init game
pygame.init()

# creat game window
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set window title
pygame.display.set_caption('Raycasting')

# init timer
clock = pygame.time.Clock()

# draw map
def draw_map():
    # loop over map rows
    for row in range(MAP_SIZE):
        # loop over map columns
        for col in range(MAP_SIZE):
            # calc square index
            square = row * MAP_SIZE + col

            # draw map in game window
            pygame.draw.rect(
                win,
                #color
                (200, 200, 200) if MAP[square] == '#' else (100, 100, 100),
                (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 2, TILE_SIZE - 2)
            )
    #draw 2d character on baord
    pygame.draw.circle(win, (255, 0, 0), (int(player_x), int(player_y)), 8)
#main loop
while True:

    #escape condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    # draw map
    draw_map()

    # update display
    pygame.display.flip()

    # set frames per sec
    clock.tick(30)
