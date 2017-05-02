import socket
import threading
import argparse
import logging
import time

''' Server class '''
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
       ''' Function to listen for clients'''
        self.sock.listen(1000)
        while True:
            client, address = self.sock.accept()
            localtime=time.asctime( time.localtime(time.time()) )
            logging.basicConfig(filename='tcp_server.log',level=logging.INFO)
            log=address[0]+" got connected on "+localtime
            logging.info(log)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address)
        ''' Function to receive data from the client.
            The connection with the client is closed if the server receievs either a carriage return or a line feed '''
        count=0
        while True:
                data = client.recv(1024)
                response=str(data)
                count=count+len(data)
                if '\n'or '\r' in response: 
                    logging.basicConfig(filename='tcp_server.log',level=logging.INFO)
                    received=str(count)+" bytes received from "+address[0]
                    logging.info(received)
                    client.send(str(count))
                    client.close()
                    break
                       

if __name__ == "__main__":
   ''' Taking port number from the command line.
       Run the code as name.py -p PortNumber '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type=int)
    args=parser.parse_args()
    port_num = args.p
    ThreadedServer('',port_num).listen()
