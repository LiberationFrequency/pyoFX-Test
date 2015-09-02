#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

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
lfos = Sine(freqs, mul=adelay*depth, add=cdelay)
lfos.ctrl()
delay = Delay(instr, lfos, feedback=.1, mul=.25).out()
delay.ctrl()
#<--


# set master volume to -20 dB to protect your ears and equipment
s.setAmp(.1)
s.gui(locals())