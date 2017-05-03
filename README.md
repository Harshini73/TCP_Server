# TCP_Server
# About
A multithreaded TCP server implementation in python3. 
# Starting the server
python3 tcpserver.py -p PORTNUM
# Features
When the server is started, it listens for connections from the client. When a client is connected, the relevant information is written to the tcpserver.log file.
The server receives data from the client until CLRF. In the case of CLRF, it sends the number of bytes received to the client and the same information is written to the log file.The server then terminates the connection with the client. 
