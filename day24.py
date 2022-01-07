import itertools
from collections import deque
from queue import Queue


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        # output_values.append(line)
        # output_values.append(list(map(int, list(line))))
        elem = line.split(' ')
        output_values.append(elem)

    return output_values




if __name__ == '__main__':
    # This is day

    filename = "input/input24.txt"
    instructions = read_input_file(filename)

    current_number = 92967699949891 + 100
    # number_string = '13579246899999'

    for current_number in range(92967699949891 + 1000, 92967699949891 -1000, -1) :
        # print(current_number)
        number_string = str(current_number)
        if '0' in number_string:
            continue

        position = 0
        w = x = y = z = 0

        for _instruction in instructions:
            # print(_instruction)
            input_instructions = _instruction[0]
            var1 = _instruction[1]
            var2 = None

            if input_instructions != "inp":
                var2 = _instruction[2]

            if input_instructions == 'inp':
                next_number = int(number_string[position])
                locals()[var1] = next_number
                position += 1

            if input_instructions == 'mul':  # multiply: var1 = var1 * var2
                if var2 not in 'wxyz':
                    locals()[var1] = locals()[var1] * int(var2)
                else:
                    locals()[var1] = locals()[var1] * locals()[var2]

            if input_instructions == 'eql':  # var1 = 1 if var1==var2 else 0
                if var2 not in 'wxyz':
                    locals()[var1] = 1 if locals()[var1] == int(var2) else 0
                else:
                    locals()[var1] = 1 if locals()[var1] == locals()[var2] else 0

            if input_instructions == 'add':  # addition: var1 = var1 + var2
                if var2 not in 'wxyz':
                    locals()[var1] = locals()[var1] + int(var2)
                else:
                    locals()[var1] = locals()[var1] + locals()[var2]

            if input_instructions == 'div':  # division: var1 = var1 / var2
                if var2 not in 'wxyz':
                    locals()[var1] = int(locals()[var1] / int(var2))
                else:
                    locals()[var1] = int(locals()[var1] / locals()[var2])

            if input_instructions == 'mod':  # modulo: var1 = var1 % var2
                if var2 not in 'wxyz':
                    locals()[var1] = locals()[var1] % int(var2)
                else:
                    locals()[var1] = locals()[var1] % locals()[var2]

            # print(f'w= {w}')
            # print(f'x= {x}')
            # print(f'y= {y}')

        # if current_number %100000 == 11111:
        print(f'current number, z= {current_number}, {z}')

        if z == 0:
            print(f'z= {z}')
            break

