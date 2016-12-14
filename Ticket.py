##basic Object composed of several strings, added getter and setter methods and a override to display information

class Ticket:
    def __init__(self, ID, description, priority):
        self.ID = ID
        self.description = description
        self.priority = priority

    def getID (self):
        return self.ID

    def setID (self, ID):
        self.ID = ID

    def getDescription (self):
        return self.description

    def setDescription (self, description):
        self.description = description

    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority


    def __str__ (self):
        return 'ID: %s Description: %s Priority: %s'% (self.ID, self.description, self.priority)