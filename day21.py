import itertools
from collections import deque


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        # output_values.append(line)
        # output_values.append(list(map(int, list(line))))
        elem = line.split(':')
        output_values.append(elem)
    s1 = int(output_values[0][1])
    s2 = int(output_values[1][1])

    return s1, s2


def deterministic_dice(score, dice):
    d1, d2, d3 = next(dice), next(dice), next(dice)
    score += d1 + d2 + d3
    score = (score - 1) % 10 + 1
    return score


def dirac_dice():
    dice = [1, 2, 3]
    outcome = itertools.product(dice, repeat=3)
    return outcome


def player_turn():
    dice_3 = [3, 4, 5, 6, 7, 8, 9]
    outcome = itertools.product(dice_3, repeat=2)
    return outcome


def new_score(score, dice):
    score = score + dice
    score = (score - 1) % 10 + 1
    return score


def play_game(s1, s2):
    total1, total2 = 0, 0
    number_of_dice_rolls = 0

    dice = itertools.cycle(range(1, 101))

    while True:
        s1 = deterministic_dice(s1, dice)
        total1 += s1
        number_of_dice_rolls += 3
        print(f'player1 moves to space {s1} for a total score of {total1}')
        if total1 >= 1000:
            losing_player_points = total2
            break
        s2 = deterministic_dice(s2, dice)
        total2 += s2
        number_of_dice_rolls += 3
        print(f'player2 moves to space {s2} for a total score of {total2}')
        if total2 >= 1000:
            losing_player_points = total1
            break
    return number_of_dice_rolls, losing_player_points


def play_game2(s1, s2):
    total1, total2 = 0, 0
    number_of_dice_rolls = 0

    for p1_dice, p2_dice in player_turn():
        print(p1_dice, p2_dice)
        s1 = new_score(s1, p1_dice)
        total1 += s1
        number_of_dice_rolls += 3
        print(f'player1 moves to space {s1} for a total score of {total1}')
        if total1 >= 21:
            losing_player_points = total2
            break
        s2 = new_score(s2, p2_dice)
        total2 += s2
        number_of_dice_rolls += 3
        print(f'player2 moves to space {s2} for a total score of {total2}')
        if total2 >= 21:
            losing_player_points = total1
            break
    return number_of_dice_rolls, losing_player_points


if __name__ == '__main__':
    # This is day 21
    filename = "input/input21.txt"
    s1, s2 = read_input_file(filename)

    number_of_dice_rolls, losing_player_points = play_game(s1, s2)

    print(f'dice rolls: {number_of_dice_rolls}')
    print(f'points of losing player: {losing_player_points}')
    print(f'part1: {number_of_dice_rolls * losing_player_points}')

    output = dirac_dice()  # tuples
    dict_output = {}
    for elem in output:
        som_elem = sum(elem)
        if som_elem in dict_output:
            dict_output[som_elem] += 1
        else:
            dict_output[som_elem] = 1
    print(dict_output)

    play_game2(s1, s2)