day3_data = []
#day3_part2 = []
map_y = 0
map_x = 0
total_trees = 0

with open("/Users/nthatfield/Documents/Projects/Advent-of-Code-2020/day3_input.txt") as file:
    for line in file:
        #print(map_y, map_x, map_x % 32)
        #print(line[map_x % (len(line) - 1)])
        if line[map_x % (len(line) - 1)] == '#':
            total_trees = total_trees + 1
        map_y = map_y + 1
        map_x = map_x + 3

print("The total number of trees is {strees}".format(strees = total_trees))

def count_trees(x_move, y_move):
    map_y2 = 0
    map_x2 = 0
    num_trees = 0
    with open("/Users/nthatfield/Documents/Projects/Advent-of-Code-2020/day3_input.txt") as file:
        for line in file:
            map_width = len(line.strip())
            
            if map_y2 % y_move == 0:
                #print (line[map_x2 % map_width])
                if line[map_x2 % map_width] == '#':
                    num_trees = num_trees + 1
                map_x2 = map_x2 + x_move
                
            map_y2 = map_y2 + 1
            
    return num_trees

#print(count_trees(1, 1))
#print(count_trees(3, 1))
#print(count_trees(5, 1))
#print(count_trees(7, 1))
#print(count_trees(1, 2))

print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))
