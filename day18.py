import ast
import itertools
from collections import deque


class SnailFishNumber:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def get_nested_level(self):

        if isinstance(self.left, int) and isinstance(self.right, int):
            return 1
        elif isinstance(self.left, int):
            return 1 + self.right.get_nested_level()
        elif isinstance(self.right, int):
            return 1 + self.left.get_nested_level()
        else:
            return 1 + max(self.left.get_nested_level(), self.right.get_nested_level())


stack = deque()
def get_snailfish_level(input_list):
    left_elem = input_list[0]
    right_elem = input_list[1]
    print(f'stack= {stack}')
    print(f'left | right= {left_elem} | {right_elem}')

    if isinstance(left_elem, int) and isinstance(right_elem, int):
        depth = 0
        return depth
    elif isinstance(left_elem, int):
        stack.append(['left', left_elem])
        depth = 1 + get_snailfish_level(right_elem)
        if depth == 4:
            print(f'explode {explode(left_elem, right_elem, None)}')
        return depth
    elif isinstance(right_elem, int):
        stack.append(['right', right_elem])
        depth = 1 + get_snailfish_level(left_elem)
        if depth == 4:
            print(f'explode {explode(None, left_elem, right_elem)}')
        return depth
    else:
        depth = 1 + max((get_snailfish_level(left_elem)), (get_snailfish_level(right_elem)))
        return depth


def explode(left=None, input_pair=None, right=None):
    print(f'left | input pair | right=  {left} | {input_pair} | {right}')
    if left is None:
        output_list = [0, input_pair[1] + right]
    else:
        output_list = [input_pair[0] + left, 0]
    stack.pop()
    for i in range(3):
        pos, elem = stack.pop()
        if pos == 'right':
            output_list = [output_list] + [elem]
        else:
            output_list = [elem] + [output_list]
    return output_list


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = list()
    for line in content:
        output_values.append(ast.literal_eval(line))
    return output_values


def flatten_list(input_list, output_list=[]):
    for elem in input_list:
        if isinstance(elem, list):
            flatten_list(elem, output_list)
        else:
            output_list.append(elem)
    return output_list


if __name__ == '__main__':
    # This is day 18
    filename = "input/input18test.txt"
    snail_fish_numbers = read_input_file(filename)

    for sfn in snail_fish_numbers:
        print(sfn)
        print(get_snailfish_level(sfn))


# [[6,[5,[4,[3,2]]]],1]