from chess import util
from chess.piece import Piece

class Rook(Piece):
    def __init__(self, color, index, fen):
        super().__init__(color, index, fen)

    def moves(self):
        moves = []

        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for offset_file, offset_rank in offsets:
            target_file = self.file
            target_rank = self.rank
            while True:
                target_file += offset_file
                target_rank += offset_rank
                # check square is on board and not occupied by friendly piece
                if self.can_move(target_file, target_rank):
                    index = util.filerank_to_index(target_file, target_rank)
                    moves.append(index)
                    target_piece = self.piece_list[index]
                    if target_piece:
                        target_color = 'w' if target_piece.isupper() else 'b'
                        if target_color != self.color:
                            break
                else:
                    break

        return moves