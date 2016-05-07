#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
static equalizer mono to stereo spread filter effect



Knüppelstereofonie

hohe CPU-Auslastung
"""


# import necessary  libraries
from pyo import *


# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=96000, buffersize=128, audio='portaudio', ichnls=1, nchnls=2)
s.setInputDevice(9)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)

# Input
instr = Input(chnl=0)


# Processing
eq_left = EQ(instr, freq=[31.5,63,125,250,500,1000,2000,4000,8000,16000], q=1, boost=[12,-12,12,-12,12,-12,12,-12,12,-12], type=0, mul=.5)
eq_left.ctrl(title='EQ_Left')
pan_left = Pan(eq_left, outs=2, pan=0, mul=.3).out()
pan_left.ctrl(title='Pan_Left')

eq_right = EQ(instr, freq=[31.5,63,125,250,500,1000,2000,4000,8000,16000], q=1, boost=[-12,12,-12,12,-12,12,-12,12,-12,12], type=0, mul=.5)
eq_right.ctrl(title='EQ_Right')
pan_right = Pan(eq_right, outs=2, pan=1, mul=.3).out()
pan_right.ctrl(title='Pan_Right')



# GUI
s.gui(locals())