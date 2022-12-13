def read_input(filepath):
    maps = []
    with open(filepath) as f:
        for line in f:
            maps.append(list(line.strip()))
    return maps

def rotate_a_map(m):
    rotated_maps = []
    #????
    rotated_string =  '\n'.join(map("".join, zip(*reversed(m))))
    rotated_strings = rotated_string.split('\n')
    for string in rotated_strings:
        rotated_maps.append(list(string.strip()))
    return rotated_maps


def is_a_visible_tree(map_row, map_col, tree, row, col):
    visible = False
    left = map_row[:(col+1)]
    right = map_row[col:]
    map_col_reverse = map_col[::-1] #Syntax: reversed_list = systems[start:stop:step] 
    top = map_col_reverse[:(row+1)]
    bottom = map_col_reverse[row:]
    
    # print(map_row)
    # print(map_col)
    # print("\n")

    # print(left)
    # print(right)
    # print(top)
    # print(bottom)
    # print('\n')
    if((tree == max(left) and left.count(tree) == 1) or (tree == max(right) and right.count(tree) == 1) or (tree == max(top) and top.count(tree) == 1) or (tree == max(bottom) and bottom.count(tree) == 1)):
        visible = True

    return visible

def part01(a_map):
    number_rows_in_map = len(a_map)
    number_cols_in_map = len(a_map[0])

    total_visible_tree = number_rows_in_map*2 + (number_cols_in_map -2)*2 #total of visible trees on the edges

    rotated_map = rotate_a_map(a_map)
    # print(a_map)
    # print(rotated_map)
    for row, m in enumerate(a_map):
        for col, tree in enumerate(m):
            if(row > 0 and row < number_rows_in_map - 1 and col > 0 and col < number_cols_in_map - 1):    
                #print(row, col, tree)

                map_row = a_map[row]
                map_col = rotated_map[col]

                if(is_a_visible_tree(map_row, map_col, tree, row, col)):
                    total_visible_tree += 1

    print(total_visible_tree)

def count_short_trees(tree, trees):
    count = 0
    for t in trees:
        if (t < tree):
            count +=1
        elif (t >= tree):
            count += 1
            break
    return count

def get_score(map_row, map_col, tree, row, col):
    left = map_row[:col][::-1]
    right = map_row[col+1:]
    map_col_reverse = map_col[::-1] #Syntax: reversed_list = systems[start:stop:step] 
    top = map_col_reverse[:row][::-1]
    bottom = map_col_reverse[row+1:]

    left_scenic_score = count_short_trees (tree, left)
    #right_scenic_score = len([i for i in right if i <= tree])
    right_scenic_score = count_short_trees (tree, right)
    top_scenic_score = count_short_trees (tree, top)
    bottom_scenic_score = count_short_trees (tree, bottom)

    # print(map_row, map_col)
    # print(row, col, tree)
    # print(left,"\n", right,"\n", top,"\n", bottom)
    # print(left_scenic_score, right_scenic_score, top_scenic_score,bottom_scenic_score)

    return left_scenic_score * right_scenic_score * top_scenic_score * bottom_scenic_score


def part02(a_map):
    number_rows_in_map = len(a_map)
    number_cols_in_map = len(a_map[0])

    rotated_map = rotate_a_map(a_map)

    map_scores = []

    for row, m in enumerate(a_map):
        if (row > 0 and row < number_rows_in_map - 1 ):
            map_score = []
            for col, tree in enumerate(m):
                if(col > 0 and col < number_cols_in_map - 1):                    
                    map_row = a_map[row]
                    map_col = rotated_map[col]

                    score = get_score(map_row, map_col, tree, row, col)
                    map_score.append(score)
                    # print(score, "\n")

            map_scores.append(map_score)

    the_highest_scenic_score = max(map_scores[0])
    for map_score in map_scores:
        max_score = max(map_score)
        if(max(map_score) > the_highest_scenic_score):
            the_highest_scenic_score = max_score
    print(the_highest_scenic_score)

a_map = read_input("input.txt")
#part01(a_map)
part02(a_map)