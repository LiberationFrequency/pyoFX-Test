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
# set master volume to -20 db to protect your ears and equipment
s.setAmp(0.1)


# Input
instr = Input(chnl=[0], mul=0.9)    # chnl=[0,1] for stereo input

# Processing

# type = 0-7
##
##    Rectangular (no window)
##    Hamming
##    Hanning (default)
##    Bartlett (triangular)
##    Blackman 3-term
##    Blackman-Harris 4-term
##    Blackman-Harris 7-term
##    Tuckey (alpha = 0.66)
##    Sine (half-sine window)
env = WinTable(type=2, size=8192)


wsize = .1
#trans = -7

#ratio = pow(2., trans/12.)
#rate = -(ratio-1) / wsize

#ind = Phasor(freq=rate, phase=[0,0.5])
ind = Phasor(freq=30, phase=[0,0.5], mul=.97)
ind.ctrl()
win = Pointer(table=env, index=ind, mul=.7)
snd = Delay(instr, delay=ind*wsize, mul=win).out()
snd.ctrl()


# GUI
s.gui(locals())