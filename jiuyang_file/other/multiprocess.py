from multiprocessing import Pool
import os


class AA(object):
    def __init__(self):
        print('init')
        self.ab = '22'
        print(id(self.ab))

    def task(self, n):
        print(id(self.ab))
        self.ab += n

        print("进程%s, 收到%s, +n=%s" % (os.getpid(), n, id(self.ab)))


if __name__ == '__main__':
    aa = AA()
    p = Pool(4)

    for i in range(5):
        t = p.apply_async(func=aa.task, args=(str(i),))

    p.close()
    p.join()
    print("done ！  主进程！aa.ab=%s" % aa.ab)
    print("主进程ID  %s " % os.getpid())
