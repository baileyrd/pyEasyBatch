from header import Header

class GenericRecord(object):

    _header = Header()
    _payload = payload

    def __init__(self, header, payload):
        self._header = header
        self._payload = payload
    
    def getHeader(self):
        return self._header
    
    def getPayload(self):
        return self._payload
    
    def toString(self):
        return "Record: {" + "\n\theader=[" + self.getHeader + "],\npayload=[" + payload + "]}";