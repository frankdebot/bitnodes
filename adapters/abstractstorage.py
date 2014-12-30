class Abstractstorage(object):
    def factory(self, settings):
        if settings.get('storage','adapter') == 'mysql':
            from adapters.mysql import mysql
            return mysql(settings)    
        
        
    def getHeight(self):
        raise NotImplementedError( "Should have implemented this" )
    
    def insertNode(self, ip, port):
        raise NotImplementedError( "Should have implemented this" )
    
    def updateNode(self, ip, port, date, height):
        raise NotImplementedError( "Should have implemented this" )
    
    
