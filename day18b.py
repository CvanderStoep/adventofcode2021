import math
import re

with open('input/input18test.txt') as f:
    testlines = [line.strip() for line in f]
with open('input/input18.txt') as f:
    lines = [line.strip() for line in f]


def add(l, j):
    return "[" + l + "," + j + "]"


def distribute(s, num, first=False):
    if first:
        r = re.search(r"\d+", s)
        if r:
            return s[:r.start()] + str(int(r.group()) + int(num)) + s[r.end():]
        else:
            return s
    else:
        l = [(i.start(), i.end(), i.group()) for i in re.finditer(r"\d+", s)]
        if l:
            start, end, group = l[-1]

            return s[:start] + str(int(group) + int(num)) + s[end:]
        else:
            return s


def find_first_bracket_and_explode(l):
    countbracket = 0
    for i, j in enumerate(l):
        if j == "[":
            countbracket += 1
        elif j == "]":
            countbracket -= 1

        if countbracket >= 5 and l[i + 1].isnumeric():
            start, rest = l[:i], l[i:]
            index = rest.index("]")
            if "[" in rest[1:index]:
                continue
            else:
                left_number, right_number = re.findall(r"\d+", rest)[:2]
                return distribute(start, left_number, first=False) + "0" + distribute(rest[index + 1:], right_number,
                                                                                      first=True), True
    return l, False


def split_str(l):
    for i, j in enumerate(l):
        if i == 0:
            continue
        elif j.isnumeric() and l[i - 1].isnumeric():
            number = int(l[i - 1:i + 1])
            numa = math.floor(number / 2)
            numb = math.ceil(number / 2)
            left_number = str(numa)
            right_number = str(numb)
            return l[:i - 1] + "[" + left_number + "," + right_number + "]" + l[i + 1:]
    return l


def reduce_explode(l):
    s = ""
    while l != s:
        s = l
        l, exploded = find_first_bracket_and_explode(l)
        print('hier', l)

        if exploded:
            continue
        l = split_str(l)
    return l


def evaluate(a):
    a = a.replace("]", ")")
    a = a.replace("[", "(")
    a = a.replace(",", "*3+2*")
    return eval(a)


def part1(v):
    l = v[0]
    for i, j in enumerate(v[1:]):
        l = add(l, j)
        l = reduce_explode(l)
    return l
    # return evaluate(l)


def part2(v):
    return max([evaluate(reduce_explode(add(i, j))) for _, i in enumerate(v) for _, j in enumerate(v) if i != j])


print("part1 test output", part1(testlines))
# print("part1 my output", part1(lines))
# print("part2 test output", part2(testlines))
# print("part2 my output", part2(lines))