import string

data = []
with open('/home/pi/Programming/AdventOfCode/2020/Day06/Day06.txt','r') as f:
    data = [l.strip() for l in f.readlines()]

count = 0
letters = string.ascii_lowercase
group = ''
for line in data:
    if len(line) > 0:
        group += line

    else:
        for letter in letters:
            if letter in group:
                count +=1
        group = ''

for letter in letters:
    if letter in group:
        count +=1
group = ''  
print(count)

def letter_in_all_lists(letter, lists):
    for l in lists:
        if letter not in l:
            return False
    return True
group_list = []
count = 0   
## Part two
for line in data:
    if len(line) > 0:
        group_list.append(line)

    else:
        test_first = group_list[0]
        for letter in test_first:
            if letter_in_all_lists(letter, group_list):
                count += 1

        group_list = []
print(count)