import pygame
from utils import board, helper
import config
from datatypes import WhitePieces

pygame.init()

screen = pygame.display.set_mode([config.cell_size * 8, config.cell_size * 8])
pygame.display.set_caption("Chess")

# curr_board = board.Board(helper.FENtoPieces("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))
curr_board = board.Board()
curr_board.add_piece(WhitePieces.rook().set_cell(44))


mouseBottonDownCoords = None


def main():
    global mouseBottonDownCoords
    """curr_board.render(screen)
    pygame.display.flip()"""

    while True:
        for event in pygame.event.get():
            # print(mouseBottonDownCoords)
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    x, y = pygame.mouse.get_pos()
                    x //= config.cell_size
                    y //= config.cell_size
                    curr_cell = curr_board.get_cell_by_coords(x, y)

                    if (
                        mouseBottonDownCoords is None
                        or mouseBottonDownCoords == curr_cell
                    ):
                        print(curr_cell.toggle_hightlight())
                    else:
                        if not curr_board.remove_arrow(
                            mouseBottonDownCoords, curr_cell
                        ):
                            curr_board.add_arrow(mouseBottonDownCoords, curr_cell)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    x, y = pygame.mouse.get_pos()
                    x //= config.cell_size
                    y //= config.cell_size

                    mouseBottonDownCoords = curr_board.get_cell_by_coords(x, y)

        curr_board.render(screen)
        pygame.display.flip()


main()
pygame.quit()
