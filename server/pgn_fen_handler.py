import re

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

def update_fen(fen, from_index, to_index):
    fen_list = fen_to_list(fen)
    piece = fen_list[from_index]
    fen_list[from_index] = None
    fen_list[to_index] = piece
    fen = list_to_fen(fen_list)
    return fen

def algebraic_to_index(fen, whites_turn, move):
    fen_list = fen_to_list(fen)

    # special case for promotion (=)

    # remove check, checkmate and capture
    move = move.replace('+', '')
    move = move.replace('#', '')
    move = move.replace('x', '')
    
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


def pgn_to_fen(pgn):
    pgn_dict = pgn_to_dict(pgn)
    move_list = pgn_dict['move_list']
    print(move_list)

pgn = '[Event "?"]\n[Site "?"]\n[Date "????.??.??"]\n[Round "?"]\n[White "?"]\n[Black "?"]\n[Result "*"]\n\n1. e4 e5 2. Nf3 Nc6 3. Bb5 *'
pgn2 = '[Event "Ultimate Blitz Challenge"]\n[Site "St. Louis, MO USA"]\n[Date "2016.04.29"]\n[EventDate "2016.04.28"]\n[Round "16.2"]\n[Result "1/2-1/2"]\n[White "SoSneaky"]\n[Black "KasparovKingKiller"]\n[ECO "A41"]\n[WhiteElo "?"]\n[BlackElo "?"]\n[PlyCount "91"]\n\n1. Nf3 g6 2. e4 Bg7 3. d4 d6 4. c4 Bg4 5. Be2 Nc6 6. Nbd2 e5\n7. d5 Nce7 8. O-O Nf6 9. c5 O-O 10. cxd6 cxd6 11. h3 Bd7\n12. Re1 b5 13. Bf1 Nc8 14. b3 Rb8 15. a4 a6 16. axb5 axb5\n17. Ba3 Ne8 18. Bb4 f5 19. Ra6 Bh6 20. exf5 Bxf5 21. g4 Bd7\n22. Ne4 Bf4 23. Bg2 Qe7 24. Qc2 Kh8 25. Qb2 Kg8 26. Qa3 h5\n27. Nxd6 Ncxd6 28. Bxd6 Nxd6 29. Qxd6 Qxd6 30. Rxd6 hxg4\n31. hxg4 e4 32. Rxd7 exf3 33. Bxf3 Bd2 34. Re2 Rxf3 35. Rxd2\nRxb3 36. d6 Rf3 37. Rc7 b4 38. Kg2 Rff8 39. Re2 Rfd8 40. Ree6\nb3 41. Rxg6+ Kh8 42. Rh6+ Kg8 43. Rg6+ Kf8 44. Rh6 Kg8\n45. Rg6+ Kf8 46. Rh6 1/2-1/2'

fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
fen = 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1'
