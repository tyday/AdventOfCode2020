# timestamp = 1014511
# businfo = "17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,433,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19"

timestamp = 939
businfo = "17,x,13,19"


# businfo = businfo.split(',')
# buses = [(int(index),int(value)) for index,value in enumerate(businfo) if value != "x"]

def parse_bus_info(businfo):
    businfo = businfo.split(',')
    return [(int(index),int(value)) for index,value in enumerate(businfo) if value != "x"]

def check(buses, index):
    for bus in buses:
        position = bus[0]
        bus_number = bus[1]
        if (index + position) % bus_number != 0:
            return False
    print(buses)
    return True

# Part Two

def partTwo(businfo):
    i = 0
    did_not_pass = True

    max_bus_number = max([y for x,y in businfo])
    max_bus_number_index = max([x for x,y in businfo if y == max_bus_number])

    while(did_not_pass):
        if(check(businfo, i-max_bus_number_index)):
            # Index - index position of the highest number
            did_not_pass = False
            print(f"Index {i}")
        i+=max_bus_number
        # Index plus highest number

def partTwo_Faster(buses):
    # https://www.reddit.com/r/adventofcode/comments/kc5bl5/weird_math_trick_goes_viral/
    # https://www.reddit.com/r/adventofcode/comments/kc5bl5/weird_math_trick_goes_viral/gfotzko/
    pos, increment = 0, buses[0][1]
    for offset, time in buses[1:]:
        while (pos + offset) % time != 0:
            pos += increment

        increment *= time

    return pos

if __name__ == '__main__':
    businfo = "1789,37,47,1889"
    # businfo = "17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,433,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19"

    businfo = parse_bus_info(businfo)
    # partTwo(parse_bus_info(businfo))

    print(partTwo_Faster(businfo))