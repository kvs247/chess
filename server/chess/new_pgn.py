from datetime import date

def new_pgn(white_username, black_username):
    date_today = str(date.today()).replace('-', '.')

    pgn = (
        f'[Date "{date_today}"]\n'
        f'[Result "*"]\n'
        f'[White "{white_username}"]'
        f'\n[Black "{black_username}"]\n\n*'
    )

    return pgn

print(new_pgn('a', 'b'))