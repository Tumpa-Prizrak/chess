from utils import pieces
from typing import Optional

def FENtoPieces(fen: str) -> list[pieces.Piece]:  # TODO Finish for other info
    out = []
    rank = 0
    file = 0

    for char in fen.split()[0]:
        if (piece := symbol_to_piece(char)) is None:
            if char == '/':
                rank += 1
                file = 0
            else:
                file += int(char)
        else:
            piece = piece().set_cell(rank * 8 + file)
            out.append(piece)
            file += 1
    
    return out


def symbol_to_piece(char: str) -> Optional[pieces.Piece]:
    color = "black" if char.islower() else "white"

    piece_map = {
        "p": pieces.WhitePieces.pawn if color == "white" else pieces.BlackPieces.pawn,
        "n": pieces.WhitePieces.knight if color == "white" else pieces.BlackPieces.knight,
        "b": pieces.WhitePieces.bishop if color == "white" else pieces.BlackPieces.bishop,
        "r": pieces.WhitePieces.rook if color == "white" else pieces.BlackPieces.rook,
        "q": pieces.WhitePieces.queen if color == "white" else pieces.BlackPieces.queen,
        "k": pieces.WhitePieces.king if color == "white" else pieces.BlackPieces.king
    }

    return piece_map.get(char.lower())
