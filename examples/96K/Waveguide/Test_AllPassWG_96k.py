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
gt = Gate(instr, thresh=-45, risetime=0.005, falltime=0.01, lookahead=5, mul=0.08)
gt.ctrl()
rnd = Randi(min=0.5, max=1.0, freq=[.13,.22,.155,.171])
rnd.ctrl()
rnd2 = Randi(min=0.95, max=1.05, freq=[145,.2002,.1055,.071])
rnd2.ctrl()
fx = AllpassWG(gt, freq=rnd2*[74.87,75,75.07,75.21], feed=1, detune=rnd, mul=0.15).out()
fx.ctrl()


# GUI
s.gui(locals())