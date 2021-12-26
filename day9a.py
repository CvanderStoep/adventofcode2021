import numpy as np


def find_minima(input_data):
    a = np.pad(input_data, (1, 1),
               mode='constant',
               constant_values=(np.amax(input_data), np.amax(input_data)))

    loc_minimum = []
    rows = a.shape[0]
    cols = a.shape[1]
    for ix in range(1, rows - 1):
        for iy in range(1, cols - 1):
            if a[ix, iy] < a[ix, iy + 1] and a[ix, iy] < a[ix, iy - 1] and \
                    a[ix, iy] < a[ix + 1, iy] and a[ix, iy] < a[ix - 1, iy]:
                temp_pos = (ix - 1, iy - 1)
                loc_minimum.append(temp_pos)

    return loc_minimum


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        output_values.append(list(map(int, list(line))))
    output_data = np.array(output_values)

    return output_data


if __name__ == '__main__':
    # This is day9 part1
    filename = "input/input9test.txt"
    data = read_input_file(filename)
    loc_min = find_minima(data)

    risk = 0
    for el in loc_min:
        # print(f'el= {el} ', data[el[0], el[1]])
        risk += 1 + data[el[0], el[1]]
    print(f'risk level= {risk}')

