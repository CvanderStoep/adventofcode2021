import sys
from statistics import mean, median


def read_input_file():
    # This is day7 part 1 and 2

    filename = "input7.txt"
    with open(filename) as f:
        content = f.read().splitlines()

    for line in content:
        initial_positions = line.split(',')
    initial_positions = list(map(int, initial_positions))

    max_position = max(initial_positions)
    min_position = min(initial_positions)

    print(f'min: {min_position}, max: {max_position}, number of points: {len(initial_positions)}')

    lowest_fuel = sys.maxsize
    position_with_lowest_fuel = min_position

    for position in range(min_position, max_position):
        fuel = 0
        for crap in initial_positions:
            step = abs(crap - position)
            fuel += int(step * (step + 1) / 2)  # formula for part 2
            # fuel += step  # formula for part 1
        if fuel < lowest_fuel:
            lowest_fuel = fuel
            position_with_lowest_fuel = position

    print(f'mp, fuel: {position_with_lowest_fuel}, {lowest_fuel}')
    print(f'median: {round(median(initial_positions))}')


if __name__ == '__main__':
    read_input_file()
