from genericRecord import GenericRecord

class FileRecord(GenericRecord):

    def toString(self):
        return "Record: {" + "\n\theader=[" + self.getHeader + "],\npayload=[" + payload + "]}";


