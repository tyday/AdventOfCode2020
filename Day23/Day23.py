
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

def move(current_cup):
    
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
    # sample = '389125467'
    sample = '853192647'
    a = set_up(sample)
    
    for i in range(2,102):
        a = move(a)
        print(f'{i} : {a.display()}')
    print(a.display())
    while a.val != 1:
        a = a.right
    print(a.display())