from __future__ import absolute_import

from adapters.abstractstorage import Abstractstorage

class mysql(Abstractstorage):
    
    locks = []
    
    def __init__(self, settings):
        print "Must init"
        import mysql.connector
        self.connection = mysql.connector.connect(user=settings.get('storage_mysql', 'username'),
                                             database=settings.get('storage_mysql', 'database'),
                                             password=settings.get('storage_mysql', 'password'),
                                             host=settings.get('storage_mysql', 'host')
                                             )
        
    
    def insertNode(self, ip, port):
        print "IP: {} port: {}".format(ip, port)
        
        stmt = ("INSERT IGNORE INTO nodes (ip, port) VALUES(%s, %s)")
        stmt_data = (ip, int(port))
        
        cursor = self.connection.cursor()
        
        cursor.execute(stmt, stmt_data)
        self.connection.commit();
        cursor.close()
        
    def updateNode(self, ip, port, height):
        stmt = ("UPDATE nodes SET height=%s, last_seen=NOW() WHERE ip=%s AND port=%s")
        stmt_data = (int(height), ip, int(port))
        
        cursor = self.connection.cursor()
        
        cursor.execute(stmt, stmt_data)
        self.connection.commit();
        cursor.close()
        
    # Checkout a random node which hasn't been checked in the last XX mintus
    # Also care for locking so no 2 workers check out the same host
    def getNextNode(self):
        # Read lock the table
        self.connection.cursor().execute("LOCK TABLES nodes READ")
        
        self.connection.cursor().execute("SELECT * FROM nodes")
        
        
        self.connection.cursor().execute("UNLOCK TABLES")
        
        
