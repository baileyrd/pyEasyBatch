from retryPolicy import RetryPolicy

class RetryTemplate(object):

    def __init__(self, retryPolicy):
        self.retryPolicy = RetryPolicy()
    
    def execute(self):
        pass
    
    def beforeCall(self):
        pass
    
    def afterCall(self):
        pass
    
    def onException(self):
        pass
    
    def onMaxAttempts(self):
        pass

    def beforeWait(self):
        pass

    def afterWait(self):
        pass