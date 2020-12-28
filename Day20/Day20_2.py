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
    def flipUD(self):
        self.tile = np.flipud(self.tile)
    def get_edges(self):
        edges = []
        edges += [self.tile[0], np.flip(self.tile[0])]
        edges += [self.tile[:,-1], np.flip(self.tile[:,-1])]
        edges += [self.tile[-1], np.flip(self.tile[-1])]
        edges += [self.tile[:,0], np.flip(self.tile[:,0])]
        return edges
    def pop_edges(self):
        return self.tile[1:9,1:9]
    def __repr__(self):
        return f'ImageTile {self.name}'
    def pprint(self):
        pass

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

    def find_pieces(self, width=12):
        tile_map = np.full((width,width), None)
        for i in range(width):
            for j in range(width):
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
                    elif j == width-1:
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
                elif i == width-1:
                    # we are at the bottom edge
                    if j == 0 or j == width-1:
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
                    if j == 0 or j == width-1:
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
    def connect(self, piece, right=None, left=None,above=None,below=None):
        # Connect requires two connections to work right. A top/bottom and a left/right
        # It rotates until left/right connects to a neighbor
        # Then it flips if top/down need to connect.
        #
        # I think that's all it needs to do to be accurate
        horizontal = []
        vertical = []
        h_piece = None
        v_piece = None
        if right:
            horizontal = (2,4) #piece.get_edges()[2:4]
            h_piece = right
        else:
            horizontal = (6,8) #piece.get_edges()[6:]
            h_piece = left
        if above:
            vertical = (0,2) #piece.get_edges()[0:2]
            v_piece = above
        else:
            vertical = (4,6) #piece.get_edges()[4:6]
            v_piece = below
        rotation_unaligned = True
        while rotation_unaligned:
            for edge in piece.get_edges()[horizontal[0]:horizontal[1]]:
                if (edge == h_piece.edges).all(axis=1).any():
                    rotation_unaligned = False
                    break
            # if piece.get_edges()[horizontal[0]:horizontal[1]] in h_piece.edges:
            #     rotation_unaligned = False
            else:
                piece.rotLeft()
        mirrored_unaligned = True
        while mirrored_unaligned:
            for edge in piece.get_edges()[vertical[0]:vertical[1]]:
                if (edge == v_piece.edges).all(axis=1).any():
                    mirrored_unaligned = False
                    break
            # if piece.get_edges()[vertical[0]:vertical[1]] in v_piece.edges:
            #     mirrored_unaligned = False
            else:
                piece.flipUD()
        

    def rotate_pieces(self, width=12):
        for i in range(width):
            for j in range(width):
                if i == width-1:
                    # We're at the bottom. Look up and right
                    if j == width-1:
                        # we're at the end of the row. Look left and up
                        piece = self.tile_map[i][j]
                        horizontal_piece = self.tile_map[i][j-1]
                        vertical_piece = self.tile_map[i-1][j]
                        self.connect(piece, left=horizontal_piece, above=vertical_piece)
                    else:
                        # Look right and up
                        piece = self.tile_map[i][j]
                        horizontal_piece = self.tile_map[i][j+1]
                        vertical_piece = self.tile_map[i-1][j]
                        self.connect(piece, right=horizontal_piece, above=vertical_piece)
                elif j == width-1:
                    # we're on the right. Look left and down
                    piece = self.tile_map[i][j]
                    horizontal_piece = self.tile_map[i][j-1]
                    vertical_piece = self.tile_map[i+1][j]
                    self.connect(piece, left=horizontal_piece, below=vertical_piece)
                else:
                    # we're everywhere else. Look right and down
                    piece = self.tile_map[i][j]
                    horizontal_piece = self.tile_map[i][j+1]
                    vertical_piece = self.tile_map[i+1][j]
                    self.connect(piece, right=horizontal_piece, below=vertical_piece)


def pickle_tiles(totalImage,fileName="tiles"):
    with open(fileName, 'wb') as f:
        pickle.dump(totalImage, f)

def unpickle_tiles(fileName="tiles"):
    with open(fileName, 'rb') as f:
        return pickle.load(f)
def check_image(i,j, check, image):
    for position in check:
        if image[position[0]+i][position[1]+j] != '#':
            return False
    return True

def check_whole_image(seaMonster,monsterPositions, new_map):
    unique, counts = np.unique(new_map, return_counts=True)
    uc = dict(zip(unique, counts))
    for flip in range(2):
        for rotation in range(4):
            i = 0
            j = 0
            monsterCount = 0
            while i + len(seaMonster) < len(new_map):
                j = 0
                while j + len(seaMonster[0])< len(new_map):
                    if check_image(i,j,monsterPositions,new_map):
                        monsterCount += 1
                    
                    j += 1
                i += 1
            print(f"Monster Count: {monsterCount}")
            print(f"Noise = {uc['#'] - (monsterCount * len(monsterPositions))}")
            new_map = np.rot90(new_map)
        new_map = np.flipud(new_map)


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

    totalImage = Tiles(tiles)
    totalImage.neighbor_report()

    # pickle_tiles(totalImage, '/home/pi/Programming/AdventOfCode/2020/Day20/tiles.txt')

    # totalImage = unpickle_tiles('/home/pi/Programming/AdventOfCode/2020/Day20/tiles.txt')
    totalImage.find_pieces(12)
    totalImage.rotate_pieces(12)
    new_map = []
    for row in totalImage.tile_map:
        # new_row = np.array([])
        new_row = [item.pop_edges() for item in row]
        # for item in row:
        #     new_row.append()
        #     new_row.concatenate((item),axis=0)
        new_map.append(np.concatenate(new_row,axis=1))
    new_map = np.concatenate(new_map, axis=0)
    new_map = np.rot90(new_map)
    # for line in new_map:
    #     print("".join(line))
    print(new_map)
    seaMonster = ['                  # ',
                  '#    ##    ##    ###',
                  ' #  #  #  #  #  #   ']
    monsterPositions = []
    for i in range(len(seaMonster)):
        for j in range(len(seaMonster[i])):
            if seaMonster[i][j] == '#':
                monsterPositions.append((i,j))
    print(monsterPositions)

    check_whole_image(seaMonster,monsterPositions, new_map)
    

    
    print('End')