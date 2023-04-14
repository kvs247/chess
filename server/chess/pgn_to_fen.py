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
    pgn = '"[Date \"2023.04.14\"]\n[Result \"*\"]\n[White \"Kye_Schnei\"]\n[Black \"topherLud\"]\n\n1. Nh3 Nh6 2. Ng1 Ng8 3. Nh3 Nh6 4. Ng1 Ng8 5. Nh3 Nh6 6. Ng1 Ng8 \n7. Nh3 Nh6 8. Ng1 Ng8 9. Nh3 Nh6 10. Ng1 Ng8 11. Nh3 Nh6 12. Ng1 Ng8 \n13. Nh3 Nh6 14. Ng1 Ng8 15. Nh3 Nh6 16. Nf4 Ng4 17. Nh5 Ne5 \n18. Ng3 Ng4 19. Nf5 Ne5 20. Ne3 Ng4 21. Nf5 Ne5 22. Ne3 Ng4 \n23. Nf5 Ne5 24. Nd4 Ng4 25. Nf5 Ne3 26. Nd4 Nf5 27. Nf3 Nh4 \n28. Ng5 Nf5 29. Ne4 Nd4 30. Nc5 Nf5 31. Nd3 Nd4 32. Nf4 Ne6 \n33. Nd5 Nf4 34. Ne3 Nd5 35. Nf5 Ne3 36. Nd4 Nd5 37. Nf5 Ne3 \n38. Nd4 Nd5 39. Nf5 Ne3 40. Nd4 Nd5 41. Nf5 Ne3 42. Nd4 Nf5 \n43. Nf3 Nd4 44. Ne5 Nf5 45. Nf3 Nd4 46. Ne5 Nf5 47. Nf3 Nd4 \n48. Ne5 Nf3+ 49. exf3 Na6 50. Nc4 Nc5 51. Na5 Na4 52. Nc4 Nc5 \n53. Na5 Na4 54. Nc4 Nc5 55. Na5 Na4 56. Nc4 Nc5 57. Na5 Na4 \n58. Nc4 Nc5 59. Na5 Na4 60. Nc4 Nc5 61. Na5 Na4 62. Nc4 Nc5 \n63. Na5 Na4 64. Nc4 Nc5 65. Na5 Na4 66. Nc4 Nc5 67. Na5 Na4 \n68. Nc4 Nc5 69. Na5 Na4 70. Nc4 Nc5 71. Na5 Na4 72. Nc4 Nc5 \n73. Na5 Na4 74. Nc4 Nc5 75. Na5 Na4 76. Nc4 Nc5 77. Na5 Na4 \n78. Nc4 Nc5 79. Na5 Na4 80. Nc4 Nc5 81. Na5 Na4 82. Nc4 Nc5 \n83. Na5 Na4 84. Nc4 Nc5 85. Na5 Na4 86. Nc4 Nc5 87. Na5 Na4 \n88. Nc4 Nc5 89. Na5 Na4 90. Nc4 Nc5 91. Na5 Na4 92. Nc4 Nc5 \n93. Na5 Na4 94. Nc4 Nc5 95. Na5 Na4 96. Nc4 Nc5 97. Na5 Na4 \n98. Nc4 Nc5 *"'
    # fen = pgn_to_fen(pgn)
    fen_list = pgn_to_fen_store(pgn)
    print(fen_list)

    pass

