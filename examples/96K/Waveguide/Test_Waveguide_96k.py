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
gt = Gate(instr, thresh=-80, risetime=0.005, falltime=0.01, lookahead=5, mul=0.08)
gt.ctrl()
w = Waveguide(gt, freq=[60,120.17,180.31,240.53], dur=2.5, minfreq=20, mul=0.4).out()
w.ctrl()


# GUI
s.gui(locals())