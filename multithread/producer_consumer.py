import random, threading, time
import Queue

class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue


    def run(self):
        for i in range(10):
            num = random.randint(1,99)
            print '%s:%s produced %d ' % (time.ctime(), self.getName(), num)
            self.data.put(num)
            time.sleep(1)
            print '%s:%s completed ' % (time.ctime(), self.getName())


class Consumer_even(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        while True:
            try:
                val_even = self.data.get(1,5)
                if val_even % 2 == 0:
                    print '%s:%s consumed %d ' % (time.ctime(), self.getName(), val_even)
                    time.sleep(2)
                else:
                    self.data.put(val_even)
                    time.sleep(2)
            except:break


class Consumer_odd(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        while True:
            try:
                val_odd = self.data.get(1,5)
                if val_odd % 2 != 0:
                    print '%s:%s consumed %d ' % (time.ctime(), self.getName(), val_odd)
                    time.sleep(2)
                else:
                    self.data.put(val_odd)
                    time.sleep(2)
            except:break

def main():
    queue = Queue()
    producer = Producer('producer', queue)
    consumer_even = Consumer_even('consumer_even', queue)
    consumer_odd = Consumer_odd('consumer_odd', queue)
    producer.start()
    


