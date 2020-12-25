
antiDirections = {'nw':'se','ne':'sw','e':'w','se':'nw','sw':'ne','w':'e'}
def get_location(cl, direction):
    if direction == 'nw':
        return (cl[0]-1, cl[1]-1)
    elif direction == 'ne':
        return (cl[0]+1, cl[1]-1)
    elif direction == 'sw':
        return (cl[0]-1, cl[1]+1)
    elif direction == 'se':
        return (cl[0]+1, cl[1]+1)
    elif direction == 'e':
        return (cl[0]+2, cl[1])
    elif direction == 'w':
        return (cl[0]-2, cl[1])
    else:
        raise Exception(f'get_location direction ({direction}) out of bounds.')
class Hexagon:
    def __init__(self, location, color='white'):
        self.color = color
        self.location = location
        self.nw = None
        self.ne = None
        self.e = None
        self.se = None
        self.sw = None
        self.w = None
    def __getitem__(self, item):
        item_dict = {
            'nw':self.nw,
            'ne':self.ne,
            'e':self.e,
            'se':self.se,
            'sw':self.sw,
            'w':self.w,
        }
        return item_dict[item]
    def __setitem__(self,item,newValue):
        if item == 'nw':
            self.nw = newValue
        elif item == 'ne':
            self.ne = newValue
        elif item == 'sw':
            self.sw = newValue
        elif item == 'se':
            self.se = newValue
        elif item == 'e':
            self.e = newValue
        elif item == 'w':
            self.w = newValue
        else:
            raise Exception('Item not in Hexagon')
    def __repr__(self):
        return f"Hex:{self.location}:{self.color}"
    def flip(self):
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'

class HexagonList:
    def __init__(self):
        self.reference = Hexagon((0,0),'white')
        self.hexagons = {}
        self.hexagons[(0,0)] = self.reference
    
    def traverse(self, directions):
        if len(directions) <1:
            return self.reference
        else:
            current_tile = self.reference
            for i in directions:
                if current_tile[i]:
                    current_tile = current_tile[i]
                else:
                    location = get_location(current_tile.location, i)
                    if location in self.hexagons:
                        current_tile[i] = self.hexagons[location]
                        current_tile = current_tile[i]
                    else:
                        newTile = Hexagon(location)
                        newTile[antiDirections[i]] = current_tile
                        current_tile[i] = newTile

                        self.hexagons[location] = newTile
                        current_tile = current_tile[i]
            return current_tile
        
    def flip_over(self,directions):
        tile_to_flip = self.traverse(directions)
        tile_to_flip.flip()
    
    def count_black_hexagons(self):
        count = 0
        for hexagon in self.hexagons:
            if self.hexagons[hexagon].color == 'black':
                count += 1
        return count

def get_data(fileName):
    data = []
    returnData = []
    with open(fileName, 'r') as f:
        data = f.read().split('\n')
    # return data
    for line in data:
        i = 0
        newline = []
        while i < len(line):
            if line[i] == 's' or line[i] =='n':
                newline.append(line[i:i+2])
                i += 2
            else:
                newline.append(line[i])
                i += 1
        returnData.append(newline)
    return returnData

def partOne(data):
    floor = HexagonList()
    for direction in data:
        floor.flip_over(direction)
    print (floor.count_black_hexagons())
    # print(floor.hexagons)
    

if __name__=='__main__':
    data = get_data('/home/pi/Programming/AdventOfCode/2020/Day24/input.txt')
    # data = [
    #     ['ne', 'se'],
    #     ['se', 'ne']
    # ]
    # print(data)
    partOne(data)