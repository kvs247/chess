from chess import util
from chess.piece import Piece

class King(Piece):
    def __init__(self, color, index, fen):
        super().__init__(color, index, fen)

    def moves(self):
        moves = []

        offsets = [(1, 0), (1, 1), (0, 1), (-1, 1),
                   (-1, 0), (-1, -1), (0, -1), (1, -1)]

        for offset_file, offset_rank in offsets:
            target_file = self.file + offset_file
            target_rank = self.rank + offset_rank
            if self.can_move(target_file, target_rank):
                moves.append(util.filerank_to_index(target_file, target_rank))

        # check
        # print(moves)
        legal_moves = []
        for move in moves:
            # print('move', move)
            if not self.in_check(move):
                legal_moves.append(move)

        print('legal_moves', legal_moves)
        return legal_moves
    
    def in_check(self, index):
        # rook/queen vertical/horizontal check
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for offset_file, offset_rank in offsets:
            file, rank = util.index_to_filerank(index)
            while True:
                file += offset_file
                rank += offset_rank
                if not self.is_on_board(file, rank):
                    break
                current_index = util.filerank_to_index(file, rank)
                target_piece = self.piece_list[current_index]
                # empty square - continue
                if not target_piece:
                    continue
                target_color = 'w' if target_piece.isupper() else 'b'
                # friendly piece - stop
                if target_color == self.color:
                    break
                # enemy piece
                if target_piece.upper() == 'R' or target_piece.upper() == 'Q':
                    return True
                else:
                    break
        # bishop/queen diagonal check
        offsets = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

        for offset_file, offset_rank in offsets:
            file, rank = util.index_to_filerank(index)
            while True:
                file += offset_file
                rank += offset_rank
                if not self.is_on_board(file, rank):
                    break
                current_index = util.filerank_to_index(file, rank)
                target_piece = self.piece_list[current_index]
                # empty square - continue
                if not target_piece:
                    continue
                target_color = 'w' if target_piece.isupper() else 'b'
                # friendly piece - stop
                if target_color == self.color:
                    break
                # enemy piece
                if target_piece.upper() == 'B' or target_piece.upper() == 'Q':
                    return True
                else:
                    break
        # knight check
        offsets = [(1, 2),(1, -2),(-1, 2),(-1, -2),
                   (2, 1),(2, -1),(-2, 1),(-2, -1)]
        
        for offset_file, offset_rank in offsets:
            file, rank = util.index_to_filerank(index)
            file += offset_file
            rank += offset_rank
            if not self.is_on_board(file, rank):
                continue
            current_index = util.filerank_to_index(file, rank)
            target_piece = self.piece_list[current_index]
            if not target_piece:
                continue
            target_color = 'w' if target_piece.isupper() else 'b'
            if target_color != self.color and target_piece.upper() == 'N':
                print('check', target_piece, current_index)
                return True
        # pawn check
        # king check

        return False