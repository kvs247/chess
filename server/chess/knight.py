from chess import util
from chess.piece import Piece
    
class Knight(Piece):
    def __init__(self, color, index, fen):
        super().__init__(color, index, fen)

    def moves(self):
        moves = []

        offsets = [(1, 2),(1, -2),(-1, 2),(-1, -2),
                   (2, 1),(2, -1),(-2, 1),(-2, -1)]

        for offset_file, offset_rank in offsets:
            target_file = self.file + offset_file
            target_rank = self.rank + offset_rank
            if self.can_move(target_file, target_rank):
                moves.append(util.filerank_to_index(target_file, target_rank))

        return moves





    
    