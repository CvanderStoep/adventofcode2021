import itertools
from collections import deque


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        output_values.append(line)
        # output_values.append(list(map(int, list(line))))
        # elem = line.split('-')
        # output_values.append(elem)

    return output_values


if __name__ == '__main__':
    # This is day
    filename = "input/input11.txt"
    data = read_input_file(filename)


