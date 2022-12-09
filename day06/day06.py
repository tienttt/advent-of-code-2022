def is_a_marker(str):
    if (len(set(str)) == len(str)): #no duplication
        return True
    else:
        return False

def part01(filepath):
    with open(filepath) as f:
        line = f.readline()
    i = 0
    while (i <= len(line) - 4):
        if (is_a_marker(line[i:i+4])):
            return i+4
        i += 1

def part01(filepath):
    with open(filepath) as f:
        line = f.readline()
    i = 0
    while (i <= len(line) - 14):
        if (is_a_marker(line[i:i+14])):
            return i+14
        i += 1

part01 = part01("input.txt")
print(part01)

