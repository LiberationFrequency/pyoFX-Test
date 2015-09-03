#!/usr/bin/env python
#! -*- codeing: utf-8 -*-
"""
Artifact free sweepable recursive delay.

SmoothDelay implements a delay line that does not produce clicks or pitch shifting 
when the delay time is changing.

"""

from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

lf = Sine(freq=0.1, mul=0.24, add=0.25)
sd = SmoothDelay(instr, delay=lf, feedback=0.25, crossfade=0.05, mul=0.7).out()
sd.ctrl()

# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())
