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
instr = Input(chnl=0)



# Processing
lfoup = Sine(freq=.25, mul=.48, add=.5)
#lfoup.ctrl()
lfodown = 0 - lfoup
c = Clip(instr, min=lfodown, max=lfoup, mul=1.4).out()
c.ctrl()


# GUI
s.gui(locals())