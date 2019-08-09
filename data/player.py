class Player:
    def __init__(self):
        self.resetAll()
    
    def resetAll(self):
        self.items = []
        self.current_room = "init"
        self.all_commands = ["north","south","east","west","items","map","take","investigate"]
        self.already_executed = []
