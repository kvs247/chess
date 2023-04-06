import re

def read_pgn(pgn):
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

x = read_pgn('[Date "2023.03.24"]\n[White "topherLud"]\n[Black "Kye_Schnei"]\n[Result "0-1"]\n[ECO "C46"]\n[WhiteElo "381"]\n[BlackElo "1098"]\n[TimeControl "1/86400"]\n[EndDate "2023.03.24"]\n[Termination "Kye_Schnei won by resignation"]\n\n1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. Ne2 d6 5. h3 Nf6 6. Ng3 Be6 7. d3 O-O 8. Bg5\nd5 9. Qd2 h6 10. Bh4 d4 11. Nh5 Be7 12. g4 Nxh5 13. gxh5 Bxh4 14. O-O-O Be7 15.\nRg1 Bxa2 16. Be2 Qd6 17. Rg3 f6 18. Rdg1 Rf7 19. Qxh6 Bf8 20. Nh4 Ne7 21. Bg4\ngxh6 22. Bf5+ Kh8 23. Ng6+ Nxg6 24. Bxg6 Rg7 25. Rg4 Be7 26. Bf7 Rxg4 27. Rxg4\nBxf7 0-1')

print(x)