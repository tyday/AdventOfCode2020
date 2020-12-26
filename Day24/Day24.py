
antiDirections = {'nw':'se','ne':'sw','e':'w','se':'nw','sw':'ne','w':'e'}
cardinal_directions = ['nw','ne','e','se','sw','w']
def get_location(cl, direction):
    # https://www.redblobgames.com/grids/hexagons/
    # Doubled coordinates
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
        self.neighbors = None
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
    
    def set_neighbors(self, neighbors):
        # neighbors is a dict like {'sw': Hexagon, 'se': Hexagon}
        for k,v in neighbors.items():
            self.__setitem__(k, v)
            if self.neighbors:
                self.neighbors.append(v)
            else:
                self.neighbors = [v]
    def get_neighbors(self):
        if self.neighbors:
            return self.neighbors
        return None
    def flip(self):
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'
    def count_black_neighbors(self):
        if not self.neighbors:
            raise Exception('Hexagon has no confirmed neighbors')
        black_neighbors = [tile for tile in self.neighbors if tile.color == 'black']
        return len(black_neighbors)
    def lives(self):
        self.color = 'black'
    def dies(self):
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
    def get_black_hexagons(self):
        black_hexagons = []
        for hexagon in self.hexagons:
            if self.hexagons[hexagon].color == 'black':
                black_hexagons.append(self.hexagons[hexagon])
        return black_hexagons

    def get_or_create_neighbors(self, tile):
        if tile.neighbors:
            return tile.neighbors
        else:
            neighbors = {d:get_location(tile.location, d) for d in cardinal_directions}
            for k,v in neighbors.items():
                if v in self.hexagons:
                    neighbors[k] = self.hexagons[v]
                else:
                    self.hexagons[v] = Hexagon(v)
                    neighbors[k] = self.hexagons[v]
            tile.set_neighbors(neighbors)
            return tile.neighbors

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

def move(hexagon_list):
    # this method takes a hexagon list and makes changes to it
    # corresponding to the AOC Day 24 rules for life
    black_hexagons = hexagon_list.get_black_hexagons()
    affected_hexagons = set()
    for tile in black_hexagons:
        neighbors = hexagon_list.get_or_create_neighbors(tile)
        affected_hexagons = affected_hexagons.union(set(neighbors))
    affected_hexagons = affected_hexagons.difference(set(black_hexagons))
    
    # Move through black tile list and affect change
    flip_list = []
    for tile in black_hexagons:
        if tile.count_black_neighbors() <= 0:
            flip_list.append(tile)
        elif tile.count_black_neighbors() >= 3:
            flip_list.append(tile)
    for tile in affected_hexagons:
        hexagon_list.get_or_create_neighbors(tile)
        if tile.count_black_neighbors() == 2:
            flip_list.append(tile)
    for tile in flip_list:
        tile.flip()


    


def partOne(data):
    floor = HexagonList()
    for direction in data:
        floor.flip_over(direction)
    print (floor.count_black_hexagons())
    # print(floor.hexagons)
    
def partTwo(data):
    floor = HexagonList()
    for direction in data:
        floor.flip_over(direction)

    day = 0
    play = True
    while play:
        print(f'Day {day}: {floor.count_black_hexagons()}')

        # choice = input('Press enter or "q" to quit ')
        # if choice == 'q':
        #     play = False
        if day == 100:
            play = False
        move(floor)
        day += 1

if __name__=='__main__':
    data = get_data('/home/pi/Programming/AdventOfCode/2020/Day24/input.txt')
    # data = [
    #     ['ne', 'se'],
    #     ['se', 'ne'],
    #     ['se','se'],
    #     ['se','se','w'],
    #     ['se']
    # ]
    # print(data)
    # partOne(data)
    partTwo(data)