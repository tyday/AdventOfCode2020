
def get_data(file):
    data = open(file,'r').read().split('\n')
    data = [item.split(" = ") for item in data]
    return data

def apply_mask_to_line(mask,line):
    bval = bin(int(line))[2:]
    rtnValue = []
    for index in range(len(mask)-1, -1, -1):
        line_index = index - (len(mask) - len(bval))
        if line_index < 0:
            # Mask is longer than line. If mask is 1, enter 1 else enter 0
            if mask[index] == '1':
                rtnValue.insert(0,'1')
            else:
                rtnValue.insert(0,'0')
        else:
            if mask[index] != 'X':
                rtnValue.insert(0,mask[index])
            else:
                rtnValue.insert(0,bval[line_index])
    return "".join(rtnValue)

def apply_mask_to_line_Part_two(mask,line):    
    # If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    # If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
    # If the bitmask bit is X, the corresponding memory address bit is floating.
    bval = bin(int(line))[2:]
    rtnValue = []
    for index in range(len(mask)-1, -1, -1):
        line_index = index - (len(mask) - len(bval))
        if line_index < 0:
            # Mask is longer than line. If mask is 1, enter 1 else enter 0
            if mask[index] == '1':
                rtnValue.insert(0,'1')
            elif mask[index] == '0':
                rtnValue.insert(0,'0')
            elif mask[index] == 'X':
                rtnValue.insert(0,'X')
            else:
                # This shouldn't happen
                print('apply_mask_to_line_Part_two().line_index < 0 error')
                print('Mask input was out of bounds')
                
        else:
            if mask[index] == '1':
                rtnValue.insert(0,'1')
            elif mask[index] == '0':
                rtnValue.insert(0,bval[line_index])
            elif mask[index] == 'X':
                rtnValue.insert(0,'X')
            else:
                # This shouldn't happen
                print('apply_mask_to_line_Part_two() error')
                print('Mask input was out of bounds')

            # if mask[index] != 'X':
            #     rtnValue.insert(0,mask[index])
            # else:
            #     rtnValue.insert(0,bval[line_index])
    return "".join(rtnValue)
address_permutations_dictionary = {}
def get_address_permutations(address):
    # Example 00X1101X
    if 'X' not in address:
        address_permutations_dictionary[address]= address
        return [address]
    elif address in address_permutations_dictionary:
        return address_permutations_dictionary[address]
    else:
        # anything before x is unpermutable
        X_index = address.find('X')

        one = address[:X_index+1].replace('X','1')
        zero = address[:X_index+1].replace('X','0')
        
        ones = [one+ permutation for permutation in get_address_permutations(address[X_index+1:])]
        zeroes = [zero+ permutation for permutation in get_address_permutations(address[X_index+1:])]
        total_permutations = ones + zeroes
        address_permutations_dictionary[address] = total_permutations
        return total_permutations
        # if X_index == 0:
        #     # X is the first letter



def partOne(file):
    data = get_data(file)
    mask = None
    memory = {}

    for line in data:
        if line[0] == 'mask':
            mask = line[1]
        else:
            mem_value = apply_mask_to_line(mask, line[1])
            memory[line[0]] = int(mem_value,2)
    
    print(memory)
    sum_of_memory = sum([v for k,v in memory.items()])
    print(f"Sum: {sum_of_memory}")

def partTwo(file):
    data = get_data(file)
    mask = None
    memory = {}

    for line in data:
        if line[0] == 'mask':
            mask = line[1]
        else:
            value = line[1]
            mem = line[0][4:-1]
            mem_search = apply_mask_to_line_Part_two(mask, mem)

            mem_locations = get_address_permutations(mem_search)
            for location in mem_locations:
                memory[location] = int(value)
            # memory[line[0]] = int(mem_value,2)
    sum_of_memory = sum([v for k,v in memory.items()])
    print(f"Sum: {sum_of_memory}")
    return sum_of_memory
    

if __name__=='__main__':
    file='/home/pi/Programming/AdventOfCode/2020/Day14/input.txt'
    # partOne(file)


    # Part two
    mask = '000000000000000000000000000000X1001X'
    ind = '42'
    # print(apply_mask_to_line_Part_two(mask,ind))
    partTwo('/home/pi/Programming/AdventOfCode/2020/Day14/input.txt')

    