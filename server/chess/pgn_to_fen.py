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

# if __name__ == '__main__':
#     pgn = '[Event \"Mainz Rapid Final\"]\n[Site \"Mainz GER\"]\n[Date \"2007.08.19\"]\n[EventDate \"2007.08.19\"]\n[Round \"4\"]\n[Result \"0-1\"]\n[White \"The Levonator\"]\n[Black \"Vishy\"]\n[ECO \"E06\"]\n[WhiteElo \"2750\"]\n[BlackElo \"2792\"]\n[PlyCount \"136\"]\n\n1. d4 Nf6 2. c4 e6 3. g3 d5 4. Nf3 Be7 5. Bg2 O-O 6. O-O dxc4\n7. Qc2 a6 8. Qxc4 b5 9. Qc2 Bb7 10. Bd2 Ra7 11. Rc1 Be4\n12. Qb3 Nc6 13. e3 Qa8 14. Qd1 b4 15. Qf1 Rd8 16. Be1 a5\n17. a3 Bd6 18. Nfd2 Bxg2 19. Qxg2 Ra6 20. Nc4 Nd5 21. Nbd2\nbxa3 22. bxa3 Be7 23. Rab1 a4 24. Qf1 Nb8 25. Ne4 Nd7 26. Nc3\nc5 27. dxc5 Nxc3 28. Bxc3 Nxc5 29. Bb4 Bf8 30. Rd1 Rc8 31. Ne5\nRa7 32. Rbc1 Rac7 33. Qg2 Qxg2+ 34. Kxg2 f6 35. Nf3 e5 36. Ne1\nKf7 37. Rc4 Nb3 38. Rh4 Bxb4 39. Rxb4 Ra7 40. Kf3 Rc3 41. Nd3\nRc2 42. Rb6 Ra2 43. Nb4 Rxa3 44. Nc6 Rc7 45. Nd8+ Kg6 46. Ne6\nRe7 47. g4 Rxe6 48. Rxe6 Nd4+ 49. Rxd4 exd4 50. Re4 dxe3\n51. fxe3 Ra1 52. h3 a3 53. Ra4 a2 54. Kg2 Kf7 55. Ra6 Ke7\n56. e4 Kd7 57. h4 h6 58. g5 hxg5 59. hxg5 Kc7 60. Kh2 Kb7\n61. Ra3 Kc6 62. gxf6 gxf6 63. Rc3+ Kb5 64. Rc2 Kb4 65. Rf2\nRh1+ 66. Kxh1 a1=Q+ 67. Kg2 Kc4 68. Kf3 Kd3 0-1'
#     fen = pgn_to_fen(pgn)
#     print(fen)

#     pass

