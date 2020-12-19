day2_data = []
#day2_part2 = []

with open("/Users/nthatfield/Documents/Projects/Advent-of-Code-2020/day2_input.txt") as file:
    total_valid_passwords_part1 = 0
    total_valid_passwords_part2 = 0

    for line in file:
        split_line = line.split()
        password_bounds = split_line[0].split("-")
        if split_line[2].count(split_line[1].rstrip(":")) >= int(password_bounds[0]) and split_line[2].count(split_line[1].rstrip(":")) <= int(password_bounds[1]):
            total_valid_passwords_part1 = total_valid_passwords_part1 + 1
        #print(split_line[2][0])

        if split_line[2][int(password_bounds[0])-1] == split_line[1].rstrip(":") and split_line[2][int(password_bounds[1])-1] != split_line[1].rstrip(":"):
            total_valid_passwords_part2 = total_valid_passwords_part2 + 1
        elif split_line[2][int(password_bounds[0])-1] != split_line[1].rstrip(":") and split_line[2][int(password_bounds[1])-1] == split_line[1].rstrip(":"):
            total_valid_passwords_part2 = total_valid_passwords_part2 + 1

print(total_valid_passwords_part1)
print(total_valid_passwords_part2)
