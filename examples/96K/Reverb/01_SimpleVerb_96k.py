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
b1 = Allpass(instr, delay=[.0204,.02011], feedback=0.35)
b2 = Allpass(b1, delay=[.06653,.06641], feedback=0.41)
b3 = Allpass(b2, delay=[.035007,.03504], feedback=0.5)
b4 = Allpass(b3, delay=[.023021 ,.022987], feedback=0.65)

c1 = Tone(b1, 5000, mul=0.2).out()
c2 = Tone(b2, 3000, mul=0.2).out()
c3 = Tone(b3, 1500, mul=0.2).out()
c4 = Tone(b4, 500, mul=0.2).out()

# GUI
s.gui(locals())