'''
Created on Jan 9, 2011

@author: Administrator
'''

import weakref
from threading import currentThread
from concurrent.futures.thread import ThreadPoolExecutor, _worker

class DispatchExecutor(ThreadPoolExecutor):
    
    def __init__(self):
        ThreadPoolExecutor.__init__(1)
    
    def start_serving(self):
        t = currentThread()
        self._threads.add(t)
        self._thread_references.add(weakref.ref(t))
        _worker(weakref.ref(self), self._work_queue)