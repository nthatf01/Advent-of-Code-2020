day1_data = []
day1_part2 = []

with open("/Users/nthatfield/Documents/Projects/Advent of Code 2020/day1_input.txt") as file:
    for line in file:
        line = int(line.strip())
        day1_data.append(line)
        day1_part2.append(2020 - line)

if 1277 in day1_data:
    print("Yes")
else:
    print("No")

for number in day1_data:
    #print(number, 2020 - number)
    if (2020 - number) in day1_data:
        print("Yes", number * (2020 - number))

for number_entry in day1_part2:
    for number in day1_data:
        if (number_entry - number) in day1_data:
            #print("Yes", number, 2020 - number_entry, number_entry - number)
            print("Yes", number * (2020 - number_entry) * (number_entry - number))
