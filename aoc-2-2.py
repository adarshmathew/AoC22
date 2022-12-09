from collections import defaultdict

def check_play(input):
    play_combo = {}

    play_combo[frozenset(["A","X"])] = "C"
    play_combo[frozenset(["A","Y"])] = "A"
    play_combo[frozenset(["A","Z"])] = "B"

    play_combo[frozenset(["B","X"])] = "A"
    play_combo[frozenset(["B","Y"])] = "B"
    play_combo[frozenset(["B","Z"])] = "C"

    play_combo[frozenset(["C","X"])] = "B"
    play_combo[frozenset(["C","Y"])] = "C"
    play_combo[frozenset(["C","Z"])] = "A"

    play_score = {}
    play_score['A'] = 1
    play_score['B'] = 2
    play_score['C'] = 3
 
    return play_score[play_combo[input]]

def total_score(input):
    match_score = {}
    match_score['X'] = 0
    match_score['Y'] = 3
    match_score['Z'] = 6

    return check_play(frozenset(input)) + match_score[input[-1]]

def read_input(fpath):
    inlist = []
    with open(fpath, 'r') as infile:
        for line in infile:
            inlist.append(line.strip().split(' '))
    return inlist

def main():
    fpath = 'inputs/aoc-2.txt'

    rps_guide = read_input(fpath)

    player_score = 0

    for match in rps_guide:
        player_score += total_score(match)

    print(f"Total score after {len(rps_guide)} rounds is: {player_score}")

if __name__=="__main__":
    main()
