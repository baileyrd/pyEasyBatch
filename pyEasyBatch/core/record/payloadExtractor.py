class PayloadExtractor(object):

    def __init__(self):
        self.payloads = []
    
    def extractPayloads(self, records):
        for record in records:
            self.payloads.append(record)
    
    def getPayloads(self):
        reutrn self.payloads