from numpy import sign


def read_input_file():
    # This is day5 part 1 & 2
    filename = "input/input5test.txt"
    with open(filename) as f:
        content = f.read().splitlines()
    vents = {}
    total_vents = 0

    for line in content:
        coordinate_set = line.split('->')
        x1, y1 = (coordinate_set[0].split(","))
        x2, y2 = (coordinate_set[1].split(","))

        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        delta_x = sign(x2 - x1)
        delta_y = sign(y2 - y1)

        x, y = x1, y1
        last_coordinate = False  # there is no do ... until in python
        while not last_coordinate:
            if (x, y) == (x2, y2):
                last_coordinate = True
            if (x, y) in vents:
                vents[(x, y)] += 1
            else:
                vents[(x, y)] = 1
            x += delta_x
            y += delta_y

    for x, y in vents.items():
        print(x, y)
        if y > 1:
            total_vents += 1

    print(f'number of points with at least two lines overlap: {total_vents}')


if __name__ == '__main__':
    read_input_file()
