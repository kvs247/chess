from chess import util

class Piece:
    def __init__(self, color, index, fen):
        self.color = color
        self.index = index
        self.fen = fen

        self.file, self.rank = util.index_to_filerank(self.index)
        self.fen_dict = util.fen_to_dict(fen)
        self.piece_list = util.fen_to_list(self.fen_dict['piece_placement'])

    def can_move(self, file, rank):
        if 1 <= file <= 8 and 1 <= rank <= 8:
            index = util.filerank_to_index(file, rank)
            target_piece = self.piece_list[index]
            if not target_piece:
                return True
            else:
                target_color = 'w' if target_piece.isupper() else 'b'
                if target_color != self.color:
                    return True
            return False