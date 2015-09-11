#!/usr/bin/env python
#! -*- codeing: utf-8 -*-
"""
Artifact free sweepable recursive delay.

SmoothDelay implements a delay line that does not produce clicks or pitch shifting 
when the delay time is changing.

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
lfo = Sine(freq=0.1, mul=0.24, add=0.25)
sd = SmoothDelay(instr, delay=lfo, feedback=0.25, crossfade=0.05, mul=0.7).out()
sd.ctrl()


# GUI
s.gui(locals())
