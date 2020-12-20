import re

def get_data(fileName='/home/pi/Programming/AdventOfCode/2020/Day19/test.txt'):
    rules = {}
    messages = []
    with open(fileName, 'r') as f:
        data = f.read().splitlines()
        for line in data:
            if ":" in line:
                i = line.find(":")
                numb = line[:i]
                value = line[i+2:]
                rules[numb] = value.strip('"')
            else:
                if line != '':
                    messages.append(line)
    return rules, messages

def get_reg_ex(rule, rules):
    if rule in rules:
        if len(rules[rule]) == 1:
            return rules[rule]
        else:
            return get_reg_ex(rules[rule], rules)
    elif '|' in rule:
        variations = []
        var_list = rule.split(' | ')
        for i in range(rule.count('|')+1):
            variations.append(get_reg_ex(var_list[i], rules))

        # left = rule.split(' | ')[0]
        # right = rule.split(' | ')[1]
        # left = f"{get_reg_ex(left, rules)}"
        # right = get_reg_ex(right, rules)
        rtnValue = "|".join(variations)
        return f"({rtnValue})"
        # return f"({left}|{right})"
    else:
        return_regex = ''
        rule_list = rule.split(' ')
        for item in rule_list:
            return_regex += get_reg_ex(item, rules)
        return return_regex

def partOne(fileName):
    rules, messages = get_data(fileName)
    reggie = get_reg_ex('0', rules)
    reggie = '^' + reggie + '$'
    count = 0
    print(reggie)
    for message in messages:
        if re.search(reggie, message):
            count += 1
    print(count)

def partTwo(fileName):
    rules, messages = get_data(fileName)
    # rules['8'] = '42 | 42 42'
    # rules['11'] = '42 31 | 42 42 31 31'
    rules['11'] = '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31'
    rules['8'] = '42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42'
    reggie = get_reg_ex('0', rules)
    reggie = '^' + reggie + '$'
    count = 0
    for message in messages:
        if re.search(reggie, message):
            count += 1
    print(count)

if __name__ =='__main__':
    # partOne('/home/pi/Programming/AdventOfCode/2020/Day19/input.txt')
    partTwo('/home/pi/Programming/AdventOfCode/2020/Day19/input.txt')

    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31

    # 42: 9 14 | 10 1
    # 31: 14 17 | 1 13