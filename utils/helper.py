from typing import Optional, Callable
from datatypes import Piece, WhitePieces, BlackPieces


def FENtoPieces(fen: str) -> list[Piece]:  # TODO Finish for other info
    out = []
    rank = 0
    file = 0

    for char in fen.split()[0]:
        if (piece := symbol_to_piece(char)) is None:
            if char == "/":
                rank += 1
                file = 0
            else:
                file += int(char)
        else:
            piece = piece().set_cell(rank * 8 + file)
            out.append(piece)
            file += 1

    return out


def symbol_to_piece(char: str) -> Optional[Callable[[], Piece]]:
    color = "black" if char.islower() else "white"

    piece_map = {
        "p": WhitePieces.pawn if color == "white" else BlackPieces.pawn,
        "n": WhitePieces.knight if color == "white" else BlackPieces.knight,
        "b": WhitePieces.bishop if color == "white" else BlackPieces.bishop,
        "r": WhitePieces.rook if color == "white" else BlackPieces.rook,
        "q": WhitePieces.queen if color == "white" else BlackPieces.queen,
        "k": WhitePieces.king if color == "white" else BlackPieces.king,
    }

    return piece_map.get(char.lower())
