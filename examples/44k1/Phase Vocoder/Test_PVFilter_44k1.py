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
t = ExpTable([(0,1),(61,1),(71,0),(131,1),(171,0),(511,0)], size=512)
t.graph()
pva = PVAnal(instr, size=1024)
pvf = PVFilter(pva, t)
pvf.ctrl()
pvs = PVSynth(pvf, mul=.9).out()
pvs.ctrl()


# GUI
s.gui(locals())