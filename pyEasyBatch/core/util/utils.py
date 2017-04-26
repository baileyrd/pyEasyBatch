class Utils(object):

    LINE_SEPARATOR = ''
    FILE_SEPARATOR = ''
    DATE_FORMAT = "yyyy-MM-dd hh:mm:ss"
    DURATION_FORMAT = "%shr %smin %ssec %sms"
    NOT_APPLICABLE = "N/A"


    def __init__(self):
        pass
    
    def checkNotNull(arguement, arguementName):
        if