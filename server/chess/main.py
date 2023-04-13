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
        self.fen_dict = util.fen_to_dict(fen)

    def move(self, from_index, to_index):
        piece = self.fen_list[from_index]
        color = self.fen.split(' ')[1]

        # idea for later?
        # return_move = None

        # correct turn
        if color == 'w' and piece.islower():
            return None
        if color == 'b' and piece.isupper():
            return None
        
        # king in check?
        # promotion? :(
        def king_in_check_after_move(color, fen):
            fen_list = util.fen_to_list(fen)
            king_index = fen_list.index('K') if color == 'w' else fen_list.index('k')
            king = King(color, king_index, fen)
            if king.in_check(king_index):
                return True
            return False
        new_fen = update_fen(self.fen, from_index, to_index)
        if king_in_check_after_move(color, new_fen):
            return None
        
        # checkmate?
        new_fen = update_fen(self.fen, from_index, to_index)
        new_fen_list = util.fen_to_list(new_fen)
        # king in check and no legal moves
        king_index = new_fen_list.index('k') if color == 'w' else new_fen_list.index('K')
        king_color = 'w' if color == 'b' else 'b'
        king = King(king_color, king_index, new_fen)
        if king.in_check(king_index) and len(king.moves()) == 0:
            checkmate = True
            for index in range(64):
                piece = new_fen_list[index]
                if not piece:
                    continue # break and not contiue?
                piece_color = 'w' if piece.isupper() else 'b'
                if piece_color != king_color:
                    continue
                if piece.upper() == 'P':
                    pawn = Pawn(king_color, index, new_fen)   
                    for move in pawn.moves():
                        piece_fen = update_fen(new_fen, index, move)
                        if not king_in_check_after_move(king_color, piece_fen):
                            # print(f'{index} pawn can move {move}')
                            checkmate = False
                            break
                if piece.upper() == 'N':
                    knight = Knight(king_color, index, new_fen)   
                    for move in knight.moves():
                        piece_fen = update_fen(new_fen, index, move)
                        if not king_in_check_after_move(king_color, piece_fen):
                            # print(f'{index} knight can move {move}')
                            checkmate = False
                            break
                if piece.upper() == 'B':
                    bishop = Bishop(king_color, index, new_fen)   
                    for move in bishop.moves():
                        piece_fen = update_fen(new_fen, index, move)
                        if not king_in_check_after_move(king_color, piece_fen):
                            # print(f'{index} bishop can move {move}')
                            checkmate = False                        
                            break
                if piece.upper() == 'R':
                    rook = Rook(king_color, index, new_fen)   
                    for move in rook.moves():
                        piece_fen = update_fen(new_fen, index, move)
                        if not king_in_check_after_move(king_color, piece_fen):
                            # print(f'{index} rook can move {move}')
                            checkmate = False                        
                            break
                if piece.upper() == 'Q':
                    queen = Queen(king_color, index, new_fen)   
                    for move in queen.moves():
                        piece_fen = update_fen(new_fen, index, move)
                        if not king_in_check_after_move(king_color, piece_fen):
                            # print(f'{index} queen can move {move}')
                            checkmate = False                        
                            break
            if checkmate:
                print('checkmate')
            
        

        # castling
        king = King(color, from_index, self.fen)
        if piece == 'K':
            if from_index == 60 and to_index == 62:
                if not self.fen_list[61] and not self.fen_list[62]:
                    if self.fen_dict['castling_availability'].find('K') != -1:
                        if not king.in_check(61) and not king.in_check(62):
                            return 'O-O'
            if from_index == 60 and to_index == 58:     
                if not self.fen_list[58] and not self.fen_list[59]:
                    if self.fen_dict['castling_availability'].find('Q') != -1:
                        if not king.in_check(58) and not king.in_check(59):
                            return 'O-O-O'
        if piece == 'k':
            if from_index == 4 and to_index == 6:
                if not self.fen_list[5] and not self.fen_list[6]:
                    if self.fen_dict['castling_availability'].find('k') != -1:
                        if not king.in_check(5) and not king.in_check(6):
                            return 'O-O'
            if from_index == 4 and to_index == 2:     
                if not self.fen_list[2] and not self.fen_list[3]:
                    if self.fen_dict['castling_availability'].find('q') != -1:
                        if not king.in_check(3) and not king.in_check(2):
                            return 'O-O-O'

        # print(piece)
        piece = self.fen_list[from_index]
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