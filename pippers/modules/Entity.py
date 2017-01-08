class Entity:
    """ Base class for visible chars """
    def __init__(self, x, y, char, colo):
        self.x = x
        self.y = y
        self.char = char
        self.colo = colo

    def bind_console(self, con):
        self.con = con

    def bind_map(self, map):
        self.map = map

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.con.draw_char(self.x, self.y, self.char, self.colo)

    def clear(self):
        self.con.draw_char(self.x, self.y, ' ', self.colo)

# TODO perhaps replace with some kind of "movable" interface
class Actor(Entity):
    """ Base class for movable entities """
    def __init__(self, x, y, char, colo):
        Entity.__init__(self, x, y, char, colo)

    def move(self, x, y):
        # TODO check for obstactles
        if not self.map[self.x + x][self.y + y].blocked:
            self.x += x
            self.y += y

class Player(Actor):
    """ User's Actor """
    def __init__(self, x=0, y=0):
        """ Just init a white `@' at top-left """
        Actor.__init__(self, x, y, '@', (255, 255, 255))

class Npc(Actor):
    """ Friendly, Non-Player Character Actor """
    def __init__(self, x=0, y=0):
        """ Just init a white `@' at top-left """
        Actor.__init__(self, x, y, '@', (255, 255, 0))

