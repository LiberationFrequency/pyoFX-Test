#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description:
see ringmod_lib.py

"""

# import necessary libraries
from pyo import *
from ringmod_lib import RingMod


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
lfo = Sine(75, phase=[0,.5], mul=.5, add=.5)
lfo.ctrl()
ring = RingMod(instr, freq=[800,1000], mul=lfo).out()
ring.ctrl()


# GUI
s.gui(locals())