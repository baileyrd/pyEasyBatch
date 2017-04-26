from fieldExtractor import FieldExtractor

class BeanFieldExtractor(FieldExtractor):


    def __init__(self, type, fields):
        pass
    
    def extractFields(self, payload):
        pass

    def getValue(self, field, object):
        return getters.get(field).invoke(object)