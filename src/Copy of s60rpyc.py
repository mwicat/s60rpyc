'''
Created on Jan 8, 2011

@author: Administrator
'''

from rpyc.core import SlaveService
from rpyc.core.service import ModuleNamespace
from rpyc.utils.server import ThreadedServer

from rpyc.utils.classic import DEFAULT_SERVER_PORT
from threading import Thread, Event

class Callgate:
    
    def __init__(self):
        self._req_evt = Event()
        self._complete_evt = Event()
    
    def request_call(self, cb, *args, **kwargs):
        def f():
            return cb(*args, **kwargs)
        self.cb = f
        self._req_evt.set()
        self._complete_evt.wait()
    
    def __call__(self):
        self.result = self.cb()
        self._req_evt.clear()
        self._complete_evt.set()
        
    def wait(self):
        self._req_evt.wait()
        
    def completed(self):
        self._complete_evt.set()

callgate = Callgate()

class MyService(SlaveService):
    
    def on_connect(self):
        SlaveService.on_connect(self)
        self._conn.cg_modules = ModuleNamespace(self._conn.root.getmodule)

    def exposed_getmodule(self, name):
        def f():
            return __import__(name, None, None, "*")
        callgate.request_call(f)
        return callgate.result

class Server(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.server = ThreadedServer(MyService, port = DEFAULT_SERVER_PORT)
       
    def run(self):
        self.server.start()

        
srv = Server()
srv.start()

for i in range(3):
    callgate.wait()
    callgate()
    
    