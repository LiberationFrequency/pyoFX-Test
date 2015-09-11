#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Low Bass 

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
eq_Bass = EQ(instr, freq=[10,20,2000,4000,8000,16000], q=1, boost=[-40,-3,-3,-20,-40,-60], type=0)
eq_Bass.ctrl()

det_wg = AllpassWG(eq_Bass, freq=38, feed=.15, detune=0.5, mul=1)
det_wg.ctrl()

lpf = Biquad(det_wg, freq=32, q=5, type=2)
lpf.ctrl()

compdry = Compress(lpf, thresh=-24, ratio=1.5, risetime=.001, falltime=.1, knee=0.5, mul=.9).out()
compdry.ctrl()
compwet = Compress(compdry, thresh=-48, ratio=9, risetime=.03, falltime=.15, knee=0.5, mul=0.9).out()
compwet.ctrl()


# GUI
s.gui(locals())