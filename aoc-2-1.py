from collections import defaultdict

def check_match(input):
    score_combo = {}

    score_combo[frozenset(["A","X"])] = 3
    score_combo[frozenset(["B","Y"])] = 3
    score_combo[frozenset(["C","Z"])] = 3

    score_combo[frozenset(["A","Z"])] = 0
    score_combo[frozenset(["B","X"])] = 0
    score_combo[frozenset(["C","Y"])] = 0

    score_combo[frozenset(["A","Y"])] = 6
    score_combo[frozenset(["B","Z"])] = 6
    score_combo[frozenset(["C","X"])] = 6
 
    return score_combo[input]

def match_score(input):
    play_score = {}
    play_score['X'] = 1
    play_score['Y'] = 2
    play_score['Z'] = 3

    return check_match(frozenset(input)) + play_score[input[-1]]

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
        player_score += match_score(match)

    print(f"Total score after {len(rps_guide)} rounds is: {player_score}")

if __name__=="__main__":
    main()
