from chess import util
from chess.piece import Piece
    
class Knight(Piece):
    def __init__(self, color, index, fen_list):
        super().__init__(color, index, fen_list)

    def moves(self):
        moves = []

        offsets = [(1, 2),(1, -2),(-1, 2),(-1, -2),
                   (2, 1),(2, -1),(-2, 1),(-2, -1)]

        for offset_file, offset_rank in offsets:
            target_file = self.file + offset_file
            target_rank = self.rank + offset_rank
            if self.check_index(target_file, target_rank):
                moves.append(util.filerank_to_index(target_file, target_rank))

        return moves





    
    