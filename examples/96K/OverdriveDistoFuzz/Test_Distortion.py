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
s.setInputDevice(9)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)


# Input
instr = Input(chnl=0)


# Processing
#lfo = Sine(freq=[.2,.25], mul=.1, add=.5)
#lfo.ctrl()
disto = Disto(instr, drive=0.5, slope=0.3, mul=0.6, add=0).out()
#disto = Disto(instr, drive=lfo, slope=0.3, mul=0.3, add=0).out()
disto.ctrl()


# GUI
s.gui(locals())