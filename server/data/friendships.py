import random

num_players = 12

def get_pair(num_players, friendship_pairs):
    int1 = random.randint(1, num_players)
    int2 = random.randint(1, num_players)

    if int1 == int2:
        return get_pair(num_players, friendship_pairs)
    elif (int1, int2) in friendship_pairs:
        return get_pair(num_players, friendship_pairs)
    elif (int2, int1) in friendship_pairs:
        return get_pair(num_players, friendship_pairs)  
    else:
        return (int1, int2)

friendship_pairs = []
for _ in range(32):
    pair = get_pair(num_players, friendship_pairs)
    friendship_pairs.append(pair)
    friendship_pairs.append(pair[::-1])