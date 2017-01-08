from modules.Colours import Colours

class Map:
    def __init__(self, height, width):
        self.height = height
        self.width  = width
        self.con = None
        self.dim = None

    def bind_console(self, con):
        self.con = con

    def init_map(self):
        self.dim = [[ Cell(False)
            for y in range(self.height) ]
                for x in range(self.width) ]

    def draw_map(self):
        for y in range(self.height):
            for x in range(self.width):
                wall = self.dim[x][y].block_sight
                if wall:
                    self.con.draw_char(x, y, None, fg=None, bg=Colours.dark_wall)
                else:
                    self.con.draw_char(x, y, None, fg=None, bg=Colours.dark_ground)

class Cell:
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

