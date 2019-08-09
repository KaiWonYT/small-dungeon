# --------------------------- INIT ---------------------------
try:
    import time
    import re
    from colorama import init, Back
    from zlib import decompress
    from base64 import b64decode
    from sys import exit
except Exception:
    print("The game runs best with Python 3.x and the Colorama, re, Time, zLib, and Base64 Module.") # You only need to install the Colorama module
    exit(0) 
    
init(autoreset=True)
items = []
already_executed = []
all_commands = ["north","south","east","west","items","map","take","investigate"]
current_room = "init"
debug = False

def c_format(color_string): # Automatic color formatting by replacing words
    global all_commands
    temp_string = color_string
    for word in all_commands:
        temp_string = re.sub(word, Back.GREEN + word + Back.RESET, temp_string)
    return temp_string

# --------------------------- BEGINNING ---------------------------

# PRE MAP


def pre_map(index):
    room = [" ", " "]
    room[index] = Back.GREEN + "Y" + Back.RESET
    print(b'eJzjUlDwU0AFXOEK2gquqEIKCsHoqhQwAFRIX1dXVxuIYxBCNQrVtTACKhQDVaUPVgUAEN0UxQ=='.format(room[0],room[1]))
# HOUSE (pre_0)

def pre_0():
    global items
    global already_executed
    global current_room
    current_room = "pre_0"
    if "pre_0" in already_executed:
        dialogue = ["It's cold inside the house, and you feel like you should further investigate the garden."]
    else:
        dialogue = ["You wake up in your house.","It's cold inside, and you spot a man running away from your yard."]
        already_executed.append("pre_0")
    dialogue.append(c_format("You can see your current items, look at the map, or go east towards your garden."))
    for line in dialogue:
        print(line)
    choice = ""
    while choice not in ["east"]: # It's a single list to keep things organized :D
        choice = input("> ").lower()
        if "item" in choice:
            print(items)
        elif "map" in choice:
            pre_map(0)
        elif "east" in choice:
            pre_1()
        else:
            print(c_format("Unknown Command. Try items, or map, or a direction."))

# GARDEN (pre_1)

def pre_1():
    global items
    global already_executed
    global current_room
    current_room = "pre_1"
    if "pre_1" in already_executed:
        dialogue = ["You walk back to your garden.","There is something peculiar about the door lying in the middle of the garden.","You feel like you should further investigate the garden."]
    else:
        dialogue = ["You run towards your garden, but the man has vanished.","There is a mysterious door lying in the middle of the garden."]
        already_executed.append("pre_1")
    dialogue.append(c_format("You can see your current items, look at the map, investigate the mysterious door, or head west/back to your house."))
    for line in dialogue:
        print(line)
    choice = ""
    while choice not in ["investigate","west"]:
        choice = input("> ").lower()
        if "item" in choice:
            print(items)
        elif "map" in choice:
            pre_map(1)
        elif "investigate" in choice:
            pre_2()
        elif "west" in choice:
            pre_0()
        else:
            print("Unknown Command. Try items, or map, or investigate, or a direction.")

# FALLING INTO THE HOLE (pre_2)

def pre_2():
    global items
    global already_executed
    global current_room
    current_room = "pre_2"
    already_executed.append("pre_2")
    dialogue = ["You open the door.","You can't see the bottom of the hole and accidentally fall inside..."]
    for line in dialogue:
        print(line)
    time.sleep(6) # The average human reads about 3 words a second. 16 / 3 is about 5.3; 6 is the closest whole even number which is higher than 5.3.
    for _ in range(50):
        print("")
        time.sleep(1/50)
    print('\x1b[H\x1b[2J', end='') # ANSI codes. This is one reason Colorama is required.

# --------------------------- MAIN GAME ---------------------------

def post_map(index):
    room = [" "," "," "," "," "," "," "," "," "]
    room[index] = Back.GREEN + "Y" + Back.RESET
    compressed_post_map = decompress(b64decode(b'eJzjUlDwU0AF+rq6ujFgFle4graCK4pkjUJ1LZAASSooBKPp0AbS2gpQSQwdcAYXQpc2MkbWCVWMRkAlY9B06uO0Ew6QJGPgOuCSAM1ALos=')).decode("utf-8")
    print(compressed_post_map.format(room[7], room[2],  room[6], room[0], room[1], room[4], room[5], room[3]))


def post_0():
    global items
    global already_executed
    global current_room
    current_room = "post_0"
    if "post_0" in already_executed:
        if "Door Handle" in items:
            dialogue = ["This is where you fell down and picked up the 'Door Handle.'"]
        else:
            dialogue = ["The door seems useful.", "You feel like you should take it with you."]
    else:
        dialogue = ["Your head hurts from the fall.","You don't know you survived.", "There's a door near you."]
        already_executed.append("post_0")
    dialogue.append(c_format("You can see your current items, look at the map, take the door with you, or go east towards your garden."))
    for line in dialogue:
        print(line)
    choice = ""
    while choice not in ["east"]:
        choice = input("> ").lower()
        if "item" in choice:
            print(items)
        elif "map" in choice:
            post_map(0)
        elif "take" in choice:
            if "Door Handle" in items:
                print("There's nothing useful left to take.")
            else:
                print("Picked up the 'Door'! The 'Door' broke... \nPicked up 'Door Handle'?")
                items.append("Door Handle")
        elif "east" in choice:
            post_1()
        else:
            print(c_format("Unknown Command. Try items, map, take, or a valid direction."))

def post_1():
    print("TO BE CONTINUED")


# --------------------------- GAME ---------------------------

# Game Over

def game_over(s):

    global items
    global already_executed

    items = []
    already_executed = []

    print(s)
    print("Do you want to play again? (y / n)")

    choice = ""
    while choice not in ["y","n"]:
        choice = input("> ").lower()
        if choice == "y":
            for _ in range(50):
                print("")
                time.sleep(1/50)
            print('\x1b[H\x1b[2J', end='')
            post_0()
        elif choice == "n":
            exit(0)

# Main


try:
    pre_0()
except Exception as e:
    print(e)