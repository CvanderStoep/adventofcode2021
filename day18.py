import ast
import copy
import itertools
from collections import deque


class SnailFishNumber:
    splitted = False

    def __init__(self, left=None, right=None, level=0, parent=None, exploded=False, position=0):
        self.left = left
        self.right = right
        self.level = level
        self.parent = parent
        self.exploded = exploded  # to track whether the sfn is already exploded; only one explosion/round
        self.position = position  # to track the horizontal position of the pair (needed to exclude edge cases)

    def get_nested_level(self):

        if isinstance(self.left, int) and isinstance(self.right, int):
            return 0
        elif isinstance(self.left, int):
            return 1 + self.right.get_nested_level()
        elif isinstance(self.right, int):
            return 1 + self.left.get_nested_level()
        else:
            return 1 + max(self.left.get_nested_level(), self.right.get_nested_level())

    def set_node_levels(self, level=0):

        if isinstance(self.left, SnailFishNumber):
            self.left.parent = self
        if isinstance(self.right, SnailFishNumber):
            self.right.parent = self

        if isinstance(self.left, SnailFishNumber):
            self.left.position = self.position - 1
            self.left.level = self.level + 1
            self.left.set_node_levels(self.left.level)
        if isinstance(self.right, SnailFishNumber):
            self.right.position = self.position + 1
            self.right.level = self.level + 1
            self.right.set_node_levels(self.right.level)

    def inorderTraversal(self):
        output = []
        if isinstance(self.left, int) and isinstance(self.right, int):
            output = [self.left, self.right]
        elif isinstance(self.left, int):
            output = [self.left, self.right.inorderTraversal()]
        elif isinstance(self.right, int):
            output = [self.left.inorderTraversal(), self.right]
        else:
            output = [self.left.inorderTraversal(), self.right.inorderTraversal()]
        return output

    def inorderTraversal_print(self):

        if isinstance(self.left, int):
            print(self.left, end=' , ')
        else:
            self.left.inorderTraversal_print()
        if isinstance(self.right, int):
            print(self.right, end=' , ')
        else:
            self.right.inorderTraversal_print()

    def explode(self):

        if self.level == 3:
            root_node = self.parent.parent.parent
            # print('level 3 reached')
            if isinstance(self.left, int) and isinstance(self.right, int):
                pass
                # print('no further levels below')
            elif root_node.exploded:
                pass
                # print('already exploded')
            elif isinstance(self.left, SnailFishNumber):
                # print('level to explode reached, left = snf')
                root_node.exploded = True
                old_left = self.left.left
                old_right = self.left.right

                self.right = self.right + self.left.right
                node_up = self.parent
                found_number = False
                for _ in range(3):
                    if isinstance(node_up.left, int):
                        node_up.left += self.left.left
                        # print('hier1')
                        found_number = True
                        break
                    node_up = node_up.parent
                if self.left.position != -4:
                    # Down from root node to find first integer on the left
                    if isinstance(root_node.left, SnailFishNumber) and not found_number:
                        root_node = root_node.left
                        for _ in range(3):
                            if isinstance(root_node.right, int):
                                root_node.right += old_left
                                # print('hier11')
                                # print(f'{self.left.position}')
                                break
                            root_node = root_node.left
                self.left = 0
            elif isinstance(self.right, SnailFishNumber):
                # print('level to explode reached, right = sfn')
                root_node.exploded = True
                old_left = self.right.left
                old_right = self.right.right
                self.left = self.left + self.right.left
                node_up = self.parent
                found_number = False
                for _ in range(3):
                    if isinstance(node_up.right, int):
                        node_up.right += self.right.right
                        # print('hier2')
                        found_number = True
                        break
                    node_up = node_up.parent
                if self.right.position != 4:
                    # Down from root node to find first integer on the right
                    if isinstance(root_node.right, SnailFishNumber) and not found_number:
                        root_node = root_node.right
                        for _ in range(3):
                            if isinstance(root_node.left, int):
                                root_node.left += old_right
                                # print('hier21')
                                # print(f'{self.right.position}')
                                break
                            root_node = root_node.left
                self.right = 0
            else:
                print('level > 4?')
        else:
            if isinstance(self.left, SnailFishNumber):
                self.left.explode()
            if isinstance(self.right, SnailFishNumber):
                self.right.explode()

    def split(self):

        if not sfn.splitted:
            # print(f'splitted: {sfn.splitted}')
            if isinstance(self.left, int):
                if self.left >= 10:
                    new_left = int(self.left / 2)
                    new_right = round(self.left / 2 + 0.1)
                    # print(f' left >= 10:  {self.left}')
                    self.left = SnailFishNumber(new_left, new_right)
                    sfn.splitted = True
            else:
                self.left.split()

            if isinstance(self.right, int):
                if self.right >= 10:
                    new_left = int(self.right / 2)
                    new_right = round(self.right / 2 + 0.1)
                    # print(f'right >= 10: {self.right}')
                    self.right = SnailFishNumber(new_left, new_right)
                    sfn.splitted = True
            else:
                self.right.split()


def convert_list_to_snailfish(input_list):
    left_elem = input_list[0]
    right_elem = input_list[1]

    if isinstance(left_elem, int) and isinstance(right_elem, int):
        return SnailFishNumber(left_elem, right_elem)
    elif isinstance(left_elem, int):
        return SnailFishNumber(left_elem, convert_list_to_snailfish(right_elem))
    elif isinstance(right_elem, int):
        return SnailFishNumber(convert_list_to_snailfish(left_elem), right_elem)
    else:
        return SnailFishNumber(convert_list_to_snailfish(left_elem),
                               convert_list_to_snailfish(right_elem))


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = list()
    for line in content:
        output_values.append(ast.literal_eval(line))
    return output_values


def Snailfish_addition(sfn1, sfn2):
    if sfn1 is None:
        return sfn2
    if sfn2 is None:
        return sfn1
    else:
        return SnailFishNumber(sfn1, sfn2)


if __name__ == '__main__':
    # This is day 18
    filename = "input/input18test.txt"
    snail_fish_numbers = read_input_file(filename)

    snailfish_sum = None
    for sfn_list in snail_fish_numbers:
        print(sfn_list)
        sfn = convert_list_to_snailfish(sfn_list)
        print(f'Snailfish Level: {sfn.get_nested_level()} ')

        snailfish_sum = Snailfish_addition(snailfish_sum, sfn)
        # TODO
        # implement addition of Snailfish numbers
        sfn.set_node_levels()

        reduced = False  # keep exploding & splitting until done ==> reduced = True
        while not reduced:
            sfn.set_node_levels()
            sfn.splitted = False
            while sfn.get_nested_level() >= 4:
                sfn.exploded = False
                print(f'Snailfish Level: {sfn.get_nested_level()} ')
                sfn.explode()
                print(f'exploded: {sfn.inorderTraversal()}')
            sfn.split()
            if not sfn.splitted:
                reduced = True
            print(f'split: {sfn.inorderTraversal()}')
        print('-------------')

    sfn1 = SnailFishNumber(1,1)
    sfn1 = None
    sfn2 = SnailFishNumber(2,2)
    sum = Snailfish_addition(sfn1, sfn2)
    print(sum.inorderTraversal())

""""
    

[[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
[[3,[2,[1,[7,3]]]],[6,[5,[4,3]]]]
[[[[[9,8],1],2],3],4]
[[[ [1,[9,8]]  ,2],3],4]
[7,[6,[5,[4,[3,2]]]]]
[[6,[5,[4,[3,2]]]],1]
[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]

"""
