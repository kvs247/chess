from chess import util
from chess.piece import Piece

class Bishop(Piece):
    def __init__(self, color, index, fen):
        super().__init__(color, index, fen)

    def moves(self):
        moves = []

        offsets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for offset_file, offset_rank in offsets:
            target_file = self.file
            target_rank = self.rank
            while True:
                target_file += offset_file
                target_rank += offset_rank
                if not self.can_move(target_file, target_rank):
                    break
                # target square is on board and not occupied by friendly piece
                else:
                    index = util.filerank_to_index(target_file, target_rank)
                    moves.append(index)
                    target_color = self.get_color(index)
                    # target square is empty - continue
                    if not target_color:
                        continue
                    # target square is occupied by enemy piece - stop
                    else:
                        if target_color != self.color:
                            break

        return moves