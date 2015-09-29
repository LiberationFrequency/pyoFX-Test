#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PitchShifter 

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
prelay = SDelay(instr, delay=0.002, mul=0.5)
prelay.ctrl()

harm_left = Harmonizer(prelay, transpo=0.05, feedback=0.01, winsize=0.025, mul=.9)
harm_left.ctrl(title='Transpose_Left')
pan_left = Pan(harm_left, outs=2, pan=0).out()
pan_left.ctrl(title='Pan_Left')

harm_right = Harmonizer(prelay, transpo=-0.05, feedback=0.01, winsize=0.025, mul=.9)
harm_right.ctrl(title='Transpose_Right')
pan_right = Pan(harm_right, outs=2, pan=1).out()
pan_right.ctrl(title='Pan_Right')



# GUI
s.gui(locals())