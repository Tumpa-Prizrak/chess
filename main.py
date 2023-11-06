import pygame
from utils import board, pieces, helper
import config

pygame.init()

screen = pygame.display.set_mode([config.cell_size * 8, config.cell_size * 8])
pygame.display.set_caption("Chess")

curr_board = board.Board(helper.FENtoPieces("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))


def main():
    curr_board.draw(screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        curr_board.draw(screen)
        curr_board.draw_pieces(screen)

        pygame.display.flip()
 

main()
pygame.quit()
