import tdl

from modules import Entity
from modules import Colours
from modules import Map


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
        player.move(0, -1)
    elif user_input.key == "DOWN":
        player.move(0, 1)
    elif user_input.key == "LEFT":
        player.move(-1, 0)
    elif user_input.key == "RIGHT":
        player.move(1, 0)

    # Command keys
    elif user_input.key == "ENTER" and user_input.alt:
        pass
        #tdl.set_fullscreen(True) # XXX this messes up gnome display
    elif user_input.key == "ESCAPE":
        return True

#
# main method
#

# TODO move to setup script
tdl.set_font("pippers/res/arial10x10.png", greyscale=True, altLayout=True)
tdl.setFPS(LIMIT_FPS)

# Create `root' console (shown on screen)
root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="pip init", fullscreen=False)

# Virtual console - a holding area before drawing to root console
con  = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT)

# Init entities
player = Entity.Player(29, 21)
npc    = Entity.Npc(10, 10)

entities = [ npc, player ]

# Define & init map object
map = Map.Map(MAP_HEIGHT, MAP_WIDTH)
map.bind_console(con)
map.init_map()

# Bind entities to our console, map dimensions
for entity in entities:
    entity.bind_console(con)
    entity.bind_map(map.dim)

while not tdl.event.is_window_closed():

    map.draw_map()

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

