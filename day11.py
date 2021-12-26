import itertools
from collections import deque


def surrounding(input, x, y):
    vals = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y + 1), (x + 1, y + 1), (x - 1, y - 1),
            (x + 1, y - 1)]
    return [(x_i, y_i) for (x_i, y_i) in vals if 0 <= x_i < len(input) and 0 <= y_i < len(input[x])]


def surrounding2(input, x, y):
    vals = itertools.product(range(x - 1, x + 2), range(y - 1, y + 2))
    in_bounds = lambda x_i, y_i: 0 <= x_i < len(input) and 0 <= y_i < len(input[x]) and (x_i, y_i) != (x, y)
    return [(x_i, y_i) for (x_i, y_i) in vals if in_bounds(x_i, y_i)]


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        # output_values.append(line)
        output_values.append(list(map(int, list(line))))

    return output_values


def update_energy(input_data):
    flashed = set()
    flash_que = deque()
    total_flashes = 0

    # increase energy level of all octopus with 1
    for x_i, row in enumerate(input_data):
        for y_i, elem in enumerate(row):
            input_data[x_i][y_i] += 1
            if input_data[x_i][y_i] >= 10:
                flash_que.append([x_i, y_i])

    while flash_que:
        (x_i, y_i) = flash_que.pop()
        input_data[x_i][y_i] += 1
        if (x_i, y_i) in flashed:
            continue
        else:
            if input_data[x_i][y_i] >= 10:
                flashed.add((x_i, y_i))
                total_flashes += 1
                flash_que.extend(
                    [(x_j, y_j) for (x_j, y_j) in surrounding(input_data, x_i, y_i) if (x_j, y_j) not in flashed])
    for x_i, row in enumerate(input_data):
        for y_i, elem in enumerate(row):
            if input_data[x_i][y_i] > 9:
                input_data[x_i][y_i] = 0

    return input_data, total_flashes


if __name__ == '__main__':
    # This is day11 part1 and part2
    filename = "input/input11.txt"
    data = read_input_file(filename)

    number_of_octopus = len(data) * len(data[0])

    total_amount_of_flashes = 0
    for step in range(1, 5000):
        output, number_of_flashes_per_step = update_energy(data)
        print(f'After step {step}, number of flashes in this step: {number_of_flashes_per_step}')
        total_amount_of_flashes += number_of_flashes_per_step
        for el in output:
            print(el)
        if number_of_flashes_per_step == number_of_octopus:
            print(f'synchronized at step {step}')
            break

    print(f'total amount of flashes: {total_amount_of_flashes}')
