from pygame import Surface
import pygame
import config
from utils.pieces import BlackPieces, WhitePieces, Piece
from utils import draw


class Board:
    pieces: list[Piece]
    cells: list[int] = []

    def __init__(self, pieces: list[Piece] | None = None):
        if pieces is None:
            pieces = list()
        self.pieces = pieces

    def draw(self, screen: Surface):
        for row in range(8):
            for file in range(8):
                bgcolor = config.board1 if (row + file) % 2 == 0 else config.board2
                startPos = (file * config.cell_size, row * config.cell_size)

                pygame.draw.rect(
                    screen, bgcolor, (*startPos, config.cell_size, config.cell_size)
                )
                if config.mode & 0b01 == 0b01:
                    draw.draw_text(
                        screen,
                        config.lato32,
                        (
                            startPos[0] + config.cell_size // 2,
                            startPos[1] + config.cell_size // 2,
                        ),
                        str(row * 8 + file - (36 if config.mode & 0b10 == 0b10 else 0)),
                        (0, 0, 0),
                    )

    ### Pieces ###

    def add_piece(self, piece: Piece):
        self.pieces.append(piece)

    def draw_piece(self, screen: Surface, piece: Piece):  # I hate this bug
        row, file = piece.cell // 8, piece.cell % 8
        pos = (file * config.cell_size, row * config.cell_size)

        screen.blit(piece.surf, pos)
    
    def draw_pieces(self, screen: Surface):
        for piece in self.pieces:
            self.draw_piece(screen, piece)
