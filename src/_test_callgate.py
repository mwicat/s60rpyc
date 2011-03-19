'''
Created on Jan 9, 2011

@author: Administrator
'''

from Queue import Queue
import e32
import appuifw

class Callgate:
    
    def __init__(self, request_queue):
        self._request_queue = request_queue
    
    def request_call(self, cb, *args, **kwargs):
        def f():
            return cb(*args, **kwargs)
        res_queue = Queue()
        req = f, res_queue
        self._request_queue.put_nowait(req)
        res = res_queue.get()
        return res
    
    def stop(self):
        self._request_queue.put_nowait(1)

def exit_key_handler():
    cg

req_queue = Queue()
callgate = Callgate(req_queue)

appuifw.app.exit_key_handler = exit_key_handler

while True:
    req = req_queue.get_nowait()
    e32.ao_sleep(1)
    if req is None:
        continue
    if req == 1:
        break
    f, res_queue = req
    res = f()
    res_queue.put_nowait(res)