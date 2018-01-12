import sys
import socket
import threading,time

isNormar = True
other_usr = ''

def recieve_msg(username,s):
    global isNormar,other_usr
    print 'pls wait other user login..'
    s.send('login|%s' % username)
    while(isNormar):
        data = s.recv(1024)
        msg = data.split('|')
        if msg[0] == 'login':
            print u'%s user login in' % msg[1]
            other_usr = msg[1]
        else:
            print msg[0]
    print "thread fct exit"

def main():
    global isNormar,other_usr
    try:
        print "pls input your name:"
        username = raw_input()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("127.0.0.1",9999))
        t = threading.Thread(target=recieve_msg,args=(username,s))
        t.setDaemon(True)
        t.start()
    except:
        print 'connection exception'
        isNormar = False
    finally:
        pass
    while isNormar:
        msg = raw_input()
        if msg == 'exit':
            isNormar = False
        else:
            if other_usr != '':
                s.send('talk|%s|%s' % (other_usr,msg))
    print 'usr exit and cls connection'
    s.close()
    print t.is_alive()

def recv_msg(sock):
    try:
        while True:
            msg = sock.recv(1024)
            print "server:",msg
    except:
        print 'connection failed'

def client2():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1',9998))
        t = threading.Thread(target=recv_msg,args=(s,))
        t.setDaemon(True)
        t.start()
        while True:
            msg = raw_input()
            s.send(msg)
    except:
        print 'connection exception'


if __name__ == '__main__':
    client2()
