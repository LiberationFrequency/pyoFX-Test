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
#f_len = sndinfo(instr)[1]
#index = Phasor(freq=1.0/f_len*0.25, phase=0.9)
index = Phasor(freq=[1, 1.5], phase=.9)
index.ctrl()
pva = PVAnal(instr, size=1024, overlaps=8)
#pvb = PVBuffer(pva, index, pitch=1.25, length=f_len)
pvb = PVBuffer(pva, index, pitch=1.044, length=1.25)
pvb.ctrl()
pvs = PVSynth(pvb, mul=.9).out()


# GUI
s.gui(locals())