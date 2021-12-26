import numpy as np


def read_input_file():
    # This is day9 part1

    filename = "input/input9test.txt"
    with open(filename) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        output_values.append(list(map(int, list(line))))
    data = np.array(output_values)
    a = np.pad(data, (1, 1),
               mode='constant',
               constant_values=(np.amax(data), np.amax(data)))
    loc_min = []
    rows = a.shape[0]
    cols = a.shape[1]
    for ix in range(0, rows - 1):
        for iy in range(0, cols - 1):
            if a[ix, iy] < a[ix, iy + 1] and a[ix, iy] < a[ix, iy - 1] and \
                    a[ix, iy] < a[ix + 1, iy] and a[ix, iy] < a[ix - 1, iy]:
                temp_pos = (ix - 1, iy - 1)
                loc_min.append(temp_pos)
    risk = 0
    for el in loc_min:
        risk += 1 + data[el[0], el[1]]
        print(el)
    print(f'risk level= {risk}')

    print(a)


if __name__ == '__main__':
    read_input_file()

# if a[ix, iy] < a[ix, iy + 1] and a[ix, iy] < a[ix, iy - 1] and \
#         a[ix, iy] < a[ix + 1, iy] and a[ix, iy] < a[ix + 1, iy - 1] and \
#         a[ix, iy] < a[ix + 1, iy + 1] and a[ix, iy] < a[ix - 1, iy] and \
#         a[ix, iy] < a[ix - 1, iy - 1] and a[ix, iy] < a[ix - 1, iy + 1]:
