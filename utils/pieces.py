import pygame
from pygame.locals import RLEACCEL
import config


class Piece(pygame.sprite.Sprite):
    def __init__(self, picture: str, cell: int = -1):
        super(Piece, self).__init__()
        self.pic = f"resources/{picture}.png"
        self.cell = cell

        self.surf = pygame.image.load(self.pic)
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(
            self.surf, (config.cell_size, config.cell_size)
        )
        # self.surf = self.surf.convert()

        self.rect = self.surf.get_rect()

    def set_cell(self, cell):
        self.cell = cell
        return self


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
