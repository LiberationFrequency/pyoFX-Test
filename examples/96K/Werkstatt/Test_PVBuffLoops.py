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
instr = Input(chnl=[0], mul=0.9)    # chnl=[0,1] for stereo input


# Processing
pva = PVAnal(instr, size=1024, overlaps=8)
#pvb = PVBufLoops(pva, low=0.9, high=1.1, mode=3, length=f_len)
pvb = PVBufLoops(pva, low=0.9, high=1.1, mode=3, length=2)
pvb.ctrl()
pvs = PVSynth(pvb, mul=.9).out()

# GUI
s.gui(locals())