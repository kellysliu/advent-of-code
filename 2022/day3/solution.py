import string
import sys

def main(input_file):
    lower_alphabet = list(string.ascii_lowercase)
    lower_alphabet_scores = {}
    for l, s in zip(lower_alphabet, range(1, 27)):
        lower_alphabet_scores[l] = s

    upper_alphabet = list(string.ascii_uppercase)
    upper_alphabet_scores = {}
    for l, s in zip(upper_alphabet, range(27, 53)):
        upper_alphabet_scores[l] = s

    with open(input_file, "r") as file:
        score = 0
        priorities = 0
        lines = list(file)
        for i in range(0, len(lines), 3):
            group = [g.strip() for g in lines[i:i+3]]
            assert len(group) == 3
            overlap = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
            assert len(overlap) == 1
            overlap_c = overlap.pop()
            score += lower_alphabet_scores.get(overlap_c, 0)
            score += upper_alphabet_scores.get(overlap_c, 0)
        print(score)

if __name__ == "__main__":
    main(sys.argv[1])
