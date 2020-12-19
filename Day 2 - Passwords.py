day2_data = []
#day2_part2 = []

with open("/Users/nthatfield/Documents/Projects/Advent-of-Code-2020/day2_input.txt") as file:
    total_valid_passwords = 0
    for line in file:
        split_line = line.split()
        password_bounds = split_line[0].split("-")
        if split_line[2].count(split_line[1].rstrip(":")) >= int(password_bounds[0]) and split_line[2].count(split_line[1].rstrip(":")) <= int(password_bounds[1]):
            total_valid_passwords = total_valid_passwords + 1

print(total_valid_passwords)
