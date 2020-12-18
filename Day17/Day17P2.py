

def parseInput(fileName):
    location_dict = {}
    # Receiving a text file like this:
    #  .#. <-- (1,0,0) <-- (x,y,z)
    #  ..# <-- (2,1,0)
    #  ### <-- (0,2,0), (1,2,0), (2,2,0)
    # return a dictionary of all occupied positions like so:
    # {(1,0,0): 'On',(2,1,0): 'On',(0,2,0): 'On',(1,2,0): 'On',(2,2,0): 'On'}
    with open(fileName, 'r') as f:
        data = f.read()
        data = data.split('\n')
        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == '#':
                    location_dict[(x,y,0,0)] = {'status':True}
        return location_dict

def get_neighbors(location):
    # location is a tuple
    # consisting of (x,y,z)
    # returns every neighbor in 3D space
    # as a list of 3D tuples [(x+1,y+1,z+1),(x+0,y+1,z+1)...]
    neighbors = []
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    neighbor = (location[0]+x, location[1] + y, location[2] +z, location[3]+w)
                    neighbors.append(neighbor)
    neighbors.remove(location)
    return neighbors

def iterate_through_cells(activeLocations):
    activity_dictionary = {}
    activeLocations_nextIteration = {}
    # Go through activeLocations one by one
    # Add each neighbor to a new dictionary
    # if that neighbor is already in the dictionary increment its value by one
    for k,v in activeLocations.items():
        for neighbor in v['neighbors']:
            if neighbor in activity_dictionary:
                activity_dictionary[neighbor] += 1
            else:
                activity_dictionary[neighbor] = 1

    # Go through active locations a second time
    # if its value in activity_direction == 2 or 3:
    #     Add it to  activeLocations_nextIteration
    # Pop it from activity_dictionary
    for k,v in activeLocations.items():
        if k in activity_dictionary:
            if 2 <= activity_dictionary[k] <=3:
                activeLocations_nextIteration[k] = activeLocations[k]
                activity_dictionary.pop(k)


    # the only remaining members of activity_dictionary
    # were inactive
    # Iterate through the remaining members of activity_dictionary
    # if they == 3
    #   Then add them to activeLocations_nextIteration
    for k,v in activity_dictionary.items():
        if v == 3:
            activeLocations_nextIteration[k] = {
                'status':True,
                'neighbors':get_neighbors(k)
                }

    return activeLocations_nextIteration

def partOne(fileName):
    activeLocations = parseInput(fileName)
    for k, v in activeLocations.items():
        activeLocations[k]['neighbors'] = get_neighbors(k)
    # print(activeLocations)
    print_grid(activeLocations)

    count = 0
    key = 'p'
    while key != 'q':
        count += 1
        activeLocations = iterate_through_cells(activeLocations)
        if key == 'p':
            print_grid(activeLocations)
        key = input(f'Turn {count}. Active Cubes: {len(activeLocations)}  Press q to quit, p to print ')

def print_grid(activeLocations):

    x,y,z,w = [],[],[],[]
    for location in activeLocations:
        x.append(location[0])
        y.append(location[1])
        z.append(location[2])
        w.append(location[3])
    
    for ww in range(min(w),max(x)+1):
        for zz in range(min(z),max(z)+1):
            print()
            print(f"{zz:3} " + "".join(str(y) for y in range(min(y),max(y)+1)) + f"   W:{str(ww)}")
            for yy in range(min(y),max(y)+1):
                row = f'{yy:2}  '
                for xx in range(min(x),max(x)+1):
                    value = ''
                    if (xx,yy,zz,ww) in activeLocations:
                        value = '#'
                    else:
                        value = '.'
                    row += value
                print(row)



if __name__=='__main__':
    partOne('/home/pi/Programming/AdventOfCode/2020/Day17/input.txt')

