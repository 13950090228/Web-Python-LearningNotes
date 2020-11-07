# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:30:47 2019

@author: 50671
"""
import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def task(arg,dic):
#     # q.put(arg) 
#     time.sleep(2)
#     dic[arg]=100


# if __name__ == '__main__':
#     # q=multiprocessing.Queue()
#     m=multiprocessing.Manager()
#     dic=m.dict()
#     p_list=[]
#     for i in range(10): 
#         # p=multiprocessing.Process(target=task,args=(i,q,))
#         p=multiprocessing.Process(target=task,args=(i,dic,))
#         p.start()
#         p_list.append(p)
        
#     while True:
#         count=0

#         for i in p_list:
#             if not p.is_alive():
#                 print(p.is_alive())
#                 count+=1
#         if count == len(p_list):
#             break
#     print(dic)



# lock=multiprocessing.RLock()
# def task(arg):
#     print('懒趴给你含')
#     # lock.acquire()
#     time.sleep(3)
#     print(arg)
#     # lock.release()

# if __name__ == '__main__':
#     p1=multiprocessing.Process(target=task,args=(1,))
#     p1.start()
    
#     p2=multiprocessing.Process(target=task,args=(2,))
#     p2.start()
    
# def task(arg):
#     print(arg)
#     time.sleep(5)
    
# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(5)
#     for i in range(10):
#         pool.submit(task,i)
import re
import requests
import uuid
from bs4 import BeautifulSoup
# start=time.time()
# r=requests.get(url='https://dig.chouti.com/',
#                headers={
#                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
#                    }
#                )

# r1=re.findall(r'<a class="link-title link-statistics" data-id=".*?" href=".*?" target=".*?">(.*?)</a>',r.text)
# for i in r1:
#     print(i)
# end=time.time()
# print(end-start)

r=requests.get(url='https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/7c5524bbd8d8e2d8b4fec3774915d2fb.jpg?w=632&h=340')
print(r.content)
file_name = str(uuid.uuid4()) + '.jpg'
with open(file_name, mode='wb') as f:
    f.write(r.content)






