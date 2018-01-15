import threading
import time
import Queue

def run(num):
    # print 'number:%s' % num
    time.sleep(1)
    print 'task done', num, threading.current_thread()


def create_thread():
    t1 = threading.Thread(target=run,args=(1,))
    t2 = threading.Thread(target=run,args=(2,))

    t1.start()
    t2.start()

    print t1.getName()
    print t2.getName()


class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print 'number:%s' % self.num
        time.sleep(2)

def test_mythread():
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()


def test_join_setDaemon():
    start_time = time.time()
    t_objs = []
    for i in range(5):
        t = threading.Thread(target=run, args=('t-%s' % i, ))
        # t.setDaemon(True)
        t.start()
        t_objs.append(t)
    for t in t_objs:
        t.join()
    print 'all threads finished', threading.current_thread(), threading.active_count()
    print 'cost:', time.time() - start_time

def add_num():
    global num
    time.sleep(1)

    lock.acquire()
    num += 1
    lock.release()

num, num2 = 0, 0
lock = threading.RLock()

def test_lock():
    thread_list = []
    for i in range(100):
        t = threading.Thread(target=add_num)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    print 'final num:',num

def run1():
    print 'gotlockA', time.ctime()
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num

def run2():
    print 'gotlockB', time.ctime()
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2

def run3():
    lock.acquire()
    res = run1()
    print 'run1 and run2'
    res2 = run2()
    lock.release()
    print 'run3: ', res, res2, threading.currentThread()

def deadlock():
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()
    while threading.active_count() != 1:
        print 'while ', threading.active_count()
    else:
        print 'num1:%s,num2:%s' % (num,num2)


def run (n):
    semaphore.acquire()
    time.sleep(1)
    print 'run:%s\n' % n
    semaphore.release()

semaphore = threading.BoundedSemaphore()

def test_semapahore():
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()
    while threading.active_count() != 1:
        pass
    else:
        print 'all'

def do(event):
    print 'start'
    event.wait()
    print 'execute'

event_obj = threading.Event()

def test_event():
    for i in range(5):
        t = threading.Thread(target=do, args=(event_obj,))
        t.start()
    event_obj.clear()
    inpt = raw_input('input:')
    if inpt == '1':
        event_obj.set()

def test_queue():
    q = Queue.Queue()
    q.put('aaa')
    q.put('bbb')
    q.put('ccc')
    print q.get()

q = Queue.Queue(maxsize=10)
def producer():
    count = 1
    while True:
        q.put('product %s' % count)
        print 'has product', count
        count += 1
        time.sleep(0.1)

def consumer(n):
    while True:
        print '%s consume %s' % (n,q.get())
        time.sleep(0.5)

def test_product_consumer():
    p = threading.Thread(target=producer,)
    c1 = threading.Thread(target=consumer,args=('tom',))
    c2 = threading.Thread(target=consumer,args=('jack',))
    p.start()
    c1.start()
    c2.start()

#create_thread()
#test_mythread()
# test_join_setDaemon()
# test_lock()
# deadlock()
# test_semapahore()
# test_event()
# test_queue()
test_product_consumer()
