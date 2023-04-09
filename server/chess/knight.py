from chess import util

class Knight:
    def __init__(self, color, index, fen_list):
        self.color = color
        self.index = index
        self.fen_list = fen_list

    def moves(self):
        moves = []
        file, rank = util.index_to_filerank(self.index)

        def check_index(file, rank):
            if 1 <= file <= 8 and 1 <= rank <= 8:
                index = util.filerank_to_index(file, rank)
                target_piece = self.fen_list[index]
                if not target_piece:
                    moves.append(index)
                else:
                    target_color = 'w' if target_piece.isupper() else 'b'
                    if target_color != self.color:
                        moves.append(index)
        
        # up 2, right 1
        check_index(file + 1, rank + 2)
        # up 2, left 1
        check_index(file - 1, rank + 2)
        # down 2, right 1
        check_index(file + 1, rank - 2)
        # down 2, left 1
        check_index(file - 1, rank - 2)
        # up 1, right 2
        check_index(file + 2, rank + 1)
        # up 1, left 2
        check_index(file - 2, rank + 1)
        # down 1, right 2
        check_index(file + 2, rank - 1)
        # down 1, left 2
        check_index(file - 2, rank - 1)
        
        return moves
    