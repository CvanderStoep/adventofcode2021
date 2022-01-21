import itertools
from collections import deque


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        # output_values.append(line)
        # output_values.append(list(map(int, list(line))))
        elem = line.split(',')
        switch = elem[0].split(' ')[0]
        xelem = elem[0].split('=')[1].split('..')
        yelem = elem[1].split('=')[1].split('..')
        zelem = elem[2].split('=')[1].split('..')

        output_values.append([switch, xelem, yelem, zelem])

    return output_values


def reboot(reboot_step, cuboid):

    cuboid_off = set()
    switch = reboot_step[0]
    xmin = max(int(reboot_step[1][0]), -50)
    xmax = min(int(reboot_step[1][1]), 50)
    ymin = max(int(reboot_step[2][0]), -50)
    ymax = min(int(reboot_step[2][1]), 50)
    zmin = max(int(reboot_step[3][0]), -50)
    zmax = min(int(reboot_step[3][1]), 50)
    # xmin = int(reboot_step[1][0])
    # xmax = int(reboot_step[1][1])
    # ymin = int(reboot_step[2][0])
    # ymax = int(reboot_step[2][1])
    # zmin = int(reboot_step[3][0])
    # zmax = int(reboot_step[3][1])
    print(f'xmin, xmax, ymin, ymax, zmin, zmax [{xmin} {xmax}] [{ymin} {ymax}] [{zmin} {zmax}]')

    if switch == "on":
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                for z in range(zmin, zmax + 1):
                    cuboid.add((x,y,z))
    else:
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                for z in range(zmin, zmax + 1):
                    cuboid_off.add((x,y,z))

    cuboid = cuboid.difference(cuboid_off)
    return cuboid


if __name__ == '__main__':
    # This is day 22
    filename = "input/input22.txt"
    reboot_steps = read_input_file(filename)
    cuboid = set()
    for reboot_step in reboot_steps:
        print(reboot_step)
        cuboid = reboot(reboot_step, cuboid)
        print(f'cuboid length: {len(cuboid)}')
