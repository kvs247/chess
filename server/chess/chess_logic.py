from chess import util
from chess import knight
 
class Chess:
    def __init__(self, fen):
        self.fen = fen
        self.fen_list = util.fen_to_list(fen)

    def move(self, from_index, to_index):
        piece = self.fen_list[from_index]
        color = self.fen.split(' ')[1]

        # correct color
        print('color', color)
        print('piece', piece)
        if color == 'w' and piece.islower():
            return None
        print('color==b', color == 'b')
        print('piece.isupper()', piece.isupper())
        if color == 'b' and piece.isupper():
            print('fire')
            return None

        # knight
        if piece.upper() == 'N':
            selected_piece = knight.Knight(color, from_index, self.fen_list)
            legal_indexes = selected_piece.moves()
            if to_index in legal_indexes:
                return util.index_to_algebraic(self.fen, from_index, to_index)
            else:
                return None