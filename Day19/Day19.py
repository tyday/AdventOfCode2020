# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb

def get_data(fileName='/home/pi/Programming/AdventOfCode/2020/Day19/test.txt'):
    rules = {}
    messages = []
    with open(fileName, 'r') as f:
        data = f.read().splitlines()
        for line in data:
            if ":" in line:
                i = line.find(":")
                numb = int(line[:i])
                value = line[i+2:]
                rules[numb] = value.strip('"')
            else:
                messages.append(line)
    return rules, messages
def get_possibilities_alt(ruleNo, rules):
    rule = rules[int(ruleNo)]

    if len(rule) == 1:
        if rule[0].isdigit():
            return get_possibilities_alt(int(rule[0]), rules)
        else:
            return [rule[0]]
    
    elif '|' in rule:
        instructions = rule.split(' | ')
        # left = get_possibilities_alt(instructions[0], rules)
        left = [get_possibilities_alt(i, rules) for i in instructions[0].split(' ')]
        right = [get_possibilities_alt(i, rules) for i in instructions[1].split(' ')]
        # right = get_possibilities_alt(instructions[1], rules)
        return [left + right]
        pass
        # rule is an or statement
        # return [get_possibilities_alt(1), get_possibilities_alt(2)]
    else:
        instructions = rule.split(' ')
        first_result = get_possibilities_alt(instructions[0], rules)
        trailing_results = []
        for inst in instructions[1:]:
            possibilities = get_possibilities_alt(inst, rules)
            # trailing_results.append(get_possibilities_alt(inst, rules))
            trailing_results += possibilities
        results = []
        for res in first_result:
            combined_result = []
            for res2 in trailing_results:
                combined_result.append(res+res2)
            results += (combined_result)
        return results

def get_possibilities(ruleNo, rules):
    rule = rules[ruleNo]
    rule = rule.split(' ')
    if len(rule) == 1:
        if rule[0].isdigit():
            pass
        else:
            return [rule[0]]

    rtnList = ['']

    for item in rule:
        if item == '|':
            rtnList.append('')
        else:
            for i in get_possibilities(int(item), rules):
                if len(i) == 1:
                    rtnList[-1] += i
                else:
                    for item in i:
                        rtnList[-1] += item
                    # rtnList[-1] = [rtnList[-1] + item for item in i]
            # rtnList[-1] = [rtnList[-1] + i for i in get_possibilities(int(item), rules)]
    return rtnList


def partOne():
    print(get_data())


if __name__ == '__main__':
    partOne()
    rules = {0: '4 1 5', 1: '2 3 | 3 2', 2: '4 4 | 5 5', 3: '4 5 | 5 4', 4: 'a', 5: 'b', 6: '4 5', 7: '4 2'}
    print(get_possibilities_alt(4, rules))
    print(get_possibilities_alt(6, rules))
    print(get_possibilities_alt(2, rules))
    print(get_possibilities_alt(1, rules))
    print(get_possibilities_alt(7, rules))