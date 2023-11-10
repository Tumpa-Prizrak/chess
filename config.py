import pygame

pygame.init()


### Colors ###
board1 = (118, 150, 86)
board2 = (238, 238, 210)
highlighted_board = (252, 40, 71)


### Values ###
cell_size = 100  # Ugly(


### Fonts ###
lato32 = pygame.font.Font("resources/Lato.ttf", 32)


### Features ###
draw_index = True
draw_index_with_offset = False

list_of_features = [draw_index, draw_index_with_offset]
mode = 0
for value in list_of_features[::-1]:
    mode = (mode << 1) | value

# It just works
