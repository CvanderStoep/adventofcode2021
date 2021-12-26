def read_input_file():
    # This is day8 part1

    filename = "input8.txt"
    with open(filename) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        output_values.append(line.split('|')[1])

    number_of_digits = 0
    for elem in output_values:
        digits = elem.split()
        for digit in digits:
            if len(digit) in [2, 3, 4, 7]:
                number_of_digits += 1

    print(f'number of digits 1, 4, 7, 8: {number_of_digits}')


if __name__ == '__main__':
    read_input_file()
