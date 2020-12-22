day4_data = []
temp_passport = ''
line_break_counter = 0

with open("/Users/nthatfield/Documents/Projects/Advent-of-Code-2020/day4_input.txt") as file:
    while True:
        file_character = file.read(1)
        if not file_character:
            day4_data.append(temp_passport)
            temp_passport = ''
            line_break_counter == 0
            break

        if file_character != '\n':
            temp_passport = temp_passport + file_character
            line_break_counter = 0
        elif line_break_counter == 0:
            temp_passport = temp_passport + " "
            line_break_counter = 1
        else:
            day4_data.append(temp_passport)
            temp_passport = ''
            line_break_counter == 0

total_valid_passports = 0
  
for passport in day4_data:
    temp_check = []
    passport_fields = passport.split()

    for field in passport_fields:
        field_check = field.split(":")
        if field_check[0] != 'cid':
            temp_check.append(field_check[0])

    if len(temp_check) == 7:
        total_valid_passports = total_valid_passports + 1

print(total_valid_passports)
        
