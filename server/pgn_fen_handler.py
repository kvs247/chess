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

def rook_moves(index, fen, whites_turn):
    possible_moves = []
    file, rank = util.index_to_filerank(index)
    fen_list = util.fen_to_list(fen)

    # up
    for i in range(rank + 1, 9):
        index = util.filerank_to_index(file, i)
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
        index = util.filerank_to_index(file, i)
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
        index = util.filerank_to_index(i, rank)
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
        index = util.filerank_to_index(i, rank)
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

def algebraic_to_index(fen, whites_turn, move):
    # convert algebraic notation to index
    # returns (from_index, to_index)
    # UNLESS promotion, then (promotion_type, to_index)

    fen_list = util.fen_to_list(fen)

    # remove check, checkmate and capture
    move = move.replace('+', '')
    move = move.replace('#', '')
    move = move.replace('x', '')

    # promotion
    if '=' in move:
        to_file = ord(move[0]) - 96
        to_rank = int(move[1])
        to_index = util.filerank_to_index(to_file, to_rank)

        promotion_type = move[3]
        if not whites_turn:
            promotion_type = promotion_type.lower()

        return promotion_type, to_index

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
        possible_indexes = rook_moves(to_index, fen, whites_turn)
        for index in piece_indexes:
            if index in possible_indexes:
                return index, to_index
            
def update_fen(fen, from_index, to_index):
    fen_list = util.fen_to_list(fen)
    piece = fen_list[from_index]
    fen_list[from_index] = None
    fen_list[to_index] = piece
    fen = util.list_to_fen(fen_list)
    return fen

def update_fen_promotion(fen, to_index, promotion_type, whites_turn):
    fen_list = util.fen_to_list(fen)
    if whites_turn:
        fen_list[to_index + 8] = None
    else:
        fen_list[to_index - 8] = None
    fen_list[to_index] = promotion_type
    fen = util.list_to_fen(fen_list)
    return fen

def pgn_to_fen(pgn):
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    pgn_dict = pgn_to_dict(pgn)
    move_list = pgn_dict['move_list']
    move_list = move_list.split(' ')
    move_list = [m for m in move_list if m[0].isalpha()]

    whites_turn = True
    i = 1
    for move in  move_list:
        from_index, to_index = algebraic_to_index(fen, whites_turn, move)
        # promotion
        if type(from_index) == str:
            fen = update_fen_promotion(fen, to_index, from_index, whites_turn)
            whites_turn = not whites_turn
            continue
        fen_list = util.fen_to_list(fen)
        # castling
        if from_index == 60 and to_index == 62:
            if fen_list[60] == 'K':
                fen = update_fen(fen, 63, 61) + ' w KQkq - 0 1'
        if from_index == 60 and to_index == 58:
            if fen_list[60] == 'K':
                fen = update_fen(fen, 56, 59) + ' w KQkq - 0 1'
        if from_index == 4 and to_index == 6:
            if fen_list[4] == 'k':
                fen = update_fen(fen, 7, 5) + ' w KQkq - 0 1'
        if from_index == 4 and to_index == 2:
            if fen_list[4] == 'k':
                fen = update_fen(fen, 0, 3) + ' w KQkq - 0 1'

        fen = update_fen(fen, from_index, to_index) + ' w KQkq - 0 1'
        
        whites_turn = not whites_turn

        i += 1

    return fen

if __name__ == '__main__':
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

    pgn = '''[Event "Kasparov - Anand PCA World Championship Match"]
    [Site "New York, NY USA"]
    [Date "1995.09.19"]
    [EventDate "?"]
    [Round "6"]
    [Result "1/2-1/2"]
    [White "KasparovKingKiller"]
    [Black "Vishy"]
    [ECO "C80"]
    [WhiteElo "?"]
    [BlackElo "?"]
    [PlyCount "55"]

    1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3
    d5 8.dxe5 Be6 9.Nbd2 Nc5 10.c3 d4 11.Ng5 dxc3 12.Nxe6 fxe6
    13.bxc3 Qd3 14.Nf3 O-O-O 15.Qe1 Nxb3 16.axb3 Kb7 17.Be3 Be7
    18.Bg5 h6 19.Bxe7 Nxe7 20.Nd4 Rxd4 21.cxd4 Qxb3 22.Qe3 Qxe3
    23.fxe3 Nd5 24.Kf2 Kb6 25.Ke2 a5 26.Rf7 a4 27.Kd2 c5 28.e4
    1/2-1/2'''

    pgn = '[Event "Reykjavik Rapid"]\n[Site "Reykjavik ISL"]\n[Date "2004.03.18"]\n[EventDate "2004.03.17"]\n[Round "1.2"]\n[Result "1-0"]\n[White "KasparovKingKiller"]\n[Black "DrDrunkenstein"]\n[ECO "E92"]\n[WhiteElo "2831"]\n[BlackElo "2484"]\n[PlyCount "63"]\n\n1. c4 Nf6 2. Nc3 g6 3. e4 d6 4. d4 Bg7 5. Nf3 O-O 6. Be2 e5\n7. Be3 exd4 8. Nxd4 c6 9. f3 Re8 10. Bf2 d5 11. exd5 cxd5\n12. c5 Nc6 13. O-O Nh5 14. Qd2 Be5 15. g3 Bh3 16. Rfe1 Ng7\n17. Rad1 Rc8 18. Ndb5 a6 19. Nd6 Bxd6 20. cxd6 d4\n21. Ne4 Bf5 22. d7 Bxd7 23. Bxd4 Nxd4 24. Qxd4 Nf5\n25. Qxd7 Qb6+ 26. Kh1 Red8 27. Qa4 Rxd1 28. Qxd1 Qxb2\n29. Qb1 Rc2 30. Qxb2 Rxb2\n31. Bc4 Nd4 32. Re3 1-0'

    print(pgn_to_fen(pgn))