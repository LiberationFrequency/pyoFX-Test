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
det_wg = AllpassWG(instr, freq=82.4, feed=.15, detune=0.5, mul=.25).out()
det_wg.ctrl()
#lowpass filter
#lfo = Sine(freq=[.2, .25], mul=1000, add=1500)
lpf = Biquad(det_wg, freq=400, q=5, type=2)
lpf.ctrl()

compdry = Compress(lpf, thresh=-24, ratio=1.5, risetime=.2, falltime=.2, knee=0.5, mul=.9).out()
compdry.ctrl()
compwet = Compress(instr, thresh=-48, ratio=9, risetime=.5, falltime=.5, knee=0.5, mul=0.9).out()
compwet.ctrl()


# GUI
s.gui(locals())