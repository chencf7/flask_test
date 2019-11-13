# coding=utf-8
from threading import Thread
import time

exitFlag = 0


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


class MyThread(Thread):
    def __init__(self, thread_id, name, counter):
        # 继承线程类的属性
        # Thread.__init__(self)
        super(MyThread, self).__init__()
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    # 继承实现了thread的run方法，thread.start方法执行时，即调用run
    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def my_counter():
    i = 0
    for _ in range(100000000):
        i += 1
    return True


# 线程顺序执行
def sync_threading():
    print('threading start')
    thread_arr = {}
    st = time.time()
    # for tid in range(2):
    #     t = Thread(target=my_counter)
    #     t.start()
    #     t.join()
    t1 = Thread(target=my_counter)
    t2 = Thread(target=my_counter)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # t1 = Thread(target=my_counter)
    # t1.start()
    # t1.join()
    # t2 = Thread(target=my_counter)
    # t2.start()
    # t2.join()
    et = time.time()
    print('Total time: {}\'s'.format(et - st))


def test1(t_name):
    count = 1
    while True:
        count += 1
        print(t_name+': ', count)


def run():
    # test1()
    t1 = Thread(target=test1, args=('线程1',))
    t2 = Thread(target=test1, args=('线程2',))
    t1.start()
    t2.start()

    # sync_threading()
    return
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()
    # Thread 提供了让一个线程等待另一个线程完成的 join() 方法
    # 当在某个程序执行流中调用其他线程的 join() 方法时，调用线程将被阻塞，直到被 join() 方法加入的 join 线程执行完成
    thread1.join()
    # thread2.join()
    print("退出主线程")


