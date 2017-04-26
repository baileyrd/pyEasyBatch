from record import Record
from header import Header
import datetime

POSION_HEADER = Header(0L, "Poison record", datetime.datetime.now())

class PoisonRecord(Record):

    def getHeader(self):
        pass
    
    def getPayload(self):
        pass
    
    def toString(self):
        return 'Poison Record'
    
    def isPoisonRecord(self):
        pass