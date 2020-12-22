day4_data = []
temp_passport = ''
line_break_counter = 0

with open("/Users/nthatfield/Documents/Projects/Advent-of-Code-2020/day4_input.txt") as file:
    while True:
        file_character = file.read(1)
        if not file_character:
            break

        if file_character != '\n':
            temp_passport = temp_passport + file_character
            line_break_counter = 0
        elif line_break_counter == 0:
            line_break_counter = 1
        else:
            day4_data.append(temp_passport)
            temp_passport = ''
            line_break_counter == 0
        


print(day4_data)
