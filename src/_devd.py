'''
Created on Jan 9, 2011

@author: Administrator
'''


from pysrc import pydevd

pydevd.settrace('172.16.0.1', stdoutToServer=True, stderrToServer=True)
import rpyc
print 'marek'