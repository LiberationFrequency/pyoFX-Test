#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description

"""

# import necessary libraries
from pyo import *


# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=96000, buffersize=256, audio='jack', nchnls=1)
#s = Server(sr=96000, buffersize=128, audio='portaudio', ichnls=1, nchnls=2)    #stereo out
#s.setInputDevice(9)
#s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)


# Input
instr = Input(chnl=[0], mul=0.9)    # chnl=[0,1] for stereo input


# Processing
pva = PVAnal(instr, size=1024)
#pva.ctrl()
pvt = PVTranspose(pva, transpo=1.0144)
pvt.ctrl()
pvs = PVSynth(pvt).out()
pvs.ctrl()
delay = Delay(instr, delay=1024./s.getSamplingRate(), feedback=0.1, mul=0.5).out(1)
delay.ctrl()


# GUI
s.gui(locals())