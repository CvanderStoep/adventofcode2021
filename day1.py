def read_input_file():
    # Define a filename.
    filename = "input1.txt"

    # Open the file as f.
    # The function readlines() reads the file.
    with open(filename) as f:
        content = f.read().splitlines()

    # Show the file contents line by line.
    # We added the comma to print single newlines and not double newlines.
    # This is because the lines contain the newline character '\n'.
    previous_value = None
    number_of_increased_values = 0

    for line in content:
        value = int(line)

        if previous_value is None:
            pass
            # print(value, '(N/A - no previous measurement)')
        elif value > previous_value:
            # print(value, '(increased)')
            number_of_increased_values += 1
        elif value == previous_value:
            pass
            # print(value, '(identical)')
        else:
            pass
            # print(value, '(decreased)')
        previous_value = value

    print('measurements larger than previous:', number_of_increased_values)

    number_of_sum_increased_values = 0

    value_1 = None
    value_2 = None
    value_3 = None
    value_4 = None

    for line in content:
        value = int(line)
        if value_1 is None:
            value_1 = value
            continue
        elif value_2 is None:
            value_2 = value
            continue
        elif value_3 is None:
            value_3 = value
            # continue
        else:
            value_4 = value

        running_sum_1 = value_1 + value_2 + value_3
        if value_4 is None:
            # print(running_sum_1, '(N/A - no previous sum)')
            continue

        running_sum_2 = value_2 + value_3 + value_4
        if running_sum_2 > running_sum_1:
            # print(running_sum_2, '(increased)')
            number_of_sum_increased_values += 1
        else:
            # print(running_sum_2, '(decreased / no change)')
            pass
        value_1 = value_2
        value_2 = value_3
        value_3 = value_4

    print('measurements larger than previous sum:', number_of_sum_increased_values)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_input_file()
