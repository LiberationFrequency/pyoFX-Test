#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
An envelope follower, which outputs the continuous mean amplitude of an input signal
and a band-pass filter, whose frequency followed the peaks.

"""


# import necessary libraries
from pyo import *


# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=96000, buffersize=256, audio='jack', nchnls=1)
#s.setInputDevice(9)
#s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)


# Input
instr = Input(chnl=0)


# Processing
fol = Follower(instr, freq=30, mul=4000, add=40)
fol.ctrl()
f = Biquad(instr, freq=fol, q=5, type=2).out()
f.ctrl()


# GUI
s.gui(locals())