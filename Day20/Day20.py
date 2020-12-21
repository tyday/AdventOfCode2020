
class ImageTile:
    def __init__(self,input):
        # input looks like this:
        #   ['Tile 1951:',
        #    '#.##...##.',
        #    '#.####...#',
        #    '.....#..##',
        #    '#...######',
        #    '.##.#....#',
        #    '.###.#####',
        #    '###.##.##.',
        #    '.###....#.',
        #    '..#.#..#.#',
        #    '#...##.#..']
        self.name = input[0][input[0].find(' ')+1:-1]
        self.tile = [[j for j in i] for i in input[1:]]
        self.flipped_tile = [[j for j in reversed(i)] for i in input[1:]]
        self.sides = self.find_sides(self.tile)
        self.flipped_sides = self.find_sides(self.flipped_tile)
        self.neighbor_dict = None
        self.reversed = False
    
    def find_sides(self, tile):
        sides = []
        sides.append(tile[0])
        sides.append([a[9] for a in tile])
        sides.append(tile[9])
        sides.append([a[0] for a in tile])
        return sides
    
    def get_neighbors(self, neighbors, reversed = False):
        if self.neighbor_dict != None:
            return self.neighbor_dict
        neighbor_dict = {0:[],1:[],2:[],3:[]}
        tile = None
        sides = None
        if reversed:
            tile = self.flipped_tile
            sides = self.flipped_sides
        else:
            tile = self.tile
            sides = self.sides
        for i in range(len(sides)):
            for neighbor in neighbors:
                if sides[i] in neighbor.sides:
                    neighbor_dict[i].append(neighbor.name)
        
        self.neighbor_dict = neighbor_dict
        return neighbor_dict
    
    def neighbor_report(self, neighbors, verbose=False):
        message = ''
        count = 0
        for k,v in self.get_neighbors(neighbors).items():
            if len(v) > 0:
                count += 1
            message += f"   Side {k} has {len(v)} possible neighbors.\n"
        message = f"{self.name} has possible neighbors on {count} sides.\n" + message
        if verbose:
            print(message)
        return count

    def flip(self):
        self.reversed = not self.reversed
        self.tile, self.flipped_tile = self.flipped_tile, self.tile
        self.sides, self.flipped_sides = self.flipped_sides, self.sides
        self.neighbor_dict = None
        if self.reversed:
            self.name += "R"
        else:
            self.name = self.name[:-1]


def get_data(fileName, tiles):
    with open(fileName, 'r') as f:
        data = f.read().splitlines()
        current_tile = []
        current_tile_name = ''
        for line in data:
            if line.startswith('Tile'):
                current_tile_name = line[line.find(' ')+1:-1]
                current_tile.append(line)
            elif line == "":
                tiles[current_tile_name] = ImageTile(current_tile)
                current_tile_name = ''
                current_tile = []
            else:
                current_tile.append(line)
        tiles[current_tile_name] = ImageTile(current_tile)
                

def tiles_summary(tiles):
    tile_list = [v for k,v in tiles.items()]
    for k,v in tiles.items():
        ind_list = [i for i in tile_list if i != v]
        print(v.neighbor_report(ind_list))

def flip_tiles(tiles):
    # complete_run = False
    
    # while not complete_run:
    #     not_flipped = True
    #     tile_list = [v for k,v in tiles.items()]
    #     while not_flipped:
    #         for k,v in tiles.items():
    #             ind_list = [i for i in tile_list if i != v]
    #             nbors = v.neighbor_report(ind_list,verbose=True)
    #             if nbors == 0:
    #                 print(f"---------------Flipped {k}-------------")
    #                 v.flip()
    #                 not_flipped == False
    #                 break
    #         # complete_run = True
    for i in range(2):
        tile_list = [v for k,v in tiles.items()]
        for k,v in tiles.items():
            ind_list = [i for i in tile_list if i != v]
            nbors = v.neighbor_report(ind_list,verbose=True)
            if nbors == i:
                if not v.reversed:
                    print(f"---------------Flipped {k}-------------")
                    v.flip()
    print('------------------Final Form -------------------')
    tile_list = [v for k,v in tiles.items()]
    for k,v in tiles.items():
        ind_list = [i for i in tile_list if i != v]
        nbors = v.neighbor_report(ind_list,verbose=True)




if __name__=='__main__':
    tiles = {}
    get_data('/home/pi/Programming/AdventOfCode/2020/Day20/sample.txt', tiles)
    # tiles_summary(tiles)
    flip_tiles(tiles)



                