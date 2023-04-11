from chess.piece import Piece
from chess.bishop import Bishop
from chess.rook import Rook

class Queen(Piece):
    def __init__(self, color, index, fen):
        super().__init__(color, index, fen)

    def moves(self):
        moves = []

        bishop = Bishop(self.color, self.index, self.fen)
        rook = Rook(self.color, self.index, self.fen)

        moves += bishop.moves()
        moves += rook.moves()

        return moves