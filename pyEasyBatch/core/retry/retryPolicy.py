class RetryPolicy(object):

    maxAttempts = -1
    delay = None
    timeUnit = None

    def __init__(self):
        pass
    
    def getMaxAttempts(self):
        return self.maxAttempts
    
    def getDelay(self):
        return self.delay
    
    def getTimeUnit(self):
        return self.timeUnit
    
    def toString(self):
        return "{ maxAttempts = " + maxAttempts + ", delay = " + delay + " " + timeUnit + " }"