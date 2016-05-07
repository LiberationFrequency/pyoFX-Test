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
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)


# Input
instr = Input(chnl=0)


# Processing
compdry = Compress(instr, thresh=-24, ratio=2, risetime=.01, falltime=.2, knee=0.5).out()
compdry.ctrl(title='Compressor dry')
compwet = Compress(instr, thresh=-48, ratio=9, risetime=.25, falltime=.25, knee=0.5, mul=2).out()
compwet.ctrl(title='Compressor wet')


# GUI
s.gui(locals())