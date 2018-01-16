from multiprocessing import Process, Pipe, Manager, Lock, Pool


def foo(lock, i):
    # lock.acquire()
    print 'foghjhgjghjhgjgjgho', i
    # lock.release()


def test_process():
    lock = Lock()
    for i in range(5):
        p = Process(target=foo, args=(lock, i))
        p.start()


def foo_pipe(conn):
    conn.send([42, None, 'foo'])
    print 'child:', conn.recv()
    conn.close()

4999999950000000
49999995000000
4942148467503573
4942228849065910
4999999950000000
5000000050000000
50000005000000
50000005000000
5000000050000000
5000000050000000
5000000050000000
def test_pipe():
    parent_conn, child_conn = Pipe()
    p = Process(target=foo_pipe, args=(child_conn,))
    p.start()
    print 'parent:', parent_conn.recv()
    parent_conn.send('parent send')
    p.join()


def foo_manager(d, l):
    d[1] = '1'
    d['2'] = 2
    l.append(1)
    print 'foo_m:', l


def test_manager():
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=foo_manager, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print d
        print l


def foo_pool(i):
    import time, os
    time.sleep(2)
    print 'process', os.getpid()
    return i + 100


def bar(arg):
    import os
    print '-->', arg, os.getpid()


def test_pool():
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func=foo_pool, args=(i, ),callback=bar)
        # pool.apply(func=foo_pool, args=(i, ))
    print 'end'
    pool.close()
    pool.join()


if __name__ == '__main__':
    test_process()