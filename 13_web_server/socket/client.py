import socket

HOST,PORT = "127.0.0.1",8000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    usr_input = raw_input("input:")
    s.sendall(usr_input)
    reply = s.recv(1024)
    print "reply:",reply
s.close()