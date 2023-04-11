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
        # returns True if square is on board and not occupied by friendly piece
        if not self.is_on_board(file, rank):
            return False
        index = util.filerank_to_index(file, rank)
        color = self.get_color(index)
        if not color:
            return True
        elif color != self.color:
            return True 
        return False
        
    def is_on_board(self, file, rank):
        if 1 <= file <= 8 and 1 <= rank <= 8:
            return True
        return False
    
    def get_color(self, index):
        target_piece = self.piece_list[index]
        if target_piece:
            return 'w' if target_piece.isupper() else 'b'
        return None
    