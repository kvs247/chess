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
    move_list = [m for m in move_list if m != '']
    move_list = [m for m in move_list if m[0].isalpha()]

    for move in move_list:
        # print(move)
        # print(fen)
        # print(util.algebraic_to_index(fen, move))
        from_index, to_index = util.algebraic_to_index(fen, move)
        # promotion
        if type(from_index) == tuple:
            promotion_type = to_index
            from_index, to_index = from_index
            fen = update_fen(fen, from_index, to_index, promotion_type)
        else:
            fen = update_fen(fen, from_index, to_index)
        
    return fen

def pgn_to_fen_store(pgn):
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    result = [fen]
    pgn_dict = pgn_to_dict(pgn)
    move_list = pgn_dict['move_list']
    if not move_list:
        return result
    move_list = move_list.split(' ')
    if move_list == ['*']:  # new game
        return result
    move_list = [m for m in move_list if m != '']
    move_list = [m for m in move_list if m[0].isalpha()]

    for move in move_list:
        # print('pgn_to_fen.py:', move)
        from_index, to_index = util.algebraic_to_index(fen, move)
        # promotion
        if type(from_index) == tuple:
            promotion_type = to_index
            from_index, to_index = from_index
            fen = update_fen(fen, from_index, to_index, promotion_type)
            result.append(fen)
        else:
            fen = update_fen(fen, from_index, to_index)
            result.append(fen)
        
    return result

if __name__ == '__main__':
    pgn = '[Event \"Live Chess\"]\n[Site \"Chess.com\"]\n[Date \"2023.04.13\"]\n[Round \"?\"]\n[White \"Kye_Schnei\"]\n[Black \"twocupterry\"]\n[Result \"1/2-1/2\"]\n[ECO \"C44\"]\n[WhiteElo \"764\"]\n[BlackElo \"759\"]\n[TimeControl \"60+1\"]\n[EndTime \"8:45:49 PDT\"]\n[Termination \"Game drawn by stalemate\"]\n\n1. e4 e5 2. Nf3 Nc6 3. g3 Nf6 4. d3 Bc5 5. Bg2 d6 6. Bg5 h6 7. Bh4 g5 8. Nxg5\nhxg5 9. Bxg5 Rg8 10. Bxf6 Qxf6 11. Qf3 Qxf3 12. Bxf3 Bh3 13. Nd2 O-O-O 14. O-O-O\nf5 15. Nc4 Bxf2 16. d4 f4 17. gxf4 exf4 18. d5 Be3+ 19. Kb1 Nd4 20. Rxd4 Bxd4\n21. Rd1 Be3 22. Rd3 Rg1+ 23. Rd1 Rxd1+ 24. Bxd1 Rg8 25. Nxe3 Rg1 26. Kc1 Kd7 27.\nNc4 Bg4 28. Kd2 Rxd1+ 29. Kc3 b5 30. Na5 c5 31. Kb3 Rd2 32. Nb7 Kc7 33. Na5 Kb6\n34. Kc3 Kxa5 35. Kxd2 b4 36. b3 f3 37. Ke1 Bh3 38. Kf2 Bg4 39. h3 Bh5 40. e5 Kb6\n41. exd6 Bg6 42. h4 Kb7 43. h5 Bxh5 44. Kg3 a6 45. Kh4 a5 46. Kxh5 c4 47. Kh4 f2\n48. d7 Kc7 49. d8=Q+ Kxd8 50. d6 f1=Q 51. d7 Kxd7 52. Kg5 Qc1+ 53. Kg6 Qxc2+ 54.\nKf6 Qxa2 55. Kf5 Qxb3 56. Ke4 a4 57. Ke5 a3 58. Kf5 a2 59. Kf4 a1=Q 60. Kg4 c3\n61. Kg5 c2 62. Kf5 c1=Q 63. Ke4 Qba3 64. Kf5 b3 65. Kg6 b2 66. Kf6 b1=Q+ 67. Kf7\nQad3 68. Kf8 Qe1 69. Kg8 Qbb4 70. Kf7 Qf4+ 71. Kg8 Qae5 1/2-1/2'
    fen = pgn_to_fen(pgn)
    # fen_list = pgn_to_fen_store(pgn)
    # print(fen_list)

    pass

