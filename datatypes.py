from config import cell_size
import pygame
import config
import math
from pygame.locals import RLEACCEL


class Cell:
    x: int
    y: int
    cell: int
    highlighted: bool

    def __init__(self, a: int, b: int = -1, highlighted: bool = False) -> None:
        if b == -1:
            a, b = (a % 8, a // 8)

        self.x = a
        self.y = b
        self.cell = a + b * 8
        self.highlighted = highlighted

    def __str__(self) -> str:
        return str(self.cell)

    def __repr__(self) -> str:
        return str(self)

    def __abs__(self) -> tuple:
        return (self.x * cell_size, self.y * cell_size)

    ### hightlight ###

    def hightlight(self):
        self.highlighted = True

    def unhightlight(self):
        self.highlighted = False

    def toggle_hightlight(self):
        self.highlighted = not self.highlighted

    def center(self) -> tuple:
        return (
            self.x * cell_size + cell_size // 2,
            self.y * cell_size + cell_size // 2,
        )

    def draw(self, screen: pygame.Surface):
        bgcolor = config.board1 if (self.x + self.y) % 2 == 0 else config.board2
        startPos = (self.x * config.cell_size, self.y * config.cell_size)

        pygame.draw.rect(
            screen,
            config.highlighted_board if self.highlighted else bgcolor,
            (*startPos, config.cell_size, config.cell_size),
        )


class Arrow:
    start: Cell
    end: Cell
    color: tuple[int, int, int]

    def __init__(
        self, start: Cell, end: Cell, color: tuple[int, int, int] = (0, 0, 0)
    ) -> None:
        self.start = start
        self.end = end
        self.color = color

    def draw(self, screen: pygame.Surface):
        x1, y1 = startPos = self.start.center()
        x2, y2 = endPos = self.end.center()

        # Calculate angle and rotate arrow point
        n = 20
        angle = math.atan2(y2 - y1, x2 - x1)
        xr = x2 - n * math.cos(angle + math.pi / 6)
        yr = y2 - n * math.sin(angle + math.pi / 6)
        xl = x2 - n * math.cos(angle - math.pi / 6)
        yl = y2 - n * math.sin(angle - math.pi / 6)

        points = [startPos, endPos, (xr, yr), endPos, (xl, yl), endPos]

        pygame.draw.polygon(screen, self.color, points, width=5)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Arrow):
            return abs(self.start) == abs(__value.start) and abs(self.end) == abs(
                __value.end
            )
        return False


class Piece(pygame.sprite.Sprite):
    def __init__(self, picture: str, cell: int = -1):
        super(Piece, self).__init__()
        self.pic = f"resources/{picture}.png"
        self.cell = Cell(cell)

        self.surf = pygame.image.load(self.pic)
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(
            self.surf, (config.cell_size, config.cell_size)
        )

        self.rect = self.surf.get_rect()

    def set_cell(self, cell: int | Cell):
        if isinstance(cell, int):
            cell = Cell(cell)

        self.cell = cell
        return self

    def draw(self, screen: pygame.Surface):
        screen.blit(self.surf, abs(self.cell))


class WhitePieces:
    @staticmethod
    def pawn():
        return Piece("white-pawn")

    @staticmethod
    def knight():
        return Piece("white-knight")

    @staticmethod
    def bishop():
        return Piece("white-bishop")

    @staticmethod
    def rook():
        return Piece("white-rook")

    @staticmethod
    def queen():
        return Piece("white-queen")

    @staticmethod
    def king():
        return Piece("white-king")


class BlackPieces:
    @staticmethod
    def pawn():
        return Piece("black-pawn")

    @staticmethod
    def knight():
        return Piece("black-knight")

    @staticmethod
    def bishop():
        return Piece("black-bishop")

    @staticmethod
    def rook():
        return Piece("black-rook")

    @staticmethod
    def queen():
        return Piece("black-queen")

    @staticmethod
    def king():
        return Piece("black-king")
