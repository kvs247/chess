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

def fen_to_dict(fen):
    fen_dict = {}

    fen_split = fen.split(' ')
    fen_dict['piece_placement'] = fen_split[0]
    fen_dict['active_color'] = fen_split[1]
    fen_dict['castling_availability'] = fen_split[2]
    fen_dict['en_passant_target_square'] = fen_split[3]
    fen_dict['halfmove_clock'] = int(fen_split[4])
    fen_dict['fullmove_number'] = int(fen_split[5])

    return fen_dict

def fen_from_dict(fen_dict):
    fen = ''
    fen += fen_dict['piece_placement'] + ' '
    fen += fen_dict['active_color'] + ' '
    fen += fen_dict['castling_availability'] + ' '
    fen += fen_dict['en_passant_target_square'] + ' '
    fen += str(fen_dict['halfmove_clock']) + ' '
    fen += str(fen_dict['fullmove_number'])

    return fen

def index_to_square(index):
    file, rank = index_to_filerank(index)
    return chr(file + 96) + str(rank)

def square_to_index(square):
    file = ord(square[0]) - 96
    rank = int(square[1])
    return filerank_to_index(file, rank)

def piece_placement_to_list(piece_placement):
    def helper(piece):
        if piece.isdigit():
            return [None] * int(piece)
        else:
            return piece
    piece_placement = piece_placement.replace('/', '')
    nested_list = list(map(lambda x: helper(x), piece_placement))
    piece_placement_list = []
    for sublist in nested_list:
        piece_placement_list.extend(sublist)
    return piece_placement_list

def piece_placement_list_to_string(pieces_list):
    piece_placement_string = ''
    for i in range(0, 64):
        if i % 8 == 0 and i != 0:
            piece_placement_string += '/'
        element = pieces_list[i]

        int_count = 0
        if element:
            piece_placement_string += element
        else:
            int_count += 1
            piece_placement_string += '1'
    
    # replace consecutive 1s with their sum
    for i in range(8, 0, -1):
        pattern  = '1' * i
        piece_placement_string = re.sub(pattern, str(i), piece_placement_string)

    return piece_placement_string

# algebraic/index conversion

def is_light_square(index):
    file, rank = index_to_filerank(index)
    if (file + rank) % 2 == 0:
        return False
    return True

def knight_moves(index):
    possible_moves = []
    file, rank = index_to_filerank(index)
    if 1 <= file + 2 <= 8 and 1 <= rank + 1 <= 8:
        possible_moves.append(filerank_to_index(file + 2, rank + 1))
    if 1 <= file + 2 <= 8 and 1 <= rank - 1 <= 8:
        possible_moves.append(filerank_to_index(file + 2, rank - 1))
    if 1 <= file - 2 <= 8 and 1 <= rank + 1 <= 8:
        possible_moves.append(filerank_to_index(file - 2, rank + 1))
    if 1 <= file - 2 <= 8 and 1 <= rank - 1 <= 8:
        possible_moves.append(filerank_to_index(file - 2, rank - 1))
    if 1 <= file + 1 <= 8 and 1 <= rank + 2 <= 8:
        possible_moves.append(filerank_to_index(file + 1, rank + 2))
    if 1 <= file + 1 <= 8 and 1 <= rank - 2 <= 8:
        possible_moves.append(filerank_to_index(file + 1, rank - 2))
    if 1 <= file - 1 <= 8 and 1 <= rank + 2 <= 8:
        possible_moves.append(filerank_to_index(file - 1, rank + 2))
    if 1 <= file - 1 <= 8 and 1 <= rank - 2 <= 8:
        possible_moves.append(filerank_to_index(file - 1, rank - 2))

    return possible_moves

def rook_moves(index, fen, whites_turn):
    possible_moves = []
    file, rank = index_to_filerank(index)
    fen_list = fen_to_list(fen)

    # up
    for i in range(rank + 1, 9):
        index = filerank_to_index(file, i)
        if not fen_list[index]:
            possible_moves.append(index)
        elif whites_turn and fen_list[index] == 'R':
            possible_moves.append(index)
            break
        elif not whites_turn and fen_list[index] == 'r':
            possible_moves.append(index)
            break
        elif fen_list[index]:
            break

    # down
    for i in range(rank - 1, 0, -1):
        index = filerank_to_index(file, i)
        if not fen_list[index]:
            possible_moves.append(index)
        elif whites_turn and fen_list[index] == 'R':
            possible_moves.append(index)
            break
        elif not whites_turn and fen_list[index] == 'r':
            possible_moves.append(index)
            break
        elif fen_list[index]:
            break

    # right
    for i in range(file + 1, 9):
        index = filerank_to_index(i, rank)
        if not fen_list[index]:
            possible_moves.append(index)
        elif whites_turn and fen_list[index] == 'R':
            possible_moves.append(index)
            break
        elif not whites_turn and fen_list[index] == 'r':
            possible_moves.append(index)
            break
        elif fen_list[index]:
            break

    # left
    for i in range(file - 1, 0, -1):
        index = filerank_to_index(i, rank)
        if not fen_list[index]:
            possible_moves.append(index)
        elif whites_turn and fen_list[index] == 'R':
            possible_moves.append(index)
            break
        elif not whites_turn and fen_list[index] == 'r':
            possible_moves.append(index)
            break
        elif fen_list[index]:
            break

    return possible_moves

def queen_moves(index, fen, whites_turn):
    # TODO needs diagonal aswell
    
    possible_moves = []
    file, rank = index_to_filerank(index)
    fen_list = fen_to_list(fen)

    # up
    for i in range(rank + 1, 9):
        index = filerank_to_index(file, i)
        if not fen_list[index]:
            possible_moves.append(index)
        elif whites_turn and fen_list[index] == 'Q':
            possible_moves.append(index)
            break
        elif not whites_turn and fen_list[index] == 'q':
            possible_moves.append(index)
            break
        elif fen_list[index]:
            break

    # down
    for i in range(rank - 1, 0, -1):
        index = filerank_to_index(file, i)
        if not fen_list[index]:
            possible_moves.append(index)
        elif whites_turn and fen_list[index] == 'Q':
            possible_moves.append(index)
            break
        elif not whites_turn and fen_list[index] == 'q':
            possible_moves.append(index)
            break
        elif fen_list[index]:
            break

    # right
    for i in range(file + 1, 9):
        index = filerank_to_index(i, rank)
        if not fen_list[index]:
            possible_moves.append(index)
        elif whites_turn and fen_list[index] == 'Q':
            possible_moves.append(index)
            break
        elif not whites_turn and fen_list[index] == 'q':
            possible_moves.append(index)
            break
        elif fen_list[index]:
            break

    # left
    for i in range(file - 1, 0, -1):
        index = filerank_to_index(i, rank)
        if not fen_list[index]:
            possible_moves.append(index)
        elif whites_turn and fen_list[index] == 'Q':
            possible_moves.append(index)
            break
        elif not whites_turn and fen_list[index] == 'q':
            possible_moves.append(index)
            break
        elif fen_list[index]:
            break

    return possible_moves

def algebraic_to_index(fen, move):
    # convert algebraic notation to index
    # returns (from_index, to_index)
    # UNLESS promotion, then ((from_index, to_index), promotion_type)

    fen_list = fen_to_list(fen)

    fen_dict = fen_to_dict(fen)

    whites_turn = True if fen_dict['active_color'] == 'w' else False

    # remove check, checkmate and capture
    move = move.replace('+', '')
    move = move.replace('#', '')
    move = move.replace('x', '')

    # promotion
    if '=' in move:
        to_file = ord(move[0]) - 96
        to_rank = int(move[1])
        to_index = filerank_to_index(to_file, to_rank)
        if whites_turn:
            from_index = to_index + 8
        else:
            from_index = to_index - 8

        promotion_type = move[3]
        if not whites_turn:
            promotion_type = promotion_type.lower()

        return (from_index, to_index), promotion_type

    # castling
    if move == 'O-O':
        if whites_turn:
            return 60, 62
        else:
            return 4, 6
    elif move == 'O-O-O':
        if whites_turn:
            return 60, 58
        else:
            return 4, 2

    to_rank = int(move[-1])
    to_file = ord(move[-2]) - 96
    to_index = filerank_to_index(to_file, to_rank)

    # pawn
    if move[0].lower() == move[0]:
        #capture
        if len(move) == 3:
            from_file = ord(move[0]) - 96
            if whites_turn:
                from_rank = to_rank - 1
            else:
                from_rank = to_rank + 1
            from_index = filerank_to_index(from_file, from_rank)
            return from_index, to_index
        # non capture
        if whites_turn:
            if fen_list[to_index + 8] == 'P':
                return to_index + 8, to_index
            elif fen_list[to_index + 16] == 'P':
                return to_index + 16, to_index
        else:
            if fen_list[to_index - 8] == 'p':
                return to_index - 8, to_index
            elif fen_list[to_index - 16] == 'p':
                return to_index - 16, to_index

    piece = move[0]
    if not whites_turn:
        piece = piece.lower()
    piece_indexes = [i for i, x in enumerate(fen_list) if x == piece]
    if len(piece_indexes) == 1:
        return piece_indexes[0], to_index
    
    # ambiguous move
    if len(move) == 4:
        if move[1].isdigit():
            given_rank = int(move[1])
        else:
            given_file = ord(move[1]) - 96

        for index in piece_indexes:
            file, rank = index_to_filerank(index)
            try:
                if file == given_file:
                    return index, to_index
            except:
                pass
            try:
                if rank == given_rank:
                    return index, to_index
            except:
                pass

    # knight
    if piece.upper() == 'N':
        possible_indexes = knight_moves(to_index)
        for index in piece_indexes:
            if index in possible_indexes:
                return index, to_index

    # bishop
    if piece.upper() == 'B':
        light_square = is_light_square(to_index)
        for index in piece_indexes:
            if is_light_square(index) == light_square:
                return index, to_index
    
    # rook
    if piece.upper() == 'R':
        possible_indexes = rook_moves(to_index, fen, whites_turn)
        for index in piece_indexes:
            if index in possible_indexes:
                return index, to_index
            
    # queen
    if piece.upper() == 'Q':
        possible_indexes = queen_moves(to_index, fen, whites_turn)
        for index in piece_indexes:
            if index in possible_indexes:
                return index, to_index

def index_to_algebraic(fen, from_index, to_index):
    fen_list = fen_to_list(fen)
    piece = fen_list[from_index]

    # need to implement check/checkmate +/#

    # ambiguos move for knight and rook
    # rook
    if piece.upper() == 'R':
        color = 'w' if piece == 'R' else 'b'
        if color == 'w':
            rook_indexes = [i for i, x in enumerate(fen_list) if x == 'R']
        else:
            rook_indexes = [i for i, x in enumerate(fen_list) if x == 'r']
        if len(rook_indexes) > 1:
            valid_rook_moves = rook_moves(to_index, fen, color == 'w')
            rook_indexes = [index for index in rook_indexes if index in valid_rook_moves]
            if len(rook_indexes) > 1:
                file, rank = index_to_filerank(to_index)
                to_square_algebraic = str(chr(file + 96)) + str(rank)
                # moved on file
                if abs(from_index - to_index) % 8 == 0:
                    return 'R' + str(index_to_filerank(from_index)[1]) + to_square_algebraic
                # moved on rank
                else:
                    return 'R' + str(chr(index_to_filerank(from_index)[0] + 96)) + to_square_algebraic
    # knight
    if piece.upper() == 'N':
        color = 'w' if piece == 'N' else 'b'
        if color == 'w':
            knight_indexes = [i for i, x in enumerate(fen_list) if x == 'N']
        else:
            knight_indexes = [i for i, x in enumerate(fen_list) if x == 'n']
        if len(knight_indexes) > 1:
            valid_knight_moves = knight_moves(to_index)
            knight_indexes = [index for index in knight_indexes if index in valid_knight_moves]
            if len(knight_indexes) > 1:
                to_file, to_rank = index_to_filerank(to_index)
                to_square_algebraic = str(chr(to_file + 96)) + str(to_rank)                
                # assuing there are only 2 knights
                # on same file
                if index_to_filerank(knight_indexes[0])[0] == index_to_filerank(knight_indexes[1])[0]:
                    return 'N' + str(index_to_filerank(from_index)[1]) + to_square_algebraic
                # on same rank
                else:
                    return 'N' + str(chr(index_to_filerank(from_index)[0] + 96)) + to_square_algebraic


    # en passant

    # castling
    if piece == 'K':
        if from_index == 60 and to_index == 62:
            return 'O-O'
        if from_index == 60 and to_index == 58:
            return 'O-O-O'
    if piece == 'k':
        if from_index == 4 and to_index == 6:
            return 'O-O'
        if from_index == 4 and to_index == 2:
            return 'O-O-O'

    # promotion
    # if fen_list[to_index] == 'P' and to_index < 8:
    #     return 'P' + index_to_filerank(from_index)[0] + 'x' + index_to_filerank(to_index)[0] + '=Q'
    # elif fen_list[to_index] == 'p' and to_index > 55:
    #     return 'p' + index_to_filerank(from_index)[0] + 'x' + index_to_filerank(to_index)[0] + '=q'

    # capture
    if fen_list[to_index]:
        # pawn
        if piece.upper() == 'P':
            from_file, _ = index_to_filerank(from_index)
            from_file_char = chr(from_file + 96)
            file, rank = index_to_filerank(to_index)
            file_char = chr(file + 96)
            return f'{from_file_char}x{file_char}{rank}'
        # not pawn
        else:
            piece_type = piece.upper()
            file, rank = index_to_filerank(to_index)
            file_char = chr(file + 96)
            return f'{piece_type}x{file_char}{rank}'            
    # non capture
    else:
        # pawn
        if piece.upper() == 'P':
            file, rank = index_to_filerank(to_index)
            file_char = chr(file + 96)
            return f'{file_char}{rank}'
        # not pawn
        else:
            piece_type = piece.upper()
            file, rank = index_to_filerank(to_index)
            file_char = chr(file + 96)
            return f'{piece_type}{file_char}{rank}'


# tests
if __name__ == '__main__':
    # test index_to_algebraic
    print('\n')
    print('index_to_algebraic tests:')
    # pawn move
    test = index_to_algebraic(
        'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
        52, 36
        )
    print('e4:', test)
    # regular move
    test = index_to_algebraic(
        'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
        62, 45
        )
    print('Nf3:', test)
    # pawn capture
    test = index_to_algebraic(
        'rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 2',
        36, 27
        )
    print('exd4:', test)
    # regular capture
    test = index_to_algebraic(
        'r1bqkbnr/pppppppp/2n5/4P3/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2',
        18, 28
        )
    print('Nxe5:', test)
    # castling
    test = index_to_algebraic(
        'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
        60, 63
        )
    print('O-O:', test)
    test = index_to_algebraic(
        'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
        4, 2
        )
    print('O-O-O:', test)
    test = index_to_algebraic(
        'rnbqkb1r/pppppppp/7n/8/4P3/8/PPPPKPPP/RNBQNB1R b kq - 6 4',
        60, 58
        )
    print('Nxc1:', test)
    test = index_to_algebraic(
        'r6r/pppppppp/n1n2k2/8/8/N1N2K2/PPPPPPPP/R6R w - - 0 1',
        56, 58
    )
    print('Rac1:', test)
    test = index_to_algebraic(
        'r6r/pppppppp/n1n2k2/8/8/N1N2K2/PPPPPPPP/R6R w - - 0 1',
        63, 60
    )
    print('Rhe1:', test)    
    test = index_to_algebraic(
        'k7/p1r3r1/8/8/2r3r1/8/P5r1/K7 b - - 0 1',
        10, 26
    )
    print('R7c5:', test)
    test = index_to_algebraic(
        'rnbqkbnr/pppppppp/8/8/8/2N1N3/PPPPPPPP/R1BQKB1R w KQkq - 0 1',
        44, 27
    )
    print('Ned5:', test)
    test = index_to_algebraic(
        'r1bqkb1r/pppppppp/6n1/8/6n1/P7/1PPPPPPP/RNBQKBNR b KQkq - 0 1',
        22, 28
    )
    print('N6e5:', test)

    print('\n')

    