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
    if not move_list:
        return fen
    move_list = move_list.split(' ')
    move_list = [m for m in move_list if m[0].isalpha()]

    whites_turn = True
    castling_rights = 'KQkq'
    half_move = 0
    full_move = 1
    en_passant = '-'
    for move in  move_list:
        # print(fen)
        promotion = False
        from_index, to_index = util.algebraic_to_index(fen, whites_turn, move)

        # promotion
        if type(from_index) == str:
            fen = update_fen_promotion(fen, to_index, from_index, whites_turn)
            promotion = True
        fen_list = util.fen_to_list(fen)
        if not promotion:
            piece = fen_list[from_index]
            target_piece = fen_list[to_index]
        else:
            piece = 'P' if whites_turn else 'p'
            target_piece = None

        # castling  
        if from_index == 60 and to_index == 62:
            if fen_list[60] == 'K':
                fen = update_fen(fen, 63, 61)
                castling_rights = castling_rights.replace('K', '')
                castling_rights = castling_rights.replace('Q', '')
        if from_index == 60 and to_index == 58:
            if fen_list[60] == 'K':
                fen = update_fen(fen, 56, 59)
                castling_rights = castling_rights.replace('K', '')
                castling_rights = castling_rights.replace('Q', '')
        if from_index == 4 and to_index == 6:
            if fen_list[4] == 'k':
                fen = update_fen(fen, 7, 5)
                castling_rights = castling_rights.replace('k', '')
                castling_rights = castling_rights.replace('q', '')
        if from_index == 4 and to_index == 2:
            if fen_list[4] == 'k':
                fen = update_fen(fen, 0, 3)
                castling_rights = castling_rights.replace('k', '')
                castling_rights = castling_rights.replace('q', '')

        # castling rights   
        if piece == 'K':
            castling_rights = castling_rights.replace('K', '')
            castling_rights = castling_rights.replace('Q', '')
        if piece == 'k':
            castling_rights = castling_rights.replace('k', '')
            castling_rights = castling_rights.replace('q', '')
        if piece == 'R' and from_index == 56:
            castling_rights = castling_rights.replace('Q', '')
        if piece == 'R' and from_index == 63:
            castling_rights = castling_rights.replace('K', '')
        if piece == 'r' and from_index == 0:
            castling_rights = castling_rights.replace('q', '')
        if piece == 'r' and from_index == 7:
            castling_rights = castling_rights.replace('k', '')

        # apply en passant
        if en_passant != '-':
            en_peasent_file = ord(en_passant[0]) - 96
            en_peasent_rank = int(en_passant[1])
            en_peasent_index = util.filerank_to_index(en_peasent_file, en_peasent_rank)
            if piece == 'P' and to_index == en_peasent_index:
                fen_list[en_peasent_index + 8] = None
                fen = util.list_to_fen(fen_list)
            if piece == 'p' and to_index == en_peasent_index:
                fen_list[en_peasent_index - 8] = None
                fen = util.list_to_fen(fen_list)

        # update fen
        if not promotion:
            fen = update_fen(fen, from_index, to_index)
        # set player turn
        whites_turn = not whites_turn
        turn = 'w' if whites_turn else 'b'
        # set castling rights
        if castling_rights == '':
            castling_rights = '-'
        # set full move
        if turn == 'w':
            full_move += 1
        # set halfmove
        if piece == 'p' or piece == 'P':
            half_move = 0
        if target_piece != None:
            half_move = 0
        # set en passant
        en_passant = '-'
        if not promotion:
            if piece == 'p' or piece == 'P':
                if abs(from_index - to_index) == 16 or abs(to_index - from_index) == 16:
                    index = min(from_index, to_index) + 8
                    file, rank = util.index_to_filerank(index)
                    file = chr(file + 96)
                    en_passant = f'{file}{rank}'

        fen += f' {turn} {castling_rights} {en_passant} {half_move} {full_move}' 

        half_move += 1

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

    pgn = '[Event \"Reykjavik Rapid\"]\n[Site \"Reykjavik ISL\"]\n[Date \"2004.03.18\"]\n[EventDate \"2004.03.17\"]\n[Round \"1.2\"]\n[Result \"1-0\"]\n[White \"KasparovKingKiller\"]\n[Black \"DrDrunkenstein\"]\n[ECO \"E92\"]\n[WhiteElo \"2831\"]\n[BlackElo \"2484\"]\n[PlyCount \"63\"]\n\n'   
    x = pgn_to_fen(pgn)
    print('final position:')
    print(x)