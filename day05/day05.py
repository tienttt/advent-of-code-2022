import re

stacks = [[] for _ in  range(9)] #the last item in the stack is the first item of the list
moves = []

def read_input(filepath): #Another solution to try: Read it into a list of list and rotate it
    # s = ' 1   2   3   4   5   6   7   8   9 '
    # nums = s.split()
    # print(nums)
    # for n in nums:
    #     print(s.index(n))

    #print(stacks)

    with open(filepath) as f:
        line_num = 0
        for line in f:
            line = line.strip("\n")
            if (not line.startswith("move") and line_num < 8):
                #print(line)
                col = 1
                stack_index = 0
                while(col <= 33):
                    if (line[col] != ' '):
                        stacks[stack_index].append(line[col])
                    stack_index += 1
                    col += 4
                line_num += 1                
                       
            elif (line.startswith("move")):
                move = line.split(' ')
                moves.append([move[1], move[3], move[5]])
        #print(stacks)
    

def part01():
    #stacks_part01 = stacks.copy()
    top_of_each_stack = ''

    # i = 0
    for move in moves:
        number_moves, move_from, move_to = [int(i) for i in move]
        move_from = move_from - 1
        move_to = move_to - 1

        #print(stacks_part01) 

        for i in range(number_moves):
            # print(number_moves, move_from, move_to)
            # print("Before remove:")                
            # print(stacks_part01[move_from])
            # print(stacks_part01[move_to])
            last_item = stacks_part01[move_from][0]
            del stacks_part01[move_from][0]
            stacks_part01[move_to].insert(0, last_item)
            # print("After remove:")
            # print(stacks_part01[move_from])
            # print(stacks_part01[move_to])
        # i += 1
        # if (i == 3):
        #     return

    for stack in stacks_part01:
        top_of_each_stack += stack[0]

    print(top_of_each_stack)

def part02():
    stacks_part02 = stacks
    top_of_each_stack = ''

    # i = 0
    for move in moves:
        number_moves, move_from, move_to = [int(i) for i in move]
        move_from = move_from - 1
        move_to = move_to - 1
        move_items = stacks_part02[move_from][:number_moves]
        del stacks_part02[move_from][:number_moves]
        stacks_part02[move_to] = move_items + stacks_part02[move_to]

    for stack in stacks:
        top_of_each_stack += stack[0]

    print(top_of_each_stack)



read_input("input.txt")
part02()