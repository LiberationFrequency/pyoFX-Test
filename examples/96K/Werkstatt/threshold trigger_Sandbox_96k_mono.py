#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description

"""


# import necessary libraries
from pyo import *



# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=96000, buffersize=128, audio='portaudio', nchnls=1)
s.setInputDevice(9)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)



# Input
instr = Input(chnl=[0], mul=0.9) # chnl=[0,1] for stereo input



# Processing
n = 0

b = Thresh(instr, threshold=0.4, dir=0)
ti = Timer(b, b)

def printer():
        global n
        n = n + 1

        print 'trigger', n , 'time', str(ti.get(all)).strip('[]')

tf = TrigFunc(b, printer)

t = LinTable([(0,0), (50,1), (250,.3), (8191,0)])
env = TrigEnv(b, table=t, dur=.5, mul=.3)
sine = Sine(freq=400, mul=env).out()

# GUI
s.gui(locals())