from chess import util
from chess.piece import Piece

class Pawn(Piece):
    def __init__(self, color, index, fen):
        super().__init__(color, index, fen)

    def moves(self):
        moves = []

        sign = 1 if self.color == 'w' else -1
        # 1 rank
        index = util.filerank_to_index(self.file, self.rank + (1 * sign))
        if 0 <= index <= 63:
            empty = not self.piece_list[index]
            if empty and self.can_move(self.file, self.rank + (1 * sign)):
                moves.append(index)
        # 2 ranks
        index = util.filerank_to_index(self.file, self.rank + (2 * sign))
        if 0 <= index <= 63:
            empty = not self.piece_list[index]
            first_move = (self.rank == 2 or self.rank == 7)
            boolean = empty and first_move
            if boolean and self.can_move(self.file, self.rank + (2 * sign)):
                moves.append(util.filerank_to_index(self.file, self.rank + (2 * sign)))
        # capture
        for offset in [1, -1]:
            index = util.filerank_to_index(self.file + offset, self.rank + (1 * sign))
            if 0 <= index <= 63:
                target_piece = self.piece_list[index]
                if target_piece:
                    target_color = 'w' if target_piece.isupper() else 'b'
                    if target_color != self.color:
                        moves.append(index)
        # en passant
        en_passant_target_square = self.fen_dict['en_passant_target_square']
        if en_passant_target_square != '-':
            index = util.square_to_index(en_passant_target_square)
            if 0 <= index <= 63:
                file, rank = util.index_to_filerank(index)
                if self.file == file + 1 or self.file == file - 1:
                    if self.rank == rank - (1 * sign):
                        index = util.filerank_to_index(file, rank)
                        moves.append(index)

        return moves