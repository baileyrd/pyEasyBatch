from recordProcessor import RecordProcessor

class CompositeRecordProcessor(RecordProcessor):
    
    
    def __init__(self, processors = []):
        self.processors = processors

    def processRecord(self, record):
        processedRecord = record
        for processor in self.processors:
            processedRecord = process.processRecord(processedRecord)
            if processedRecord:
                return processedRecord
    
    def addRecordProcessor(recordProcessor):
        processors.add(recordProcessor)