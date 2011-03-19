'''
Created on Jan 14, 2011

@author: Administrator
'''

import os
import rpyc
from rpycutil import rcopy
from s60util import install

HOST = '172.16.0.2'
FNS = 'amx.jad', 'amx.jar'
APP = 'Aportuj'
DIR = r'E:\installs'

conn = rpyc.classic.connect(HOST)
for fn in FNS:
    rcopy(fn, DIR, dst=conn)
install(conn, os.path.join(DIR, FNS[0]))
conn.modules.midlet.run(APP)
