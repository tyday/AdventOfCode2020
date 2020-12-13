import math

directions = {
    'E':{
        'move':(1,0),
        'degrees':90
        },
    'W':{
        'move':(-1,0),
        'degrees':270
    },
    'N':{
        'move':(0,-1),
        'degrees':0
    },
    'S':{
        'move':(0,1),
        'degrees':180
    }
}
directions_two = {
    'E':{
        'move':(1,0),
        'degrees':90
        },
    'W':{
        'move':(-1,0),
        'degrees':270
    },
    'N':{
        'move':(0,1),
        'degrees':0
    },
    'S':{
        'move':(0,-1),
        'degrees':180
    }
}

def getData(fileName = 'input.txt'):
    data = []
    with open(fileName) as f:
        data = f.read().splitlines()
        return data

def change_course(course, change, action):
    degrees = directions[course]['degrees']
    if action == 'R':
        degrees = (degrees + change)%360
    else:
        degrees = (degrees - change)%360
    # degrees = (degrees + change)%360
    for k,v in directions.items():
        if v['degrees'] == degrees:
            return k
    print('Failed to find change_course()')
    return None

def rotate_waypoint(x,y ,action, value):
    # change = change % 360
    # if change not in [0,90,180,270]:
    #     print('Failed in rotate_waypoint')
    #     return waypoint
    # y = y * -1 # Our grid is flipped (it's like an array )
    if action == 'R':
        value *= -1
    # X' = x*cos(theta) - y*sin(theta)
    # Y' = y*cos(theta) + x*sin(theta)
    value = math.radians(value)
    x1 = x*math.cos(value) - y * math.sin(value)
    y1 = y*math.cos(value) + x*math.sin(value)
    return (round(x1), round(y1))

    

def partOne(data):
    x,y = 0,0
    course = 'E'
    for line in data:
        action = line[0]
        value = int(line[1:])
        if action == 'F':
            x += directions[course]['move'][0] * value
            y += directions[course]['move'][1] * value
        elif action in 'NSEW':
            x += directions[action]['move'][0] * value
            y += directions[action]['move'][1] * value
        elif action in 'LR':
            course = change_course(course, value, action)
            # x += directions[course]['move'][0] * value
            # y += directions[course]['move'][1] * value
        else:
            'Something went wrong in partOne()'
    print(f'x,y: {x,y}')
    print(f'Manhattan distance: {abs(x)+abs(y)}')

            
def partTwo(data):
    ship_position = {'x':0,'y':0}
    way_point = {'x':10,'y':1}

    for line in data:
        action = line[0]
        value = int(line[1:])

        if action in 'NSEW':
            # move way_point NSEW
            way_point['x'] += directions_two[action]['move'][0] * value
            way_point['y'] += directions_two[action]['move'][1] * value
        if action in 'RL':
            #rotate way_point
            new_coords = rotate_waypoint(way_point['x'],way_point['y'], action, value)
            way_point['x'] = new_coords[0]
            way_point['y'] = new_coords[1]
        if action == 'F':
            # move ship towards waypoint
            ship_position['x'] += way_point['x'] * value
            ship_position['y'] += way_point['y'] * value
        # print(f'{line} :: {ship_position} - waypoint {way_point}')
    print(f'Ship position: {ship_position} - waypoint {way_point}')
    print(f"Manhattan distance: {abs(ship_position['x']) + abs(ship_position['y'])}")
    return ship_position

if __name__=='__main__':
    data = getData('/home/pi/Programming/AdventOfCode/2020/Day12/input.txt')
    # data = ['E10','W10','N10','S10','F10', 'R90', 'F10']
    # data = ['F10','N3','F7', 'R90','F11']
    # partOne(data)
    partTwo(data)