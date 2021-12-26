from collections import Counter


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = {}
    for line in content:
        if '-' in line:
            x, y = line.split(' -> ')
            output_values[x] = y
        elif len(line) > 0:
            output_template = line

    return output_values, output_template


def polymer_insertion1(template, insertion_rules):
    pairs = [template[i:i + 2] for i in range(len(template) - 1)]

    output_template = ''
    for pair in pairs:
        if pair in insertion_rules:
            output_template += pair[0] + insertion_rules[pair]
        else:
            output_template += pair[0]
            print('kom je hier???')
            exit()
    output_template += template[-1]

    return output_template


def polymer_insertion2(template, insertion_rules, lettercount):
    output_dict_triplets = {}
    for pair in template:
        insert_letter = insertion_rules[pair]
        output_template = pair[0] + insert_letter + pair[1]
        output_dict_triplets[output_template] = template[pair]
        if insert_letter in lettercount:
            lettercount[insert_letter] += template[pair]
        else:
            lettercount[insert_letter] = template[pair]

    output_dict = {}
    for triplet in output_dict_triplets:
        # print(f'triplet = {triplet}')
        pair1 = triplet[0:2]
        pair2 = triplet[1:3]
        if pair1 in output_dict:
            output_dict[pair1] += output_dict_triplets[triplet]
        else:
            output_dict[pair1] = output_dict_triplets[triplet]

        if pair2 in output_dict:
            output_dict[pair2] += output_dict_triplets[triplet]
        else:
            output_dict[pair2] = output_dict_triplets[triplet]

    return output_dict, lettercount


def template2template_dict(template):
    pairs = [template[i:i + 2] for i in range(len(template) - 1)]
    template_dict = Counter(pairs)
    return template_dict


if __name__ == '__main__':
    # This is day 14
    filename = "input/input14.txt"
    data, template = read_input_file(filename)
    print(f'Template:     {template} ')
    # for i in range(1, 5):
    #     template = polymer_insertion1(template, data)
    #     # print(f'After step {i}, length {len(template)}: {template}')
    #     print(f'After step {i}, length {len(template)}')
    #
    #     collection = Counter(template)
    #     print(collection)
    #     print(f'part1: most common - least common = {max(collection.values()) - min(collection.values())}')

    lettercount = Counter(template)
    print(lettercount)
    template = template2template_dict(template)

    for i in range(1, 41):
        template, lettercount = polymer_insertion2(template, data, lettercount)
        print(f'part2: after step {i} {lettercount}')
        print(f'part2: most common - least common = {max(lettercount.values()) - min(lettercount.values())}')
