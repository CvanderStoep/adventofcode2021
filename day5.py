def read_input_file():
    # This is day5 part 1
    filename = "input5.txt"
    with open(filename) as f:
        content = f.read().splitlines()
    vents = {}
    total_vents = 0

    for line in content:
        coordinate_set = line.split('->')
        x1, y1 = (coordinate_set[0].split(","))
        x2, y2 = (coordinate_set[1].split(","))
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        if x1 == x2 or y1 == y2:  # horizontal or vertical line
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x, y) in vents:
                        vents[(x, y)] += 1
                    else:
                        vents[(x, y)] = 1
        else:  # diagonal line
            if (x1 - x2) == (y1 - y2):
                x1, x2 = min(x1, x2), max(x1, x2)
                y1, y2 = min(y1, y2), max(y1, y2)
                for x in range(x1, x2 + 1):
                    coord = (x, y1 + x - x1)
                    if coord in vents:
                        vents[coord] += 1
                    else:
                        vents[coord] = 1
            else:
                if x1 > x2:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
                for x in range(x1, x2 + 1):
                    coord = (x, y1 + x1 - x)
                    if coord in vents:
                        vents[coord] += 1
                    else:
                        vents[coord] = 1

    for x, y in vents.items():
        print(x, y)
        if y > 1:
            total_vents += 1

    print(f'number of points with at least two lines overlap: {total_vents}')


if __name__ == '__main__':
    read_input_file()
