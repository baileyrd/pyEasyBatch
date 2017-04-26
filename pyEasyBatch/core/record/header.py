class Header:

    def __init__(self, number, source, creationDate):
        self.number = number
        self.source = source
        self.creationDate = creationDate
    
    def getNumber(self):
        return self.number
    
    def getSource(self):
        return self.source
    
    def getCreationDate(self):
        return self.creationDate
