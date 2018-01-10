import socket
import commands

HOST,PORT = '',8000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()
while True:
    print "accept"
    data = conn.recv(1024)
    print "connected by: ", addr,"data: ",data
    if data == 'quit':break
    conn.sendall(str(data).upper())
print "close"
conn.close()
