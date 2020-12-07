import re
parse_string = re.compile(r'(\d+)\s(.+)(\sbag)')

def parse_bag(line):
    info = line.split('contain')
    name = info[0][:-6] # Will use for dictionary key
    immediate_bag_contents = {}
    contains = info[1][:-1].strip()
    if contains == 'no other bags':
        pass
    else:
        for item in contains.split(','):
            item = item.strip()
            re_search = parse_string.search(item)
            if re_search:
                immediate_bag_contents[re_search.group(2)] = int(re_search.group(1))
            
    
    return name, immediate_bag_contents


if __name__ == '__main__':
    data = []
    with open('/home/pi/Programming/AdventOfCode/2020/Day07/Day07TEST.txt') as f:
        data = f.readlines()
        data = [a.strip() for a in data]

    print(data)
    data_dict = {}
    for bag in data:
        name, immediate_contents = (parse_bag(bag))
        data_dict[name] = {'immediate_contents':immediate_contents, 'all_contents': immediate_contents}
    
    for k,v in data_dict.items():
        print(k)