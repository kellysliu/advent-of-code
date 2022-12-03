import sys

opponent = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

outcome_map = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

score_by_hand = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

defeats = {
    "rock" : "scissors",
    "paper": "rock",
    "scissors": "paper",
}

defeated_by = {
    "rock" : "paper",
    "paper": "scissors",
    "scissors": "rock",
}


def main(input_file):
    score = 0
    with open(input_file, "r") as file:
        for line in file:
            a, b = line.split()
            a_hand = opponent[a]
            outcome = outcome_map[b]
            if outcome == "draw":
                score += 3
                score += score_by_hand[a_hand]
            elif outcome == "lose":
                score += score_by_hand[defeats[a_hand]]
            elif outcome == "win":
                score += score_by_hand[defeated_by[a_hand]]
                score += 6
    print(score)


if __name__ == "__main__":
    main(sys.argv[1])

