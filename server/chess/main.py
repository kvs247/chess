from chess import util
from chess.pawn import Pawn
from chess.knight import Knight
from chess.bishop import Bishop
from chess.rook import Rook
from chess.queen import Queen
from chess.king import King
from chess.pgn_to_fen import update_fen

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
            return None
        
        # king in check?
        # promotion? :(
        new_fen = update_fen(self.fen, from_index, to_index)
        new_fen_list = util.fen_to_list(new_fen)
        king_index = new_fen_list.index('K') if color == 'w' else new_fen_list.index('k')
        king = King(color, king_index, new_fen)
        if king.in_check(king_index):
            return None

        # castling
        
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
            
        # rook
        if piece.upper() == 'R':
            selected_piece = Rook(color, from_index, self.fen)
            legal_indexes = selected_piece.moves()
            if to_index in legal_indexes:
                return util.index_to_algebraic(self.fen, from_index, to_index)
            else:
                return None
            
        # queen
        if piece.upper() == 'Q':
            selected_piece = Queen(color, from_index, self.fen)
            legal_indexes = selected_piece.moves()
            if to_index in legal_indexes:
                return util.index_to_algebraic(self.fen, from_index, to_index)
            else:
                return None
            
        # king 
        if piece.upper() == 'K':
            selected_piece = King(color, from_index, self.fen)
            legal_indexes = selected_piece.moves()
            if to_index in legal_indexes:
                return util.index_to_algebraic(self.fen, from_index, to_index)
            else:
                return None