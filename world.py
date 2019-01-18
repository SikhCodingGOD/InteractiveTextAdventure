_world = {}
starting_position = (0, 0)

#this function is used to check if there are tiles adjacent to the tile
#the player is currently at
def tile_exists(x, y):
    return _world.get((x, y))

def load_tiles():
    #Parses a file that describes the world space into the _world object
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    #Assume all rows contain the same number
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == "StartingRoom":
                #sets player starting position to wherever the StartingRoom tile is
                global starting_postion
                starting_postion = (x, y)
            _world[(x,y)] = None if tile_name == '' else getattr(__import__("tiles"),tile_name)(x,y)
