import re

def read_pgn(pgn_str):
    pgn_dict = {}

    date = re.search(r'Date "(.*)"', pgn_str).group(1)
    pgn_dict['date'] = date
    
    result = re.search(r'Result "(.*)"', pgn_str).group(1)
    pgn_dict['result'] = result

    white_username = re.search(r'White "(.*)"', pgn_str).group(1)
    pgn_dict['white_username'] = white_username

    black_username = re.search(r'Black "(.*)"', pgn_str).group(1)
    pgn_dict['black_username'] = black_username

    pgn_split = pgn_str.split('\n')
    move_list_split = pgn_split[pgn_split.index('') + 1:]
    move_list = ' '.join(move_list_split)
    pgn_dict['move_list'] = move_list

    return pgn_dict

# x = read_pgn('.data/PGNs/topherLud_vs_Kye_Schnei_2023.03.24.pgn')

# print(x['move_list'])