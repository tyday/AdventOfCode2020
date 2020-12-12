import copy, pprint
from enum import Enum

DIRECTIONS = ['NW','N','NE','W','E','SW','S','SE']
class Direction(Enum):
    NW = (-1,-1)
    N = (0,-1)
    NE = (1,-1)
    W = (-1,0)
    E = (1,0)
    SW = (-1,1)
    S = (0,1)
    SE = (1,1)

def get_neighbor(data,x,y):
    # returns occupant of position
    # or None if outside bounds of data 
    if -1 < x < len(data[0]):
        if -1 < y < len(data):
            return data[y][x]
    return None


def get_visible_neighbors(data, x,y):
    # returns number of occupied seats
    nbors = []
    open_spaces = []
    for direction in DIRECTIONS:
        next_neighbor = True
        xx, yy = x,y
        while next_neighbor:
            xx = xx + Direction[direction].value[0]
            yy = yy + Direction[direction].value[1]
            nbor = get_neighbor(data, xx,yy)
            if nbor == None:
                next_neighbor = False
            elif nbor == '.':
                open_spaces.append((xx,yy))
                nbors.append(nbor)
            elif nbor == '#':
                nbors.append('#')
                next_neighbor = False
            else:
                next_neighbor = False
    # return nbors.count('#'), open_spaces
    return nbors.count('#')


def neighbors(data, x,y):
    width = len(data[0])
    nbors = []
    if y > 0:
        #NW
        if x > 0:
            nbors.append(data[y-1][x-1])
        #N
        nbors.append(data[y-1][x])
        #NE
        if x < width - 1:
            nbors.append(data[y-1][x+1])

    #W
    if x > 0:
        nbors.append(data[y][x-1])
    #E
    if x < width-1:
        nbors.append(data[y][x+1])

    if y < len(data) -1:
        #SW
        if x > 0:
            nbors.append(data[y+1][x-1])
        #S
        nbors.append(data[y+1][x])
        #SE
        if x < width -1:
            nbors.append(data[y+1][x+1])

    return nbors

def get_next_pos(data, x,y):
    nbors = neighbors(data, x,y)
    seat = data[y][x]
    # if seat is empty and there are no occupied adjacent seats
    # then seat becomes occupied
    if seat == 'L' and '#' not in nbors:
        seat = '#'
    # if seat is occupied and 4 or more adjacent seats are occupied
    # Then seat becomes empty
    elif seat == '#' and nbors.count('#') >=4:
        seat = 'L'
    else:
        pass
    return seat

def get_next_pos_two(data, x,y):
    seat = data[y][x]
    visible_neighbors = get_visible_neighbors(data,x,y)
    # if seat is empty and there are no occupied adjacent seats
    # then seat becomes occupied
    if seat == 'L' and visible_neighbors ==0:
        seat = '#'
    # if seat is occupied and 5 or more adjacent seats are occupied
    # Then seat becomes empty
    elif seat == '#' and visible_neighbors >=5:
        seat = 'L'
    else:
        pass
    return seat

def partOne(data):
    key = ''
    count = 0
    while (key != 'q'):
        occupied_seats = 0
        # pprint.pprint(data)
        new_data = copy.deepcopy(data)
        for y in range( len(data)):
            for x in range( len(data[y])):
                new_data[y][x] =get_next_pos(data,x,y)
        if key == 'a':
            print('data')
            pprint.pprint(data)
            print('copy')
            pprint.pprint(new_data)
        if new_data == data:
            print("We've equilibrated")
            occupied_seats = sum([row.count('#') for row in data])
            print(f"Occupied seats = {occupied_seats}")
            key = 'q'
        data = new_data
        # key = input("Enter to continue. 'q' to quit. 'a' to print extra data. ")
    

def partTwo(data):
    # get_visible_neighbors(data,0,0)
    key = ''
    count = 0
    while (key != 'q'):
        occupied_seats = 0
        # pprint.pprint(data)
        new_data = copy.deepcopy(data)
        for y in range( len(data)):
            for x in range( len(data[y])):
                new_data[y][x] =get_next_pos_two(data,x,y)
        if key == 'a':
            print('data')
            pprint.pprint(data)
            print('copy')
            pprint.pprint(new_data)
        if new_data == data:
            print("We've equilibrated")
            occupied_seats = sum([row.count('#') for row in data])
            print(f"Occupied seats = {occupied_seats}")
            key = 'q'
        data = new_data
        # key = input("Enter to continue. 'q' to quit. 'a' to print extra data. ")

if __name__=='__main__':
    data = []
    with open('/home/pi/Programming/AdventOfCode/2020/Day11/input.txt') as f:
        data = f.read()
        data = data.split('\n')
    for y in range(len(data)):
        data[y] = list(data[y])

    # data = [[0,1,2],[3,4,5],[6,7,8]]
    pprint.pprint(data)
    # print(neighbors(data,2,2))

    partOne(data)

    partTwo(data)
    # print(get_visible_neighbors(data,6,1))
    
            