from statistics import median

import check_brackets


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        output_values.append(line)

    return output_values


if __name__ == '__main__':
    # This is day10 part1 and part2
    filename = "input/input10.txt"
    data = read_input_file(filename)

    total_error = 0
    auto_dict_error = {'(': 1, '[': 2, '{': 3, '<': 4}
    autocomplete_error_list = []
    for text in data:
        message1, position, message2, first_illegal_character = check_brackets.find_mismatch(text)
        if message1 == "corrupted":
            if first_illegal_character == ")":
                total_error += 3
            if first_illegal_character == ']':
                total_error += 57
            if first_illegal_character == '}':
                total_error += 1197
            if first_illegal_character == '>':
                total_error += 25137
        if message1 == 'incomplete':
            autocomplete_error = 0
            for br in reversed(first_illegal_character):
                err_char = br.char
                error_value = auto_dict_error.get(err_char)
                autocomplete_error = autocomplete_error * 5 + error_value
            autocomplete_error_list.append(autocomplete_error)
    print(f'part1: total error= {total_error}')
    print(f'part2: autocomplete_error_list= {autocomplete_error_list}')
    print(f'part2: median error= {median(autocomplete_error_list)}')
