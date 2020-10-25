#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from multiprocessing import Pool
import time
import os

def my_func(work) :
    print('Working(={0}) Process ID = {1}' .format(work, os.getpid()))
    time.sleep(1)
    return work

if __name__ == '__main__' :
    p = Pool(3)
    startTime = int(time.time())
    print(p.map(my_func, range(0, 30)))
    endTime = int(time.time())
    print('Working Time = about {0}s', (endTime - startTime))

