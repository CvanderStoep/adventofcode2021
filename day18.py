import ast
import itertools


class SnailFishNumber:
    splitted = False

    def __init__(self, left=None, right=None, level=0, parent=None, exploded=False, position=0, path=""):
        self.left = left
        self.right = right
        self.level = level
        self.parent = parent
        self.exploded = exploded  # to track whether the sfn is already exploded; only one explosion/round
        self.position = position  # to track the horizontal position of the pair (needed to exclude edge cases)
        self.path = path  # track the route from root to node

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
        if isinstance(self.left, int) and isinstance(self.right, int):
            output = [self.left, self.right]
        elif isinstance(self.left, int):
            output = [self.left, self.right.inorderTraversal()]
        elif isinstance(self.right, int):
            output = [self.left.inorderTraversal(), self.right]
        else:
            output = [self.left.inorderTraversal(), self.right.inorderTraversal()]
        return output

    def set_path(self):
        if isinstance(self.left, SnailFishNumber):
            self.left.path = self.path + "L"
            self.left.set_path()
        if isinstance(self.right, SnailFishNumber):
            self.right.path = self.path + "R"
            self.right.set_path()

    def clear_path(self):
        if isinstance(self.left, SnailFishNumber):
            self.left.path = ""
            self.left.clear_path()
        if isinstance(self.right, SnailFishNumber):
            self.right.path = ""
            self.right.clear_path()

    def magnitude(self):
        if isinstance(self.left, int) and isinstance(self.right, int):
            return 3 * self.left + 2 * self.right
        elif isinstance(self.left, int):
            return 3 * self.left + 2 * self.right.magnitude()
        elif isinstance(self.right, int):
            return 3 * self.left.magnitude() + 2 * self.right
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def set_right_node(self, root, path, left, right):
        # to go to the start node: remove all trailing R and replace last L with R
        # example: LRLR -> LRR
        if path == "RRRR":
            return
        while path[-1] == "R":
            path = path[:-1]
        path = path[:-1]
        path += "R"

        current_node = root
        while len(path) > 1:
            direction = path[0]
            if direction == "L":
                current_node = current_node.left
            else:
                current_node = current_node.right
            path = path[1:]
        if isinstance(current_node.right, int):
            current_node.right += right
        elif isinstance(current_node.right.left, int):
            current_node.right.left += right
        elif isinstance(current_node.right.left.left, int):
            current_node.right.left.left += right
        elif isinstance(current_node.right.left.left.left, int):
            current_node.right.left.left.left += right
        else:
            current_node.right.left.left.left.left += right

    def set_left_node(self, root, path, left, right):
        # to go to the start node: remove all trailing L and replace last R with L
        # example: LRL -> LL
        if path == "LLLL":
            return
        while path[-1] == "L":
            path = path[:-1]
        path = path[:-1]
        path += "L"

        current_node = root
        while len(path) > 1:
            direction = path[0]
            if direction == "L":
                current_node = current_node.left
            else:
                current_node = current_node.right
            path = path[1:]
            # print(f'pathL= {path}')
        if isinstance(current_node.left, int):
            current_node.left += left
        elif isinstance(current_node.left.right, int):
            current_node.left.right += left
        elif isinstance(current_node.left.right.right, int):
            current_node.left.right.right += left
        elif isinstance(current_node.left.right.right.right, int):
            current_node.left.right.right.right += left
        else:
            current_node.left.right.right.right.right += left

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
                root_node.exploded = True
                left_value = self.left.left
                right_value = self.left.right
                route_path = self.left.path
                self.set_left_node(root_node, route_path, left_value, right_value)
                self.set_right_node(root_node, route_path, left_value, right_value)
                self.left = 0
            elif isinstance(self.right, SnailFishNumber):
                root_node.exploded = True
                left_value = self.right.left
                right_value = self.right.right
                route_path = self.right.path
                self.set_left_node(root_node, route_path, left_value, right_value)
                self.set_right_node(root_node, route_path, left_value, right_value)
                self.right = 0
            else:
                print('level > 4?')
        else:
            if isinstance(self.left, SnailFishNumber):
                self.left.explode()
            if isinstance(self.right, SnailFishNumber):
                self.right.explode()

    def split(self):

        if not SnailFishNumber.splitted:
            if isinstance(self.left, int):
                if self.left >= 10:
                    new_left = int(self.left / 2)
                    new_right = round(self.left / 2 + 0.1)
                    self.left = SnailFishNumber(new_left, new_right)
                    SnailFishNumber.splitted = True
            else:
                self.left.split()
            if not SnailFishNumber.splitted:
                if isinstance(self.right, int):
                    if self.right >= 10:
                        new_left = int(self.right / 2)
                        new_right = round(self.right / 2 + 0.1)
                        self.right = SnailFishNumber(new_left, new_right)
                        SnailFishNumber.splitted = True
                else:
                    self.right.split()

    def reset(self):
        self.set_node_levels()
        self.clear_path()
        self.set_path()
        SnailFishNumber.splitted = False


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
    if sfn1 is None and sfn2 is None:
        return None
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

    sfn = None
    for sfn_list in snail_fish_numbers:
        print(sfn_list)
        next_sfn = convert_list_to_snailfish(sfn_list)
        print(f'Snailfish Level: {next_sfn.get_nested_level()} ')

        sfn = Snailfish_addition(sfn, next_sfn)
        print('snailfish after sum', sfn.inorderTraversal())

        reduced = False  # keep exploding & splitting until done ==> reduced = True
        while not reduced:
            sfn.reset()
            while sfn.get_nested_level() >= 4:
                sfn.exploded = False
                sfn.explode()
                print(f'exploded: {sfn.inorderTraversal()}')
                sfn.reset()
            sfn.split()
            if not SnailFishNumber.splitted:
                reduced = True
            print(f'split: {sfn.inorderTraversal()}')
        print('-------------')
    print(f'part 1 - magnitude of final sum is {sfn.magnitude()} ')

    max_magnitude = 0
    for n1, n2 in itertools.permutations(range(len(snail_fish_numbers)),2):
        sfn1 = snail_fish_numbers[n1]
        sfn2 = snail_fish_numbers[n2]
        sfn1 = convert_list_to_snailfish(sfn1)
        sfn2 = convert_list_to_snailfish(sfn2)
        sfn = Snailfish_addition(sfn1, sfn2)
        reduced = False  # keep exploding & splitting until done ==> reduced = True
        while not reduced:
            sfn.reset()
            while sfn.get_nested_level() >= 4:
                sfn.exploded = False
                sfn.explode()
                print(f'exploded: {sfn.inorderTraversal()}')
                sfn.reset()
            sfn.split()
            if not SnailFishNumber.splitted:
                reduced = True
            print(f'split: {sfn.inorderTraversal()}')
        print('-------------')
        sum_magnitude = sfn.magnitude()
        print(f'part 2 - magnitude of two sum is {sum_magnitude} ')
        max_magnitude = sum_magnitude if sum_magnitude > max_magnitude else max_magnitude

    print(f'part 2 - maximum magnitude of two sum is {max_magnitude} ')

""""
    

OK: [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]] -> [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
OK: [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] -> [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
OK: [[3,[2,[1,[7,3]]]],[6,[5,[4,3]]]] -> [[3, [2, [8, 0]]], [9, [5, [4, 3]]]]
OK: [[[[[9,8],1],2],3],4] -> [[[[0, 9], 2], 3], 4]
OK: [[[ [1,[9,8]]  ,2],3],4] -> [[[[0, 5], [5, 5]], 3], 4]
OK: [7,[6,[5,[4,[3,2]]]]] -> [7, [6, [5, [7, 0]]]]
OK: [[6,[5,[4,[3,2]]]],1] -> [[6, [5, [7, 0]]], 3]
OK: [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] -> [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
OK: [[[[[1, 1], [2, 2]], [3, 3]], [4, 4]], [5, 5]] -> [[[[3, 0], [3, 3]], [4, 4]], [7, 5]]
                                    should be:            [[[[3,0],[5,3]],[4,4]],[5,5]]

"""
