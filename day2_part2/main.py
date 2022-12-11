
def read_input():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    round = 0
    score = 0
    win = 6
    draw = 3
    loss = 0
    rock = 1
    paper = 2
    scissors = 3

    for line in Lines:
        if len(line) > 2:
            if line[:3] == 'A X':
                round = scissors + loss
                score += round
            elif line[:3] == 'A Y':
                round = rock + draw
                score += round
            elif line[:3] == 'A Z':
                round = paper + win
                score += round

            elif line[:3] == 'B X':
                round = rock + loss
                score += round
            elif line[:3] == 'B Y':
                round = paper + draw
                score += round
            elif line[:3] == 'B Z':
                round = scissors + win
                score += round

            elif line[:3] == 'C X':
                round = paper + loss
                score += round
            elif line[:3] == 'C Y':
                round = scissors + draw
                score += round
            elif line[:3] == 'C Z':
                round = rock + win
                score += round

    print(score)


if __name__ == '__main__':
    read_input()