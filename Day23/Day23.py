import time

def set_up(data):
    nodeA = Node(data[0])
    prevNode = nodeA
    lastNode = None
    for i in range(1,len(data)):
        newNode = Node(data[i])
        prevNode.right = newNode
        prevNode = newNode
        lastNode = newNode
    lastNode.right = nodeA
    nodeA.left = lastNode
    return nodeA

def set_up_part2(data):
    nodeA = Node(data[0])
    prevNode = nodeA
    lastNode = None
    for i in range(1,len(data)):
        newNode = Node(data[i])
        prevNode.right = newNode
        prevNode = newNode
        lastNode = newNode
    for i in range(10,1000001):
        newNode = Node(i)
        prevNode.right = newNode
        prevNode = newNode
        lastNode = newNode
    lastNode.right = nodeA
    nodeA.left = lastNode
    return nodeA

class Node:
    def __init__(self, val):
        self.val = int(val)
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)
    def __str__(self):
        return str(self.val)
    def display(self):
        rtnString = str(self.val)
        nxtNode = self.right
        while nxtNode.val != self.val:
            rtnString += str(nxtNode.val)
            nxtNode = nxtNode.right
        return rtnString

def move(current_cup, maxi):
    
    # Splice three cups to the right
    spliced_start = current_cup.right
    spliced_stop = current_cup.right.right.right
    spliced_values = [spliced_start.val, spliced_start.right.val, spliced_stop.val]
    
    #Connect the current cup to the cup after the splice
    spliced_stop.right.left = current_cup
    current_cup.right = spliced_stop.right
    
    
    next_cup = current_cup.right
    original_value = current_cup.val
    value = maxi
    for i in range (current_cup.val-1, current_cup.val -4, -1):
        if i not in spliced_values:
            value = i
            break
    if value <=0:
        value = maxi
        while value in spliced_values:
            value -= 1
    # maxi = current_cup.val
    while value != next_cup.val:
        # if next_cup.val == original_value:
        #     value -= 1
        #     if value <= 0:
        #         value = maxi
        # if maxi < next_cup.val:
        #     maxi = next_cup.val

        next_cup = next_cup.right
    next_cup.right.left = spliced_stop
    spliced_stop.right = next_cup.right
    next_cup.right = spliced_start
    spliced_start.left = next_cup
    
    return current_cup.right


if __name__=='__main__':
    # sample = '389125467'
    sample = '853192647'

    # part 1
    # a = set_up(sample)
    
    # for i in range(2,102):
    #     a = move(a,9)
    #     print(f'{i} : {a.display()}')
    # print(a.display())
    # while a.val != 1:
    #     a = a.right
    # print(a.display())

    # part 2
    start = time.time()
    print(f'Start: {start}')
    a = set_up_part2(sample)
    # print(a.display())
    print('Parsed input')
    currentloop = time.time()+ 30
    last_i = 2
    for i in range(2,10000002):
        a = move(a, 100000)
        if time.time() > currentloop:
            loop_time = time.time() - (currentloop - 30)
            remaining_seconds = ((10000002 - i)/ (i-last_i)) * loop_time
            print(f'{i}/10000002 in {time.time()- start} seconds. {round(loop_time)} for {i - last_i } values. Estimate {round(remaining_seconds)/60} minutes remaining')
            last_i = i
            currentloop = time.time()+ 30
        # print(f'{i} : {a.display()}')
    # print(a.display())
    while a.val != 1:
        a = a.right
    print(a.display())