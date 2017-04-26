class JobMonitorProxy(object):

    def __init__(self):
        pass
    
    def addMonitoringListener(self, jobMonitoringListener):
        notificationListeners.add(jobMonitoringListener)
    
    def run(self):
        pass
    
    def registerNotificationListeners(self):
        pass
    