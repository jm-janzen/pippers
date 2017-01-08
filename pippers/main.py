import tdl

from modules import Entity


# Constants
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
MAP_WIDTH = SCREEN_WIDTH
MAP_HEIGHT = SCREEN_HEIGHT - 5
LIMIT_FPS = 20


def handle_keys():

    user_input = tdl.event.key_wait()

    # Movement keys
    # TODO replace with move method
    if user_input.key == "UP":
        player.y -= 1
    elif user_input.key == "DOWN":
        player.y += 1
    elif user_input.key == "LEFT":
        player.x -= 1
    elif user_input.key == "RIGHT":
        player.x += 1

    # Command keys
    elif user_input.key == "ENTER" and user_input.alt:
        pass
        #tdl.set_fullscreen(True) # XXX this messes up gnome display
    elif user_input.key == "ESCAPE":
        return True

#
# main method
#

class Colo:
    dark_wall = (0, 0, 100)
    dark_ground = (50, 50, 150)

class Cell:
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

def init_map():
    return [[ Cell(False)
        for y in range(MAP_HEIGHT) ]
            for x in range(MAP_WIDTH) ]

def draw_map(map):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = map[x][y].block_sight
            if wall:
                con.draw_char(x, y, None, fg=None, bg=Colo.dark_wall)
            else:
                con.draw_char(x, y, None, fg=None, bg=Colo.dark_ground)


tdl.set_font("pippers/res/arial10x10.png", greyscale=True, altLayout=True)

tdl.setFPS(LIMIT_FPS)

# Create `root' console (shown on screen)
root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="pip init", fullscreen=False)

# Virtual console - a holding area before drawing to root console
con  = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT)

# Init entities
player = Entity.Player(0, 0)
npc    = Entity.Npc(10, 10)

entities = [ npc, player ]

map = init_map()

# Bind entities to our console
for entity in entities:
    entity.bind_console(con)

while not tdl.event.is_window_closed():
    draw_map(map)

    # Draw new entity positions
    for entity in entities:
        entity.draw()

    # Blit contents of con to root console
    root.blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)

    # Redraw root console
    tdl.flush()

    # Clear entities prev positions
    for entity in entities:
        entity.clear()

    # Get user input and handle
    exit_game = handle_keys()
    if exit_game:
        break

