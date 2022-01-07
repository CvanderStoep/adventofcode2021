import copy
import itertools
import random
from collections import deque


def calculate_energy(position, move):
    energy_costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

    x = abs(position[1][0] - move[0])
    y = abs(position[1][1] - move[1])
    up = abs(position[1][1] - 1)
    down = abs(move[1] - 1)
    distance = x + up + down
    distance2 = x + y
    if distance != distance2:
        pass
    return distance * energy_costs[position[0]]


def make_end_maze(maze):
    end_maze = copy.deepcopy(maze)
    end_maze[2][3] = end_maze[3][3] = "A"
    end_maze[2][5] = end_maze[3][5] = "B"
    end_maze[2][7] = end_maze[3][7] = "C"
    end_maze[2][9] = end_maze[3][9] = "D"
    return end_maze


def make_blank_maze(maze):
    blank_maze = copy.deepcopy(maze)
    blank_maze[2][3] = blank_maze[3][3] = "."
    blank_maze[2][5] = blank_maze[3][5] = "."
    blank_maze[2][7] = blank_maze[3][7] = "."
    blank_maze[2][9] = blank_maze[3][9] = "."
    return blank_maze


def make_maze_from_letters(input_maze, input_letters):
    new_maze = copy.deepcopy(input_maze)
    for letter in input_letters:
        new_maze[letter[1]][letter[2]] = letter[0]
    return new_maze


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        output_values.append(list(line))
    return output_values


def find_possible_moves(maze):
    moves = []
    number_rows = len(maze)
    number_cols = len(maze[0])
    for r in range(number_rows):
        for c in range(number_cols):
            if maze[r][c] == '.':
                moves.append([r, c])
    return moves


def letter_locations(maze):
    locations = []
    number_rows = len(maze)
    number_cols = len(maze[0])
    for r in range(number_rows):
        for c in range(number_cols):
            if maze[r][c] in 'ABCD':
                locations.append([maze[r][c], r, c])
    return locations


def surrounding(maze, x, y):
    vals = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    vals = [(x_i, y_i) for (x_i, y_i) in vals if 0 <= x_i < len(maze) and 0 <= y_i < len(maze[x])]
    vals = [(x_i, y_i) for (x_i, y_i) in vals if maze[x_i][y_i] != "#"]
    vals = [(x_i, y_i) for (x_i, y_i) in vals if maze[x_i][y_i] != "."]

    return vals


def make_move(maze, r1, c1, r2, c2):
    maze[r1][c1], maze[r2][c2] = maze[r2][c2], maze[r1][c1]
    return maze


def valid_neighbours(maze, r1, c1):
    return surrounding(maze, r1, c1)


def random_move(maze, possible_moves):
    valid_neighbour = False
    while not valid_neighbour:
        random_choice = random.choice(possible_moves)
        vn = valid_neighbours(maze, random_choice[0], random_choice[1])
        if len(vn) == 0:
            continue
        valid_neighbour = True
        random_neighbour = random.choice(vn)
    r1, c1 = random_choice[0], random_choice[1]
    r2, c2 = random_neighbour[0], random_neighbour[1]

    maze = make_move(maze, r1, c1, r2, c2)
    return maze


def print_maze(maze):
    for line in maze:
        print(line)
    print()


if __name__ == '__main__':
    # This is day 23
    filename = "input/input23.txt"
    maze = read_input_file(filename)

    end_maze = make_end_maze(maze)
    blank_maze = make_blank_maze(maze)
    letters = letter_locations(maze)

    previous_maze = make_maze_from_letters(blank_maze, letters)

    print_maze(maze)
    iterations = 0
    all_tried_solutions = set()
    all_tried_solutions.add(str(letter_locations(maze)))
    current_solution_stack = [letter_locations(maze)]
    while maze != end_maze:
        possible_moves = find_possible_moves(maze)
        maze = random_move(maze, possible_moves)
        ll = letter_locations(maze)
        if str(ll) in all_tried_solutions:
            letter_from_stack = current_solution_stack.pop()
            maze = make_maze_from_letters(blank_maze, letter_from_stack)
            continue
        all_tried_solutions.add(str(ll))
        current_solution_stack.append(ll)
        iterations += 1
        if iterations % 10000 == 0:
            print(iterations, len(current_solution_stack))
            print_maze(maze)
