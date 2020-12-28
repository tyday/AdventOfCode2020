import numpy as np
import pickle
from operator import mul

def get_data(fileName):
    tiles = {}
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
    return tiles


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
        self.tile = np.array([[j for j in i] for i in input[1:]])
        self.edges = self.get_edges()
        # self.flipped_tile = [[j for j in reversed(i)] for i in input[1:]]
        # self.sides = self.find_sides(self.tile)
        # self.flipped_sides = self.find_sides(self.flipped_tile)
        # self.neighbor_dict = None
        # self.reversed = False
    def rotLeft(self):
        self.tile = np.rot90(self.tile)
    def rotRight(self):
        self.tile = np.rot90(self.tile,3)
    def get_edges(self):
        edges = []
        edges += [self.tile[0], np.flip(self.tile[0])]
        edges += [self.tile[:,-1], np.flip(self.tile[:,-1])]
        edges += [self.tile[-1], np.flip(self.tile[-1])]
        edges += [self.tile[:,0], np.flip(self.tile[:,0])]
        return edges
    def __repr__(self):
        return f'ImageTile {self.name}'

class Tiles:
    def __init__(self, tiles):
        self.tiles = tiles
        self.neighbors = {}
        self.corner_pieces = []
        self.edge_pieces = []
        self.internal_pieces =[]
        self.tile_map = None
    
    def neighbor_report(self):
        corners = []
        edge_pieces = []
        internal_pieces = []
        other_pieces = []
        for k,v in self.tiles.items():
            neighbors = set()
            for k2, v2 in self.tiles.items():
                if k2 != k:                        
                    # if (v.edges==v2.edges).any():
                    for edge in v.edges:
                        for comparision in v2.edges:
                            if (edge == comparision).all():
                                neighbors.add(k2)
            if len(neighbors) == 2:
                corners.append(k)
                self.corner_pieces.append(v)
            elif len(neighbors) == 3:
                edge_pieces.append(k)
                self.edge_pieces.append(v)
            elif len(neighbors) == 4:
                internal_pieces.append(k)
                self.internal_pieces.append(v)
            else:
                # this shouldn't happen
                other_pieces.append(k)

            self.neighbors[k] = [self.tiles[n] for n in neighbors]
            print(f"{k} has {len(neighbors)} neighbors")
        total = 1
        for item in corners:
            total *= int(item)
        print(f"Corners {corners} = {total}")
        if len(other_pieces) != 0:
            print('Found other pieces:', other_pieces)

    def find_pieces(self):
        tile_map = np.full((12,12), None)
        for i in range(12):
            for j in range(12):
                if i == 0:
                    # we are on the top edge
                    if j == 0:
                        # We are on the corner
                        tile_map[i][j] = self.corner_pieces.pop()
                    elif j == 1:
                        left_tile = tile_map[i][j-1]
                        piece = self.neighbors[left_tile.name][0]
                        tile_map[i][j] = piece
                        if piece not in self.edge_pieces:
                            raise Exception(f'Expected piece "{piece}" not found in self.edge_pieces')
                        self.edge_pieces.remove(piece)
                    elif j == 11:
                        # we are a corner piece
                        left_tile = tile_map[i][j-1]
                        neighbors = self.neighbors[left_tile.name]
                        piece = list(set(neighbors).intersection(set(self.corner_pieces)))[0]
                        tile_map[i][j] = piece
                        self.corner_pieces.remove(piece)
                    else:
                        # We are an edge piece
                        left_tile = tile_map[i][j-1]
                        neighbors = self.neighbors[left_tile.name]
                        piece = list(set(neighbors).intersection(set(self.edge_pieces)))[0]
                        tile_map[i][j] = piece
                        self.edge_pieces.remove(piece)
                elif i == 11:
                    # we are at the bottom edge
                    if j == 0 or j == 11:
                        # we are on the corner
                        top_tile = tile_map[i-1][j]
                        neighbors = self.neighbors[top_tile.name]
                        piece = list(set(neighbors).intersection(set(self.corner_pieces)))[0]
                        
                        if piece not in self.corner_pieces:
                            raise Exception(f'Expected piece "{piece}" not found in self.corner_pieces')
                        tile_map[i][j] = piece
                        self.corner_pieces.remove(piece)
                    else:
                        top_tile = tile_map[i-1][j]
                        left_tile = tile_map[i][j-1]
                        top_neighbors = self.neighbors[top_tile.name]
                        left_neighbors = self.neighbors[left_tile.name]
                        piece = list(set(left_neighbors).intersection(set(self.edge_pieces), set(top_neighbors)))[0]

                        tile_map[i][j] = piece
                        self.edge_pieces.remove(piece)
                else:
                    if j == 0 or j == 11:
                        # we are on the edge
                        top_tile = tile_map[i-1][j]
                        neighbors = self.neighbors[top_tile.name]
                        piece = list(set(neighbors).intersection(set(self.edge_pieces)))[0]
                        
                        if piece not in self.edge_pieces:
                            raise Exception(f'Expected piece "{piece}" not found in self.edge_pieces')
                        tile_map[i][j] = piece
                        self.edge_pieces.remove(piece)
                    else:
                        top_tile = tile_map[i-1][j]
                        left_tile = tile_map[i][j-1]
                        top_neighbors = self.neighbors[top_tile.name]
                        left_neighbors = self.neighbors[left_tile.name]
                        piece = list(set(left_neighbors).intersection(set(self.internal_pieces), set(top_neighbors)))[0]

                        tile_map[i][j] = piece
                        self.internal_pieces.remove(piece)
        self.tile_map = tile_map


def pickle_tiles(totalImage,fileName="tiles"):
    with open(fileName, 'wb') as f:
        pickle.dump(totalImage, f)

def unpickle_tiles(fileName="tiles"):
    with open(fileName, 'rb') as f:
        return pickle.load(f)

if __name__=='__main__':
    tiles = get_data('/home/pi/Programming/AdventOfCode/2020/Day20/input.txt')
    # print(tiles)
    # print(tiles['2311'].tile)
    # a = tiles['2311']
    # print(a.tile)
    # a.rotRight()
    # print(a.tile)
    # a.rotLeft()
    # print(a.tile)

    # totalImage = Tiles(tiles)
    # totalImage.neighbor_report()

    # pickle_tiles(totalImage, '/home/pi/Programming/AdventOfCode/2020/Day20/tiles.txt')

    totalImage = unpickle_tiles('/home/pi/Programming/AdventOfCode/2020/Day20/tiles.txt')
    totalImage.find_pieces()
    print('End')