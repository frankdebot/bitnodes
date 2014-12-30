#!/usr/bin/env python

import sys
import socket
import logging
import pprint
import time

from ConfigParser import ConfigParser

from protocol import ProtocolError, ConnectionError, Connection, DEFAULT_PORT
from adapters.abstractstorage import Abstractstorage


SETTINGS = {}

def main(argv):
    
    address = argv[1]
    port = 9333

    SETTINGS['socket_timeout'] = 10
    SETTINGS['user_agent'] = "/Satoshi:0.8.6/"
    
    height = 0
    
    redefinelogging()
    
    conf = ConfigParser();
    conf.read('storage.conf')
        
    storage = Abstractstorage().factory(conf)
    storage.insertNode(address, 9333)

    #getseeds(storage)
    
    connection = Connection((address, int(port)),
                            socket_timeout=SETTINGS['socket_timeout'],
                            user_agent=SETTINGS['user_agent'],
                            height=height)

    try:
        logging.debug("Connecting to {}".format(connection.to_addr))
        connection.open()
        handshake_msgs = connection.handshake()
        
        # Update node
        storage.updateNode(address, 9333, handshake_msgs[0].get('height', 0))
        
        # Expand the network
        addr_msgs = connection.getaddr()
        for addr_msg in addr_msgs:
            if 'addr_list' in addr_msg:
                for peer in addr_msg['addr_list']:
                    age = int(time.time()) - peer['timestamp']  # seconds
                    address = peer['ipv4'] if peer['ipv4'] else peer['ipv6']
                    port = peer['port'] if peer['port'] > 0 else 9333
                    
                    if age < 86400:
                        storage.insertNode(address, port)
        
        
    except (ProtocolError, ConnectionError, socket.error) as err:
        logging.debug("{}: {}".format(connection.to_addr, err))
    finally:
        connection.close()
    
        
    
    return 0

def getseeds(storageadapter):
    conf = ConfigParser()
    conf.read('seeds.conf')
    hosts = conf.get('seeds', 'hosts').strip().split("\n")

    for seeder in hosts:
        nodes = []
        try:
            nodes = socket.getaddrinfo(seeder, None)
        except socket.gaierror as err:
            logging.warning("{}".format(err))
            continue
        
        for node in nodes:
            address = node[-1][0]
            logging.debug("{}: {}".format(seeder, address))
            
            storageadapter.insertNode(address, 9333);
    
    

def redefinelogging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)



if __name__ == '__main__':
    sys.exit(main(sys.argv))
    
    
    