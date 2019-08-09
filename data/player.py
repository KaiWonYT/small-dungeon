class Player:
    def __init__(self):
        self.resetAll()
    
    def resetAll(self):
        self.items = []
        self.current_room = "init"
        self.all_commands = ["north","south","east","west","items","map","take","investigate"]
        self.already_executed = []

    def hasAlreadyExecuted(self, story_name):
        if story_name in self.already_executed:
            return True
        else:
            self.already_executed.append(story_name)
            return False

    def checkAddItem(self, item):
        if (item in self.items):
            return True
        else:
            self.items.append(item)
            return False

    def checkRemoveItem(self, item):
        if (item in self.items):
            self.items.remove(item)
            return True
        else:
            return False

    def printItems(self):
        if len(self.items) == 0: 
            print("Inventory is empty.")
        else:
            print("Inventory: %s." % ",".join(self.items)) # Using % to support older versions of python