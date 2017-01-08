class Entity:
    """ TODO Base class for visible chars """
    def __init__(self, x, y, char, colo):
        self.x = x
        self.y = y
        self.char = char
        self.colo = colo

    def bind_console(self, con):
        self.con = con

    def draw(self):
        self.con.draw_char(self.x, self.y, self.char, self.colo)

    def clear(self):
        self.con.draw_char(self.x, self.y, ' ', self.colo)

class Actor(Entity):
    """ TODO Base class for movable entities """
    def __init__(self, x, y, char, colo):
        Entity.__init__(self, x, y, char, colo)

    def move(self, x, y):
        self.x += x
        self.y += y


class Player(Actor):
    """ Child of Entity """
    def __init__(self):
        """ Just init a white `@' at top-left """
        Actor.__init__(self, 0, 0, '@', (255, 255, 255))

