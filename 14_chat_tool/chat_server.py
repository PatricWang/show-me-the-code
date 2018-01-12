import sys
import socket
import threading,time
import User

userlist = []

def hand_user_con(usr):
    try:
        isNormar = True
        while isNormar:
            data = usr.skt.recv(1024)
            time.sleep(1)
            msg = data.split('|')
            if msg[0] == 'login':
                print "user [%s] loginin" % msg[1]
                usr.username = msg[1]
                notice_other_usr(usr)
            if msg[0] == 'talk':
                print 'user[%s]to[%s]:%s' % (usr.username,msg[1],msg[2])
                send_msg(msg[1],msg[2])
            if msg[0] == 'exit':
                print 'user[%s] exit' % msg[0]
                isNormar = False
                usr.close()
                userlist.remove(usr)
    except:
        isNormar = False

def notice_other_usr(usr):
    if(len(userlist) > 1):
        print 'the two users'
        userlist[0].skt.send(("login|%s" % userlist[1].username))
        userlist[1].skt.send(("login|%s" % userlist[0].username))
    else:
        print 'one user'

def send_msg(username,msg):
    for usr in userlist:
        if(usr.username == username):
            usr.skt.send(msg)

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('',9999))
    s.listen(5)
    print u'waiting for connection..'
    while True:
        sock,addr = s.accept()
        user = User.User(sock)
        userlist.append(user)
        t = threading.Thread(target=hand_user_con,args=(user,))
        t.setDaemon(True)
        t.start()
    s.close()

def recv_msg(sock):
    try:
        while True:
            msg = sock.recv(1024)
            print "client:",msg
    except:
        print 'connection failed'

def server2():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('',9998))
    s.listen(1)
    cli_sock,addr = s.accept()
    print "receive connection, start talk"
    t = threading.Thread(target=recv_msg,args=(cli_sock,))
    t.setDaemon(True)
    t.start()
    while True:
        msg = raw_input()
        cli_sock.send(msg)


if __name__ == '__main__':
    server2()