#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description

"""


# import necessary  libraries
from pyo import *


# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=96000, buffersize=128, audio='portaudio', nchnls=1)
#s = Server(sr=96000, buffersize=128, audio='portaudio', ichnls=1, nchnls=2)    #stereo out
s.setInputDevice(9)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(.1)


# Input
instr = Input(chnl=[0], mul=0.9)    # chnl=[0,1] for stereo input


# Processing
#--> Sets values for 8 delay lines
# delay line frequencies
freqs = [.254, .465, .657, .879, 1.23, 1.342, 1.654, 1.879]
# delay line center delays
cdelay = [.0087, .0102, .0111, .01254, .0134, .01501, .01707, .0178]
# delay line delay amplitudes
adelay = [.001, .0012, .0013, .0014, .0015, .0016, .002, .0023]
# modulation depth
depth = Sig(1)
#<--

#--> Add the delay lines to the source sound
lfo = Sine(freqs, mul=adelay*depth, add=cdelay)
lfo.ctrl()
delay = Delay(instr, lfo, feedback=.1, mul=.25).out()
delay.ctrl()
#<--


# GUI
s.gui(locals())