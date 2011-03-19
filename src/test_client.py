'''
Created on Jan 9, 2011

@author: Administrator
'''

from rpyc import classic as rpyc
import time

HOST = '172.16.0.2'

def my_callback():
    print 'called'
    #azimuth = str(magnetic_north.azimuth)
    #print azimuth


e52 = rpyc.connect(HOST)
e52r = e52.root

sensor = e52r.callmain(e52r.getmodule, 'sensor')
magnetic_north = e52r.callmain(sensor.MagneticNorthData)
e52r.callmain(magnetic_north.set_callback, 
              data_callback=e52r.callgate(my_callback))
e52r.callmain(magnetic_north.start_listening)

time.sleep(20)