

def part01(filepath):
    scores = []
    a_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    win_score = {
        "A X": 3,
        "A Y": 6,
        "A Z": 0,
        "B X": 0,
        "B Y": 3,
        "B Z": 6,
        "C X": 6,
        "C Y": 0,
        "C Z": 3
    }
    with open(filepath) as f:
        for line in f:
            pair = line.rstrip('\n')
            score = win_score[pair] + a_scores[pair[-1]]
            scores.append(score)
    print("Total scores (part 01): ", sum(scores))

def part02(filepath):
    # X - need to lose, Y - end the round in a draw, Z - win
    # A - Rock, B - Paper, C - Sciscor
    # X - Rock, Y - Paper, Z - Sciscor
    scores = []
    a_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    win_scores = {
        "A X": 0,
        "A Y": 3,
        "A Z": 6,
        "B X": 0,
        "B Y": 3,
        "B Z": 6,
        "C X": 0,
        "C Y": 3,
        "C Z": 6
    }

    your_choices = {
        "A X": "Z",
        "A Y": "X",
        "A Z": "Y",
        "B X": "X",
        "B Y": "Y",
        "B Z": "Z",
        "C X": "Y",
        "C Y": "Z",
        "C Z": "X"
    }
    with open(filepath) as f:
        for line in f:
            pair = line.rstrip('\n')
            your_choice = your_choices[pair]
            score = a_scores[your_choice] + win_scores[pair]
            scores.append(score)
    print("Total scores (part 02): ", sum(scores))
    

part01("input.txt")
part02("input.txt")
