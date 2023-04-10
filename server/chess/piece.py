from chess import util

class Piece:
    def __init__(self, color, index, fen_list):
        self.color = color
        self.index = index
        self.fen_list = fen_list

        self.file, self.rank = util.index_to_filerank(self.index)

    def check_index(self, file, rank):
        if 1 <= file <= 8 and 1 <= rank <= 8:
            index = util.filerank_to_index(file, rank)
            target_piece = self.fen_list[index]
            if not target_piece:
                return True
            else:
                target_color = 'w' if target_piece.isupper() else 'b'
                if target_color != self.color:
                    return True