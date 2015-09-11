#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description:
see rinmod_lib.py

"""

# import necessary libraries
from pyo import *
from ringmod_lib import RingMod


# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=44100, buffersize=64, audio='portaudio', nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)


# Input
instr = Input(chnl=0)


# Processing
lfo = Sine(75, phase=[0,.5], mul=.5, add=.5)
lfo.ctrl()
ring = RingMod(instr, freq=[800,1000], mul=lfo).out()
ring.ctrl()


# GUI
s.gui(locals())