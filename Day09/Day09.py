
def cannot_find_match(data, target):
    for i in range(len(data)):
        sub_data = data[:]
        val = sub_data.pop(i)
        for j in range(len(sub_data)):
            if val + sub_data[j] == target:
                return False
    return True

def find_weak_point(data, preamble_length):
    i = preamble_length
    while i < len(data):
        sub_list = data[i-preamble_length:i]
        target_value = data[i]
        
        if cannot_find_match(sub_list, target_value):
            return i, target_value
        i += 1
    return None, None


def find_contiguous_list(data, target):
    i,j = 0,1
    not_found = True
    while not_found:
        if sum(data[i:j])< target:
            j += 1
        elif sum(data[i:j])> target:
            i += 1
        else:
            return min(data[i:j]) +max(data[i:j])
        if j >= len(data):
            return None


if __name__=='__main__':
    data = []
    with open ('/home/pi/Programming/AdventOfCode/2020/Day09/input.txt') as f:
        data = f.read().split('\n')
        data = [int(d) for d in data]

    # print(data)
    index, target = find_weak_point(data,25)
    print(find_contiguous_list(data,target))