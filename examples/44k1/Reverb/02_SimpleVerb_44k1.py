#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description

"""


# import necessary libraries
from pyo import *



# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=44100, buffersize=64, audio='portaudio', nchnls=1)
#s = Server(sr=44100, buffersize=64, audio='portaudio', ichnls=1, nchnls=2)    #stereo out
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)



# Input
instr = Input(chnl=[0], mul=0.9)    # chnl=[0,1] for stereo input



# Processing
comb1 = Delay(instr, delay=[0.0297,0.0277], feedback=0.65)
comb2 = Delay(instr, delay=[0.0371,0.0393], feedback=0.51)
comb3 = Delay(instr, delay=[0.0411,0.0409], feedback=0.5)
comb4 = Delay(instr, delay=[0.0137,0.0155], feedback=0.73)

combsum = instr + comb1 + comb2 + comb3 + comb4

all1 = Allpass(combsum, delay=[.005,.00507], feedback=0.75)
all2 = Allpass(all1, delay=[.0117,.0123], feedback=0.61)
lowp = Tone(all2, freq=3500, mul=.2).out()

# GUI
s.gui(locals())