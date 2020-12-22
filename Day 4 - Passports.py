import re

day4_data = []
temp_passport = ''
line_break_counter = 0

def validate_field(field, value):
    if field == 'byr':
        if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
            return True
        else:
            return False
    elif field == 'iyr':
        if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
            return True
        else:
            return False
    elif field == 'eyr':
        if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
            return True
        else:
            return False
    elif field == 'hgt':
        if value[-2:] == 'in' and int(value.rstrip('in')) >= 59 and int(value.rstrip('in')) <= 76:
            return True
        elif value[-2:] == 'cm' and int(value.rstrip('cm')) >= 150 and int(value.rstrip('cm')) <= 193:
            return True
        else:
            return False
    elif field == 'hcl' and value[0] == '#' and len(value) == 7:
        regex = re.compile('[a-f0-9]{6}')
        if regex.search(value) is None:
            return False
        else:
            return True
    elif field == 'ecl':
        if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
        else:
            print(value)
            return False
    elif field == 'pid' and value.isdecimal() and len(value) == 9:
        return True
    
    return False

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

total_valid_passports1 = 0
total_valid_passports2 = 0

  
for passport in day4_data:
    temp_check = []
    valid_fields = 0
    passport_fields = passport.split()

    for field in passport_fields:
        field_check = field.split(":")
        if field_check[0] != 'cid':
            temp_check.append(field_check[0])
        if validate_field(field_check[0], field_check[1]):
            valid_fields = valid_fields + 1

    if len(temp_check) == 7:
        total_valid_passports1 = total_valid_passports1 + 1
        if valid_fields == 7:
            total_valid_passports2 = total_valid_passports2 + 1
        
print(total_valid_passports1)
print(total_valid_passports2)
        
