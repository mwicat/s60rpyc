'''
Created on Jan 9, 2011

@author: Administrator
'''

import rpyc
import time
from threading import Thread
from contextlib import contextmanager

HOST = '172.16.0.2'

def my_callback():
    print 'called'

def on_error(error):
    print 'error', error

def test_sensor():
    sensor = mthread(e52.root.getmodule, 'sensor')
    magnetic_north = mthread(sensor.MagneticNorthData)
    mthread(magnetic_north.set_callback, e52.modules.rpyc.async(my_callback))
    mthread(magnetic_north.start_listening)

def test_install():
    pyswinst = mthread(e52.root.getmodule, 'pyswinst')
    inst = mthread(pyswinst.SwInst)
    mthread(inst.install, u'e:\\instalki\\mm2.jar', e52.modules.rpyc.async(on_error))

e52 = rpyc.classic.connect(HOST)
bgsrv = rpyc.BgServingThread(e52)
mthread = e52.root.callmain

test_install()

time.sleep(500)
