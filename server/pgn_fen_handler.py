import re

import util

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



def is_light_square(index):
    file, rank = util.index_to_filerank(index)
    if (file + rank) % 2 == 0:
        return False
    return True

def knight_moves(index):
    possible_moves = []
    file, rank = util.index_to_filerank(index)
    if 1 <= file + 2 <= 8 and 1 <= rank + 1 <= 8:
        possible_moves.append(util.filerank_to_index(file + 2, rank + 1))
    if 1 <= file + 2 <= 8 and 1 <= rank - 1 <= 8:
        possible_moves.append(util.filerank_to_index(file + 2, rank - 1))
    if 1 <= file - 2 <= 8 and 1 <= rank + 1 <= 8:
        possible_moves.append(util.filerank_to_index(file - 2, rank + 1))
    if 1 <= file - 2 <= 8 and 1 <= rank - 1 <= 8:
        possible_moves.append(util.filerank_to_index(file - 2, rank - 1))
    if 1 <= file + 1 <= 8 and 1 <= rank + 2 <= 8:
        possible_moves.append(util.filerank_to_index(file + 1, rank + 2))
    if 1 <= file + 1 <= 8 and 1 <= rank - 2 <= 8:
        possible_moves.append(util.filerank_to_index(file + 1, rank - 2))
    if 1 <= file - 1 <= 8 and 1 <= rank + 2 <= 8:
        possible_moves.append(util.filerank_to_index(file - 1, rank + 2))
    if 1 <= file - 1 <= 8 and 1 <= rank - 2 <= 8:
        possible_moves.append(util.filerank_to_index(file - 1, rank - 2))

    return possible_moves

def algebraic_to_index(fen, whites_turn, move):
    fen_list = util.fen_to_list(fen)

    # special case for promotion (=)

    # remove check, checkmate and capture
    move = move.replace('+', '')
    move = move.replace('#', '')
    move = move.replace('x', '')

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
    to_index = util.filerank_to_index(to_file, to_rank)

    # pawn
    if move[0].lower() == move[0]:
        #capture
        if len(move) == 3:
            from_file = ord(move[0]) - 96
            if whites_turn:
                from_rank = to_rank - 1
            else:
                from_rank = to_rank + 1
            from_index = util.filerank_to_index(from_file, from_rank)
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
            file, rank = util.index_to_filerank(index)
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
        for index in piece_indexes:
            file, rank = util.index_to_filerank(index)
            if file == to_file or rank == to_rank:
                return index, to_index
            
def update_fen(fen, from_index, to_index):
    fen_list = util.fen_to_list(fen)
    piece = fen_list[from_index]
    fen_list[from_index] = None
    fen_list[to_index] = piece
    fen = util.list_to_fen(fen_list)
    return fen

def pgn_to_fen(pgn):
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    pgn_dict = pgn_to_dict(pgn)
    move_list = pgn_dict['move_list']
    move_list = move_list.split(' ')
    move_list = [m for m in move_list if m[0].isalpha()]
    
    whites_turn = True
    for move in  move_list:
        from_index, to_index = algebraic_to_index(fen, whites_turn, move)
        fen = update_fen(fen, from_index, to_index) + ' w KQkq - 0 1'
        # castling
        if from_index == 60 and to_index == 62:
            fen = update_fen(fen, 63, 61) + ' w KQkq - 0 1'
        if from_index == 60 and to_index == 58:
            fen = update_fen(fen, 56, 59) + ' w KQkq - 0 1'
        if from_index == 4 and to_index == 6:
            fen = update_fen(fen, 7, 5) + ' w KQkq - 0 1'
        if from_index == 4 and to_index == 2:
            fen = update_fen(fen, 0, 3) + ' w KQkq - 0 1'

        whites_turn = not whites_turn

    return fen

# pgn = '''[Event "?"]
# [Site "?"]
# [Date "????.??.??"]
# [Round "?"]
# [White "?"]
# [Black "?"]
# [Result "*"]

# 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 b5 5. Bb3 Nf6 6. Qe2 Nxe4 7. Qxe4 Bc5 8.
# Nxe5 Nxe5 9. Qxe5+ Kf8 10. d3 Qg5 11. Bxg5 Bxf2+ 12. Kxf2 Bb7 13. Nc3 Bxg2 14.
# Kxg2 Re8 15. Rhe1 Rxe5 16. Rxe5 d6 17. Rae1 dxe5 18. Rxe5 *'''

pgn = '''
[Event "Ultimate Blitz Challenge"]
[Site "St. Louis, MO USA"]
[Date "2016.04.29"]
[EventDate "2016.04.28"]
[Round "16.2"]
[Result "1/2-1/2"]
[White "SoSneaky"]
[Black "KasparovKingKiller"]
[ECO "A41"]
[WhiteElo "?"]
[BlackElo "?"]
[PlyCount "91"]

1. Nf3 g6 2. e4 Bg7 3. d4 d6 4. c4 Bg4 5. Be2 Nc6 6. Nbd2 e5
7. d5 Nce7 8. O-O Nf6 9. c5 O-O 10. cxd6 cxd6 11. h3 Bd7
12. Re1 b5 13. Bf1 Nc8 14. b3 Rb8 15. a4 a6 16. axb5 axb5
17. Ba3 Ne8 18. Bb4 f5 19. Ra6 Bh6 20. exf5 Bxf5 21. g4 Bd7
22. Ne4 Bf4 23. Bg2 Qe7 24. Qc2 Kh8 25. Qb2 Kg8 26. Qa3 h5
27. Nxd6 Ncxd6 28. Bxd6 Nxd6 29. Qxd6 Qxd6 30. Rxd6 hxg4
31. hxg4 e4 32. Rxd7 exf3 33. Bxf3 Bd2 34. Re2 Rxf3 35. Rxd2
Rxb3 36. d6 Rf3 37. Rc7 b4 38. Kg2 Rff8 39. Re2 Rfd8 40. Re6
b3 41. Rxg6+ Kh8 42. Rh6+ Kg8 43. Rg6+ Kf8 44. Rh6 Kg8
45. Rg6+ Kf8 46. Rh6 1/2-1/2
'''

pgn = '[Event "Ultimate Blitz Challenge"]\n[Site "St. Louis, MO USA"]\n[Date "2016.04.29"]\n[EventDate "2016.04.28"]\n[Round "16.2"]\n[Result "1/2-1/2"]\n[White "SoSneaky"]\n[Black "KasparovKingKiller"]\n[ECO "A41"]\n[WhiteElo "?"]\n[BlackElo "?"]\n[PlyCount "91"]\n\n1. Nf3 g6 2. e4 Bg7 3. d4 d6 4. c4 Bg4 5. Be2 Nc6 6. Nbd2 e5\n7. d5 Nce7 8. O-O Nf6 9. c5 O-O 10. cxd6 cxd6 11. h3 Bd7\n12. Re1 b5 13. Bf1 Nc8 14. b3 Rb8 15. a4 a6 16. axb5 axb5\n17. Ba3 Ne8 18. Bb4 f5 19. Ra6 Bh6 20. exf5 Bxf5 21. g4 Bd7\n22. Ne4 Bf4 23. Bg2 Qe7 24. Qc2 Kh8 25. Qb2 Kg8 26. Qa3 h5\n27. Nxd6 Ncxd6 28. Bxd6 Nxd6 29. Qxd6 Qxd6 30. Rxd6 hxg4\n31. hxg4 e4 32. Rxd7 exf3 33. Bxf3 Bd2 34. Re2 Rxf3 35. Rxd2\nRxb3 36. d6 Rf3 37. Rc7 b4 38. Kg2 Rff8 39. Re2 Rfd8 40. Ree6\nb3 41. Rxg6+ Kh8 42. Rh6+ Kg8 43. Rg6+ Kf8 44. Rh6 Kg8\n45. Rg6+ Kf8 46. Rh6 1/2-1/2'

print(pgn_to_fen(pgn))