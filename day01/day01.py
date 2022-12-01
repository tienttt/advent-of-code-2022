def calculate_energy_for_elve(input_file_path):
    elves = []
    with open(input_file_path) as f:
        i = 0
        total_energy = 0
        for line in f:          
            if (line != '\n'):                
                total_energy += int(line)                
            else:
                elves.append(total_energy)
                total_energy = 0
                i += 1
    return elves

def part01(elves):
    print('The total energies of the elve carrying the most:')   
    print (max(elves))

def part02(elves):
    print('The total energies of top 3 elves:')   
    print (elves[0] + elves[1] + elves[2])

elves = calculate_energy_for_elve("input.txt")
part01(elves)
part02(elves)