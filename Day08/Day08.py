
def part_one(data):
    visited_indexes = [False for line in data]

    i = 0
    accumulator = 0
    last_index = 0
    count = 0
    while visited_indexes[i] != True:
        count += 1
        last_index = i
        visited_indexes[i] = True
        code = data[i][:3]
        value = int(data[i][4:])

        if code == 'acc':
            accumulator += value
            i += 1
        elif code == 'jmp':
            i += value
        elif code == 'nop':
            i += 1
        else:
            print('Unidentified code')
            i += 1
        
        if i == len(data)-1:
            print('Finished Data')
            print(accumulator)
            return accumulator, -1,-1, count
    
    return accumulator, visited_indexes.index(True), last_index, count




if __name__ =='__main__':
    data = []

    with open('/home/pi/Programming/AdventOfCode/2020/Day08/input.txt', 'r') as f:
        data = f.read().split('\n')
        
    val,repeat_index, bad_pos, count  = part_one(data)
    print('Part One accumulator:', val, 'Index:', bad_pos, 'Repeat index:', repeat_index, 'Line', data[bad_pos])
    
    # for change in ['jmp','acc','nop']:
    #     changed_data = data[:]
    #     if data[bad_pos] != change:
    #         changed_data[bad_pos] = change + data[bad_pos][3:]
    #     print(change, ':')
    #     print(part_one(changed_data))
    count = 0
    for i  in range(len(data)):
        changed_data = data[:]
        if changed_data[i][:3] == 'jmp':
            changed_data[i] = 'nop' + data[bad_pos][3:]
        elif changed_data[i][:3] == 'nop':
            changed_data[i] = 'jmp' + data[bad_pos][3:]
        else:
            pass
        part_one(changed_data)
    
    