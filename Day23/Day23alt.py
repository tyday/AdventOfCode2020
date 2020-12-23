import time
from collections import deque

def set_up(data):
    numbs = deque([int(i) for i in data])
    return numbs

# def set_up_part2(data):
#     numbs = deque(data)
#     for i in range(10,1000001):
#         newNode = Node(i)
#         prevNode.right = newNode
#         prevNode = newNode
#         lastNode = newNode
#     lastNode.right = nodeA
#     nodeA.left = lastNode
#     return nodeA

def get search_value(val, pickup, max):
    for i in range(val -1,val - 4, -1):
        if i not in pickup:
            return i
def move(cup_list):
    current_cup = cup_list.popleft()
    pickup = []
    for i in range(3):
        pickup.append(current_cup.popleft)
    search_value = None
    


def moveOLD(current_cup):
    
    # Splice three cups to the right
    spliced_start = current_cup.right
    spliced_stop = current_cup.right.right.right
    
    #Connect the current cup to the cup after the splice
    spliced_stop.right.left = current_cup
    current_cup.right = spliced_stop.right
    
    
    next_cup = current_cup.right
    original_value = current_cup.val
    value = current_cup.val - 1
    max = current_cup.val
    while value != next_cup.val:
        if next_cup.val == original_value:
            value -= 1
            if value <= 0:
                value = max
        if max < next_cup.val:
            max = next_cup.val

        next_cup = next_cup.right
    next_cup.right.left = spliced_stop
    spliced_stop.right = next_cup.right
    next_cup.right = spliced_start
    spliced_start.left = next_cup
    
    return current_cup.right


if __name__=='__main__':
    sample = '389125467'
    # sample = '853192647'

    # part 1
    a = set_up(sample)
    
    for i in range(2,12):
        a = move(a)
        print(f'{i} : {a.display()}')
    print(a.display())
    while a.val != 1:
        a = a.right
    print(a.display())

    # part 2
    # start = time.time()
    # print(f'Start: {start}')
    # a = set_up_part2(sample)
    # # print(a.display())
    # print('Parsed input')
    # currentloop = time.time()+ 30
    # last_i = 2
    # for i in range(2,10000002):
    #     a = move(a)
    #     if time.time() > currentloop:
    #         loop_time = time.time() - (currentloop - 30)
    #         remaining_seconds = ((10000002 - i)/ (i-last_i)) * loop_time
    #         print(f'{i}/10000002 in {time.time()- start} seconds. {round(loop_time)} for {i - last_i } values. Estimate {round(remaining_seconds)/60} minutes remaining')
    #         last_i = i
    #         currentloop = time.time()+ 30
    #     # print(f'{i} : {a.display()}')
    # # print(a.display())
    # while a.val != 1:
    #     a = a.right
    # print(a.display())