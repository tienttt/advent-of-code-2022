def is_contain(pair):
    first_elve = pair[0].split('-')
    second_elve = pair[1].split('-')
    first_elve_set = set(range(int(first_elve[0]), int(first_elve[1]) + 1))
    second_elve_set = set(range(int(second_elve[0]), int(second_elve[1]) + 1))
    mutual_set = first_elve_set & second_elve_set
    
    if (len(mutual_set) == len(first_elve_set) or len(mutual_set) == len(second_elve_set)):
        return "fully_overlap"
    elif (len(mutual_set) != 0):
        return "overlap"
    print(first_elve, second_elve, mutual_set)

def read_input(filepath):
    pairs = []
    with open(filepath) as f:
        for line in f:
            pair = line.strip().split(",")
            pairs.append(pair)
    return pairs
        
def part01(pairs):
    count = 0
    for pair in pairs:
        if (is_contain(pair) == "fully_overlap"):
            count += 1
    print(count)

def part02(pairs):
    count = 0
    for pair in pairs:
        if (is_contain(pair) == "overlap" or is_contain(pair) == "fully_overlap"):
            count += 1
    print(count)

pairs = read_input("input.txt")
part01(pairs)
part02(pairs)