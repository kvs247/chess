import re

try:
    from chess import util
except ImportError:
    import util # for testing

def pgn_to_dict(pgn):
    pgn_dict = {}

    date = re.search(r'Date "(.*)"', pgn).group(1)
    pgn_dict['date'] = date
    
    result = re.search(r'Result "(.*)"', pgn).group(1)
    pgn_dict['result'] = result

    white_username = re.search(r'White "(.*)"', pgn).group(1)
    pgn_dict['white_username'] = white_username

    black_username = re.search(r'Black "(.*)"', pgn).group(1)
    pgn_dict['black_username'] = black_username

    pgn_split = pgn.split('\n')
    move_list_split = pgn_split[pgn_split.index('') + 1:]
    move_list = ' '.join(move_list_split)
    pgn_dict['move_list'] = move_list

    return pgn_dict

def update_fen(fen, from_index, to_index, promotion_type=None):
    fen_dict = util.fen_to_dict(fen)
    piece_placement_list = util.piece_placement_to_list(fen_dict['piece_placement'])
    piece_type = piece_placement_list[from_index]
    
    new_fen_dict = fen_dict.copy()

    # piece_placement
    new_piece_placement_list = piece_placement_list.copy()
    new_piece_placement_list[to_index] = piece_placement_list[from_index]
    new_piece_placement_list[from_index] = None
    # promotion
    if promotion_type:
        new_piece_placement_list[to_index] = promotion_type
    # castling
    if piece_type == 'K':
        if from_index == 60 and to_index == 62:
            new_piece_placement_list[61] = 'R'
            new_piece_placement_list[63] = None
        if from_index == 60 and to_index == 58:
            new_piece_placement_list[59] = 'R'
            new_piece_placement_list[56] = None
    if piece_type == 'k':
        if from_index == 4 and to_index == 6:
            new_piece_placement_list[5] = 'r'
            new_piece_placement_list[7] = None
        if from_index == 4 and to_index == 2:
            new_piece_placement_list[3] = 'r'
            new_piece_placement_list[0] = None
    # en passant
    if fen_dict['en_passant_target_square'] != '-':
        en_passant_target_index = util.square_to_index(fen_dict['en_passant_target_square'])
        if piece_type == 'P' and to_index == en_passant_target_index :
            new_piece_placement_list[en_passant_target_index + 8] = None
        if piece_type == 'p' and to_index == en_passant_target_index :
            new_piece_placement_list[en_passant_target_index - 8] = None
    new_fen_dict['piece_placement'] = util.piece_placement_list_to_string(new_piece_placement_list)

    # active_color
    if fen_dict['active_color'] == 'w':
        new_fen_dict['active_color'] = 'b'
    else:  
        new_fen_dict['active_color'] = 'w'

    # castling_availability
    castling_availability = fen_dict['castling_availability']
    if piece_type == 'K':
        new_fen_dict['castling_availability'] = castling_availability.replace('K', '').replace('Q', '')
    if piece_type == 'k':
        new_fen_dict['castling_availability'] = castling_availability.replace('k', '').replace('q', '')
    if piece_type == 'R' and from_index == 63:
        new_fen_dict['castling_availability'] = castling_availability.replace('K', '')
    if piece_type == 'R' and from_index == 56:
        new_fen_dict['castling_availability'] = castling_availability.replace('Q', '')
    if piece_type == 'r' and from_index == 7:
        new_fen_dict['castling_availability'] = castling_availability.replace('k', '')
    if piece_type == 'r' and from_index == 0:
        new_fen_dict['castling_availability'] = castling_availability.replace('q', '')
    if new_fen_dict['castling_availability'] == '':
        new_fen_dict['castling_availability'] = '-'

    # en_passant_target_square
    if piece_type.upper() == 'P' and abs(to_index - from_index) == 16:
        en_passant_target_index = min(to_index, from_index) + 8
        en_passant_target_square = util.index_to_square(en_passant_target_index)
        new_fen_dict['en_passant_target_square'] = en_passant_target_square
    else:
        new_fen_dict['en_passant_target_square'] = '-'

    # halfmove_clock
    if piece_type.upper() == 'P' or piece_placement_list[to_index] != None:
        new_fen_dict['halfmove_clock'] = 0
    else:
        new_fen_dict['halfmove_clock'] = fen_dict['halfmove_clock'] + 1

    # fullmove_number
    if fen_dict['active_color'] == 'b':
        new_fen_dict['fullmove_number'] = fen_dict['fullmove_number'] + 1

    return util.fen_from_dict(new_fen_dict)

def pgn_to_fen(pgn):
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    pgn_dict = pgn_to_dict(pgn)
    move_list = pgn_dict['move_list']
    if not move_list:
        return fen
    move_list = move_list.split(' ')
    # print(move_list)
    if move_list == ['*']:  # new game
        return fen
    move_list = [m for m in move_list if m[0].isalpha()]

    for move in move_list:
        from_index, to_index = util.algebraic_to_index(fen, move)
        # promotion
        if type(from_index) == tuple:
            promotion_type = to_index
            from_index, to_index = from_index
            fen = update_fen(fen, from_index, to_index, promotion_type)
        else:
            fen = update_fen(fen, from_index, to_index)
        
    return fen

if __name__ == '__main__':
    pgn = '[Event \"World Rapid Championship\"]\n[Site \"Dubai UAE\"]\n[Date \"1980.06.18\"]\n[EventDate \"2014.06.16\"]\n[Round \"13.1\"]\n[Result \"*\"]\n[White \"Vishy\"]\n[Black \"FabulousFabiano\"]\n[ECO \"C11\"]\n[WhiteElo \"2770\"]\n[BlackElo \"2840\"]\n[PlyCount \"125\"]\n\n *'
    fen = pgn_to_fen(pgn)
    print(fen)

    pass

