import threadpool,threading
import time
from multiprocessing import Process, Pool
# calculate sum from 1 to 10**10


def no_multithread():
    global ret
    for i in xrange(10**8+1):
        ret += i

def calc_sum(start, end):
    global ret,lock
    lock.acquire()
    for i in xrange(start, end+1):
        ret += i
    lock.release()



ret = 0
lock = threading.Lock()
sub_sum = [0,0,0,0,0,0,0,0,0,0]

def with_multithread():
    thread_list = []
    for i in range(10):
        t = threading.Thread(target=calc_sum, args=(10**7*i+1, 10**7*(i+1)))
        t.start()
        thread_list.append(t)
    [i.join() for i in thread_list]

def calc_sub_sum(idx):
    start_time = time.time()
    print 'cur thread start:',threading.currentThread()
    global sub_sum
    for i in xrange(10**7*idx+1, 10**7*(idx+1)+1):
        sub_sum[idx] += i
    print 'time elapsed:', time.time() - start_time


def with_multithread_subsum():
    thread_list = []
    global ret, sub_sum
    for i in range(10):
        t = threading.Thread(target=calc_sub_sum, args=(i, ))
        t.start()
        thread_list.append(t)
    [i.join() for i in thread_list]
    ret = sum(sub_sum)

def sum_pool(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

def onresult(sum):
    global ret
    ret += sum

def with_pool():
    arglist = []
    for i in range(10):
        arglist.append(([i*10**7+1,10**7*(i+1)],None))
    pool = threadpool.ThreadPool(10)
    reqs = threadpool.makeRequests(sum_pool, args_list=arglist, callback=onresult)
    [pool.putRequest(req) for req in reqs]
    pool.wait()

def process_calc_sum(start, end):
    result = 0
    for i in xrange(start, end+1):
        result += i
    return result

def with_process():
    arglist = []
    for i in range(10):
        arglist.append(([i * 10 ** 7 + 1, 10 ** 7 * (i + 1)], None))
    pool = Pool(10)
    for i in range(10):
        pool.apply_async(func=process_calc_sum, args=(i * 10 ** 7 + 1, 10 ** 7 * (i + 1)), callback=onresult)
    pool.close()
    pool.join()


def main():
    time_start = time.time()
    # no_multithread()
    # with_multithread()
    # with_multithread_subsum()
    # with_pool()
    with_process()
    # for i in range(10):
    #     calc_sub_sum(i)
    # ret = sum(sub_sum)
    print ret
    print "main time elapse:", time.time() - time_start

if __name__ == '__main__':
    main()