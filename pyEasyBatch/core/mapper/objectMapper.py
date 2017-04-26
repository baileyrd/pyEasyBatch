class ObjectMapper(object):

    setters = None
    typeConverters = None

    def __init__(self, objectType):
        self.objectType = objectType
    

    def mapObject(self):
        pass
    
    def initializeSetters(self):
        pass

    def getSetters(self):
        pass

    def createInstance(self):
        pass

    def convertValue(self, result, field, value, setter, type, typeConverter):
        pass

    def initializeTypeConverters(self):
        pass
    
    def registerTypeConverter(self):
        pass
    
    def getClassName(self):
        pass





