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


#item: a list 
def find_mutual_item(items):
    result = set(items[0])
    for item in items:
        result = result & set(item)
    mutual_item = list(result)[0]
    return mutual_item


def part01(filepath, priority_dict):
    final_score = 0
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            length = len(line)
            length_in_half = int(len(line) / 2)
            first_compartment = line[0:length_in_half]
            second_compartment = line[(length_in_half) : length]
            mutual_item = find_mutual_item([first_compartment, second_compartment])
            
            final_score += priority_dict[mutual_item]

    print(final_score)


def part02(filepath, priority_dict):
    final_score = 0
    with open(filepath) as f:
        elve_group = []
        lines = []
        for line in f:
            line = line.strip()
            lines.append(line)  
        j = 1
        for i in list(range(len(lines))):
            if ((j) % 4 != 0):
                elve_group.append(lines[i])
                j += 1
                if (i == (len(lines) - 1)):
                    mutual_item_in_group = find_mutual_item(elve_group)
                    #print(elve_group, mutual_item_in_group)
                    final_score += priority_dict[mutual_item_in_group]
            else:   
                mutual_item_in_group = find_mutual_item(elve_group)
                #print(elve_group, mutual_item_in_group)
                final_score += priority_dict[mutual_item_in_group]
                elve_group = []
                elve_group.append(lines[i])
                j = 2
    print(final_score)

priority_dict = get_priority_dict()
part01("input.txt", priority_dict)
part02("input.txt", priority_dict)
