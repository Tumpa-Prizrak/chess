from pygame import Surface
import pygame
import config
from datatypes import Piece
from utils import draw
from datatypes import Cell, Arrow


class Board:
    pieces: list[Piece]
    cells: list[Cell]
    arrows: list[Arrow]

    def __init__(self, pieces: list[Piece] | None = None):
        if pieces is None:
            pieces = list()
        self.pieces = pieces
        self.cells = [Cell(i) for i in range(64)]
        self.arrows = []

    def render(self, screen: Surface):
        self.draw_cells(screen)
        self.draw_pieces(screen)
        self.draw_arrows(screen)

    ### Pieces ###

    def add_piece(self, piece: Piece):
        self.pieces.append(piece)

    def draw_pieces(self, screen: Surface):
        for piece in self.pieces:
            piece.draw(screen)

    ### Cells ###

    def get_cell(self, N: int):
        return self.cells[N]
    
    def get_cell_by_coords(self, x: int, y: int):
        return self.cells[x + y * 8]
    
    def draw_cells(self, screen: Surface):
        for cell in self.cells:
            cell.draw(screen)
            if config.mode & 0b01 == 0b01:
                draw.draw_text(
                    screen,
                    config.lato32,
                    (
                        abs(cell)[0] + config.cell_size // 2,
                        abs(cell)[1] + config.cell_size // 2,
                    ),
                    str(cell.cell),
                    (0, 0, 0),
                )
    
    ### Arrows ###

    def get_arrow(self, start: Cell, end: Cell) -> Arrow | None:
        for arrow in self.arrows:
            if arrow.start == start and arrow.end == end:
                return arrow
        return None
    
    def draw_arrows(self, screen: Surface):
        for arrow in self.arrows:
            arrow.draw(screen)
    
    def add_arrow(self, start: Cell, end: Cell):
        self.arrows.append(Arrow(start, end))
    
    def remove_arrow(self, start: Cell, end: Cell):
        try:
            self.arrows.remove(Arrow(start, end))
            return True
        except ValueError:
            return False
