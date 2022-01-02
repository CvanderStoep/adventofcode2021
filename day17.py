import itertools
from collections import deque


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        # output_values.append(line)
        # output_values.append(list(map(int, list(line))))
        elem = line.split('..')
        xmin = int(elem[0].split('=')[1])
        xmax = int(elem[1].split(',')[0])
        ymin = int(elem[1].split('=')[1])
        ymax = int(elem[2])
        # output_values.append(elem)

    return xmin, xmax, ymin, ymax


def calc_new_position_and_velocity(x, y, vx, vy):
    xnew = x + vx
    ynew = y + vy
    if vx > 0:
        vxnew = vx - 1
    elif vx < 0:
        vxnew = vx + 1
    else:
        vxnew = 0
    vynew = vy - 1

    return xnew, ynew, vxnew, vynew


def calc_trajectory(xmin, xmax, ymin, ymax):
    overall_max_height = 0
    number_of_solutions = 0
    for vx_start in range(0, xmax + 1):
        for vy_start in range(ymin, -ymin + 1):
            x, y = 0, 0
            vx = vx_start
            vy = vy_start
            inside_target = False
            max_height = 0
            while not inside_target:
                x, y, vx, vy = calc_new_position_and_velocity(x, y, vx, vy)
                if y > max_height:
                    max_height = y
                if xmin <= x <= xmax and ymin <= y <= ymax:
                    inside_target = True
                    number_of_solutions += 1
                    # print(f'vx, vy, max height= {vx_start}, {vy_start}, {max_height}')
                    if max_height > overall_max_height:
                        overall_max_height = max_height
                        vx_opt, vy_opt = vx_start, vy_start

                if x > xmax or y < ymin:
                    break
    return vx_opt, vy_opt, overall_max_height, number_of_solutions


if __name__ == '__main__':
    # This is day 17
    filename = "input/input17.txt"
    xmin, xmax, ymin, ymax = read_input_file(filename)

    vx_opt, vy_opt, overall_max_height, number_of_solutions = calc_trajectory(xmin, xmax, ymin, ymax)

    print(f'part1: overall max height, vx, vy = {overall_max_height}, {vx_opt}, {vy_opt}')
    print(f'part2: number of solutions= {number_of_solutions}')
