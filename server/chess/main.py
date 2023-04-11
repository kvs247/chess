from chess import util
from chess.knight import Knight
from chess.bishop import Bishop
from chess.pawn import Pawn
 
class Chess:
    def __init__(self, fen):
        self.fen = fen
        self.fen_list = util.fen_to_list(fen)

    def move(self, from_index, to_index):
        piece = self.fen_list[from_index]
        color = self.fen.split(' ')[1]

        # correct turn
        if color == 'w' and piece.islower():
            return None
        if color == 'b' and piece.isupper():
            print('fire')
            return None
        
        # pawn
        if piece.upper() == 'P':
            selected_piece = Pawn(color, from_index, self.fen)
            legal_indexes = selected_piece.moves()
            if to_index in legal_indexes:
                move = util.index_to_algebraic(self.fen, from_index, to_index)
                # promotion
                if move[-1] == '8' or move[-1] == '1':
                    move += '=Q'
                    return move
                return util.index_to_algebraic(self.fen, from_index, to_index)
            else:
                return None

        # knight
        if piece.upper() == 'N':
            selected_piece = Knight(color, from_index, self.fen)
            legal_indexes = selected_piece.moves()
            if to_index in legal_indexes:
                return util.index_to_algebraic(self.fen, from_index, to_index)
            else:
                return None
            
        # bishop
        if piece.upper() == 'B':
            selected_piece = Bishop(color, from_index, self.fen)
            legal_indexes = selected_piece.moves()
            if to_index in legal_indexes:
                return util.index_to_algebraic(self.fen, from_index, to_index)
            else:
                return None