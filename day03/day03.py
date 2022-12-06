from string import ascii_lowercase
from string import ascii_uppercase

def get_priority_dict():
    items = sorted(set(ascii_lowercase + ascii_uppercase))  # ['A',..,'Z', 'a',...,'z']
    lowercase_priority = sorted(set (range(1,27)))
    uppercase_priority = sorted(set (range(27,53)))
    priority = uppercase_priority + lowercase_priority #[27, 28,..., 52, 1, 2,..., 26]
    priority_dict = {items[i]: priority[i] for i in range(len(items))}
    return priority_dict

    #SCORE_LOOKUP = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #score = SCORE_LOOKUP.index(char) + 1

def part01(filepath, priority_dict):
    final_score = 0
    with open(filepath) as f:
        for line in f:
            line = line.rstrip('\n')
            length = len(line)
            length_in_half = int(len(line) / 2)
            first_compartment = line[0:length_in_half]
            second_compartment = line[(length_in_half) : length]

            first_compartment_set = set(first_compartment)
            second_compartment_set = set(second_compartment)

            mutual_item = list(first_compartment_set.intersection(second_compartment_set))[0]
            
            final_score += priority_dict[mutual_item]

    print(final_score)


def part02(filepath, priority_dict):
    final_score = 0
    with open(filepath) as f:
        elve_group = []
        lines = []
        for line in f:
            line = line.rstrip('\n')
            lines.append(line)  
#0, 1, 2, ..299
        j = 1
        for i in list(range(0, len(lines))):
            if ((j) % 4 != 0):
                elve_group.append(lines[i])
                j += 1
                if (i == (len(lines) - 1)):
                    elve_1 = set (elve_group[0])             
                    elve_2 = set (elve_group[1])
                    elve_3 = set (elve_group[2])
                    mutual_item_in_group = list((elve_1.intersection(elve_2)).intersection(elve_3))[0]
                    print(elve_group, mutual_item_in_group)
                    final_score += priority_dict[mutual_item_in_group]
            else:   
                elve_1 = set (elve_group[0])             
                elve_2 = set (elve_group[1])
                elve_3 = set (elve_group[2])
                mutual_item_in_group = list((elve_1.intersection(elve_2)).intersection(elve_3))[0]
                print(elve_group, mutual_item_in_group)
                final_score += priority_dict[mutual_item_in_group]
                elve_group = []
                elve_group.append(lines[i])
                j = 2
    print(final_score)

priority_dict = get_priority_dict()
part01("input.txt", priority_dict)
part02("input.txt", priority_dict)
