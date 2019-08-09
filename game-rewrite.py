from data.player import Player
from data.story import DefaultStory
from data.map import Map

import time

player = Player()
map = Map()

def printHello():
    print("You've gone east.")
    exit(0)

def getMap(player):
    print(player.current_room)
    if player.current_room.startswith("pre"):
        map.pre_map(int(player.current_room[-1]))
    if player.current_room.startswith("post"):
        map.post_map(int(player.current_room[-1]))

def getItems(player):
    player.printItems()

pre_0 = DefaultStory("pre_0", 
["You wake up in your house.","It's cold inside, and you spot a man running away from your yard."], 
["It's cold inside the house, and you feel like you should further investigate the garden."], 
"You can see your current items, look at the map, or go east towards your garden.",
{"map":getMap,"item":getItems}
)

pre_1 = DefaultStory("pre_1", 
["You run towards your garden, but the man has vanished.","There is a mysterious door lying in the middle of the garden."], 
["You walk back to your garden.","There is something peculiar about the door lying in the middle of the garden.","You feel like you should further investigate the garden."], 
"You can see your current items, look at the map, investigate the mysterious door, or head west/back to your house.",
{"map":getMap,"item":getItems}
)

def pre_2(player):
    player.hasAlreadyExecuted("pre_2")
    dialogue = ["You open the door.","You can't see the bottom of the hole and accidentally fall inside..."]
    for line in dialogue:
        print(line)
    time.sleep(6) # The average human reads about 3 words a second. 16 / 3 is about 5.3; 6 is the closest whole even number which is higher than 5.3.
    for _ in range(50):
        print("")
        time.sleep(1/50)
    print('\x1b[H\x1b[2J', end='') # ANSI codes. This is one reason Colorama is required.
    post_0() # Place Holder

def post_0():
    print("To Be Continued!")


pre_0.setMoveChoice({"east":pre_1.run})
pre_1.setMoveChoice({"west":pre_0.run,"investigate":pre_2})

pre_0.run(player)