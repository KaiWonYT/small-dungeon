#from player import Player
#from map import Map

class DefaultStory:
    def __init__(self, story_name, firstDialog, nextDialog, available_commands, other_choice):
        self.story_name = story_name
        self.firstDialog = firstDialog
        self.nextDialog = nextDialog
        self.available_commands = available_commands
        self.other_choice = other_choice

    def setMoveChoice(self, move_choice):
        self.move_choice = move_choice

    def run(self, player, map=None):
        self.player = player
        self.map = map
        player.current_room = self.story_name
    
        if(player.hasAlreadyExecuted(self.story_name)):
            self.printLines(self.nextDialog)
        else:
            self.printLines(self.firstDialog)
        print(self.available_commands)
        
        self.choice()

    def choice(self):
        move_choice = self.move_choice
        other_choice = self.other_choice

        all_choices = {**move_choice, **other_choice}

        choice = ""
        while choice not in move_choice.keys():
            choice = input("> ").lower()

            foundFunc = False

            for key in all_choices:
                if key in choice:
                    foundFunc = True
                    all_choices[key](self.player)
            
            if not foundFunc:
                print("Unknown Command. Try items, or map, or a direction.")

    def printLines(self, dialog):
        for line in dialog:
            print(line)