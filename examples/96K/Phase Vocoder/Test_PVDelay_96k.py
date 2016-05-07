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
#s = Server(sr=96000, buffersize=128, audio='portaudio', ichnls=1, nchnls=2)    #stereo out
s.setInputDevice(9)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)


# Input
instr = Input(chnl=[0], mul=0.9)    # chnl=[0,1] for stereo input


# Processing

SIZE = 2048
SIZE2 = SIZE / 2
OLAPS = 4
MAXDEL = 2.0 # two seconds delay memories
FRAMES = int(MAXDEL * s.getSamplingRate() / (SIZE / OLAPS))
# Edit tables with the graph() method. yrange=(0, FRAMES) for delays table
dt = DataTable(size=SIZE2, init=[i / float(SIZE2) * FRAMES for i in range(SIZE2)])
dt.graph()
ft = DataTable(size=SIZE2, init=[0.5]*SIZE2)
ft.graph()
pva = PVAnal(instr, size=SIZE, overlaps=OLAPS)
pvd = PVDelay(pva, dt, ft, maxdelay=MAXDEL)
pvs = PVSynth(pvd, mul=.9).out()
pvs.ctrl()



# GUI
s.gui(locals())