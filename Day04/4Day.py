# Advent of Code Day 4
# https://adventofcode.com/2020/day/4
import string

passports = []



with open('4Day.txt', 'r') as f:
    lines = f.readlines()
    
    new_passport = False
    valid_passport_count = 0
    current_passport = []
    adequate_passport = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']

    for line in lines:
        modded_line = line.strip()
        
        if modded_line != '':
            # We're in a passport. Add the labels to a list
            for line_item in modded_line.split(' '):
                if line_item[:3] != 'cid':
                    # Don't append Country ID to list
                    current_passport.append(line_item[:3])
        
        else:
            # We've reached the end of the passport
            # So evaluate it
            # print(current_passport)
            current_passport.sort()
            if current_passport == adequate_passport:
                valid_passport_count += 1
            current_passport = []
        
    # We've reached the end of the passport list
    # So evaluate the last one
    # print(current_passport)
    current_passport.sort()
    if current_passport == adequate_passport:
        valid_passport_count += 1
    current_passport = []
    
    print(f'Valid Passport count: {valid_passport_count}')

########### Part Two
def evalutate_passport(passport):
    valid_passport = False

    try:
        byr = passport['byr']
        iyr = passport['iyr']
        eyr = passport['eyr']
        hgt = passport['hgt']
        hcl = passport['hcl']
        ecl = passport['ecl']
        pid = passport['pid']
    
    except:
        return False
    
    # Evaluate BYR birth year
    if len(byr) != 4:
        return False
    try:
        byr = int(byr)
    except:
        return False
    if byr < 1920 or byr > 2002:
        return False
    
    # Evaluate IYR issue year
    if len(iyr) != 4:
        return False
    try:
        iyr = int(iyr)
    except:
        return False
    if iyr < 2010 or iyr > 2020:
        return False
    
    # Evaluate EYR expiration year
    if len(eyr) != 4:
        return False
    try:
        eyr = int(eyr)
    except:
        return False
    if eyr < 2020 or eyr > 2030:
        return False
    
    # Evaluate height hgt
    units = ''
    height = 0
    try:
        units = hgt[-2:]
        height = int(hgt[:-2])
    except:
        return False
    if units == 'in':
        # fail if height not between 59 and 76
        if height < 59 or height > 76:
            return False
    elif units == 'cm': #150 to 193cm
        if height <150 or height > 193:
            return False
    else:
        # we have a two digit code for height that
        # is neither inches or cm... fail
        return False
    
    # Evaluate HCL Hair Color 
    if hcl[0] == '#':
        if len(hcl[1:]) != 6:
            return False
        else:
            for letter in hcl[1:]:
                if letter not in string.hexdigits:
                    return False
    else:
        return False
    
    # Evaluate ecl Eye Color
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    
    # Evaluate pid Passport ID
    if len(pid) != 9:
        return False
    if not pid.isnumeric():
        return False


    return True

with open('4Day.txt', 'r') as f:
    lines = f.readlines()
    passports = []
    current_passport = {}

    for line in lines:
        modded_line = line.strip()

        if modded_line != '':
            for line_item in modded_line.split(' '):
                if line_item[:3] != 'cid':
                    current_passport[line_item[:3]] = line_item[4:].strip()
        
        else:
            passports.append(current_passport)
            current_passport = {}
    passports.append(current_passport)
    current_passport = {}

valid_passport_count = 0
for passport in passports:
    # print(evalutate_passport(passport))
    if evalutate_passport(passport):
        valid_passport_count += 1

print(valid_passport_count)