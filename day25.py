import copy
import random


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        output_values.append(list(line))
    return output_values


def right_neighbour(i, j, state):
    rows = len(state)
    cols = len(state[0])
    right_i = i
    right_j = j + 1 if j < cols - 1 else 0
    return right_i, right_j


def down_neighbour(i, j, state):
    rows = len(state)
    cols = len(state[0])
    down_i = i + 1 if i < rows - 1 else 0
    down_j = j
    return down_i, down_j


def horizontal_move(state):
    rows = len(state)
    cols = len(state[0])

    new_state = copy.deepcopy(state)
    for r in range(rows):
        for c in range(cols):
            if state[r][c] == '>':
                nr, nc = right_neighbour(r, c, state)
                if state[nr][nc] == '.':
                    new_state[r][c] = '.'
                    new_state[nr][nc] = '>'
    return new_state


def vertical_move(state):
    rows = len(state)
    cols = len(state[0])

    new_state = copy.deepcopy(state)
    for r in range(rows):
        for c in range(cols):
            if state[r][c] == 'v':
                nr, nc = down_neighbour(r, c, state)
                if state[nr][nc] == '.':
                    new_state[r][c] = '.'
                    new_state[nr][nc] = 'v'
    return new_state


def print_state(state):
    for line in state:
        for character in line:
            print(character, end="")
        print()
    print()


if __name__ == '__main__':
    # This is day 25
    filename = "input/input25.txt"
    state = read_input_file(filename)
    print_state(state)
    i = 0
    while True:
        i += 1
        new_state1 = horizontal_move(state)
        new_state2 = vertical_move(new_state1)
        if new_state2 == state:
            break
        state = copy.deepcopy(new_state2)

    print(f'After {i} steps:')
