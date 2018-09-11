'''#单线程
from time import ctime,sleep
class Demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.music()
        self.movie()
    def music(self):
        for i in range(3):
            print('i was listen to %s.%s'%(self.a,ctime()))
            sleep(1)
    def movie(self):
         for i in range(3):
            print('i was listen to %s!%s'%(self.b,ctime()))
            sleep(5)
if __name__=='__main__':
    d=Demo('白月光','金刚狼')
    print('all over %s' %ctime())
'''

'''
#多线程
import threading
from time import ctime,sleep
class Demo:
    def music(self,a):
        for i in range(3):
            print('i was listen to %s.%s'%(a,ctime()))
            sleep(1)
    def movie(self,b):
         for i in range(3):
            print('i was listen to %s!%s'%(b,ctime()))
            sleep(3)
if __name__=='__main__':
    threads=[]
    d=Demo()
    t1=threading.Thread(target=d.movie,args=(['魔兽世界']))
    threads.append(t1)
    t2=threading.Thread(target=d.movie,args=(['演员']))
    threads.append(t2)
    for i in range(len(threads)):
        threads[i].start()
print('all over %s' %ctime())
'''
'''
#1.打开一个问件，对问件循环写1000次，一条数据，统计时间
import threading
from time import ctime
import time
class Time:
    def write(self,aaa):
        f=open('d:\\a.txt','a')
        f.writelines(aaa)
if __name__=='__main__':
    a=time.time()
    for i in range(1000):
        threading.Thread(target=Time().write,args=(['just so so\n'])).start()
    b=time.time()
    print('花费时间总长为：%d'%(b-a))
'''


# 2.开启10个线程，每个线程分别写100次，每次一条数据，统计时间，做比较
import threading
from time import ctime,sleep
import time
class Time:
    def write(self,aaa):
        f=open('d:\\a.txt','a')
        for i in range(100):
            f.writelines(aaa)
            sleep(0.01)
        # f.close()

if __name__=='__main__':
    d=Time()
    list1=[]
    list2=['1111','2222','333','444','555','666','777','888','999','000']
    for i in list2:
        t=threading.Thread(target=d.write,args=([i+'\n']))
        list1.append(t)
    a=time.time()
    print(a)
    for i in list1:
        i.start()
    for i in list1:
        i.join()
    b=time.time()
    print(b)
    print('花费时间总长为：'+str(b-a))


'''
#别人的第2题
from time import ctime,sleep
import time
import threading

class MyThread():
    def singleThread(self,f):
        for i in range(1000):
            f.write("单线程："+str(i)+"\n")
            sleep(0.00001)

    def multithreading(self,a,b):
        for i in range(100):
            a.write("线程"+str(b)+"："+str(i)+"\n")
            sleep(0.00001)

def danxiancheng_run():
    f = open("C:\\Users\\Administrator\\Desktop\\aaa.txt","w")
    t1 = time.time()
    MyThread().singleThread(f)
    f.close()
    t2 = time.time()
    print(t2-t1)

def duoxiancheng_run():
    ff = open("C:\\Users\\Administrator\\Desktop\\bbb.txt","w")
    t11 = time.time()
    threads = []
    for i in range(100):
        t = threading.Thread(target=MyThread().multithreading,args=(ff,i))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    ff.close()
    t22 = time.time()
    print(t22-t11)

if __name__ == '__main__':
    danxiancheng_run()
    duoxiancheng_run()
'''