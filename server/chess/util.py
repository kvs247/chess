import re

def filerank_to_index(file, rank):
    return (8 - (rank - 1) - 1) * 8 + (file - 1)

def index_to_filerank(index):
    rank = 8 - (index // 8)
    file = (index % 8) + 1
    return file, rank

def fen_to_list(fen):
    def helper(piece):
        if piece.isdigit():
            return [None] * int(piece)
        else:
            return piece
    pieces_string = fen.split(' ')[0].replace('/', '')
    pieces_list_nums = list(pieces_string)
    pieces_list = list(map(lambda piece: helper(piece), pieces_list_nums))
    pieces_list = [item for sublist in pieces_list for item in sublist]

    return pieces_list

def list_to_fen(pieces_list):
    fen = ''
    for i in range(0, 64):
        if i % 8 == 0 and i != 0:
            fen += '/'
        element = pieces_list[i]

        int_count = 0
        if element:
            fen += element
        else:
            int_count += 1
            fen += '1'
    
    # replace consecutive 1s with their sum
    for i in range(8, 0, -1):
        pattern  = '1' * i
        fen = re.sub(pattern, str(i), fen)

    return fen

