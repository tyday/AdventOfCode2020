passwords = []
with open('2day.txt', 'r') as f:
    for line in f.readlines():
        passwords.append(line.strip('\n'))

valid_passwords = []

# part one
def verify_password(password):
    rules, password_actual = password.split(':')[0], password.split(':')[1]
    required_letter = rules.split(' ')[1]
    min_max = rules.split(' ')[0].split('-')
    count_required_letter_appears = password_actual.count(required_letter)
    if count_required_letter_appears >= int(min_max[0]) and count_required_letter_appears <= int(min_max[1]):
        return True
    return False

for password in passwords:
    if verify_password(password):
        valid_passwords.append(password)

print(len(valid_passwords))

## Part Two

def verify_password_two(password):
    rules, password_actual = password.split(':')[0], password.split(':')[1].strip(' ')
    required_letter = rules.split(' ')[1]
    positions = rules.split(' ')[0].split('-')
    positions = [int(i)-1 for i in positions]

    # I would like to do a check here. If position 0 or 1 is less than 0 or if it's greater than length of password actual
    # then return false.

    if password_actual[positions[0]] == required_letter:
        if password_actual[positions[1]] != required_letter:
            return True
    elif password_actual[positions[1]] == required_letter:
        if password_actual[positions[0]] != required_letter:
            return True
    else:
        return False

valid_passwords_version2 = []
for password in passwords:
    if verify_password_two(password):
        valid_passwords_version2.append(password)
print(len(valid_passwords_version2))