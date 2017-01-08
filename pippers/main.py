import tdl

from modules import Entity


def handle_keys():

    user_input = tdl.event.key_wait()

    # Movement keys
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

# Constants
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

tdl.set_font("pippers/res/arial10x10.png", greyscale=True, altLayout=True)

tdl.setFPS(LIMIT_FPS)

# Create `root' console (shown on screen)
root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="pip init", fullscreen=False)

con  = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT)

# Init player
player = Entity.Player()

# Bind player to our console
player.bind_console(con)

while not tdl.event.is_window_closed():

    # Draw new player pos
    player.draw()

    # Blit contents of con to root console
    root.blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)

    # Redraw root console
    tdl.flush()

    # Clear player prev pos
    player.clear()

    # Get user input and handle
    exit_game = handle_keys()
    if exit_game:
        break

