from recordProcessor import RecordProcessor

class RecordCollector(RecordProcessor):

    def __init__(self):
        self.records = []
    
    def processRecord(self, record):
        records.append(record)
    

    def getRecords(self):
        return records