from objectMapper import ObjectMapper

class AbstractRecordMapper(object):
    
    def __init__(self, recordClass):
        self.objectMapper = ObjectMapper(recordClass)
    
    def registerTypeConverter(self, typeConverter):
        self.objectMapper.registerTypeConverter(typeConverter)
