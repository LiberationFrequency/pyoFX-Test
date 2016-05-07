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
instr = Input(chnl=0).out()


# Processing
harm1 = Harmonizer(instr, transpo=0.3, feedback=0.25, winsize=0.15, mul=0.6).out()
harm1.ctrl()
harm2 = Harmonizer(instr, transpo=-0.3, feedback=0.25, winsize=0.15, mul=0.6).out()
harm2.ctrl()
comp = Compress(instr, thresh=-24, ratio=2, risetime=.01, falltime=.2, knee=0.5).out()
comp.ctrl()


# GUI
s.gui(locals())