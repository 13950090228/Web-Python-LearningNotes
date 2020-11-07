# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:09:28 2019

@author: 50671
"""

import threading
import time
v= []
dic={}
#lock=threading.BoundedSemaphore(3)
#lock=threading.Lock()
#lock=threading.RLock()
lock=threading.Condition()
def a():
    print('执行函数！')
    input('啊啊啊')
    return True

def func(arg):
    print('线程进来了')
#    lock.acquire()
    lock.wait_for(a)
#    v.append(arg)
    print(arg)
    time.sleep(1)
#    m=v[-1]
#    
#    dic['arg']=arg
#    dic['m']=m
    
#    print(dic)
#    lock.release()

for i in range(10):
    t=threading.Thread(target=func,args=(i,))
    t.start()


    