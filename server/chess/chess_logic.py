from chess import util
from chess import knight
 
class Chess:
    def __init__(self, fen):
        self.fen = fen
        self.fen_list = util.fen_to_list(fen)

    def is_legal_move(self, from_index, to_index):
        piece = self.fen_list[from_index]
        color = 'w' if piece.isupper() else 'b'

        # def update_fen():
        #     self.fen_list[from_index] = None
        #     self.fen_list[to_index] = piece
        #     self.fen = util.list_to_fen(self.fen_list) + ' - - - - -'

        #     return self.fen

        # knight
        if piece.upper() == 'N':
            selected_piece = knight.Knight(color, from_index, self.fen_list)
            legal_indexes = selected_piece.moves()
            if to_index in legal_indexes:
                return True
            else:
                return False