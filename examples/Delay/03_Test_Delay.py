#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

lfo = Sine(freq=4, phase=.5, mul=.5, add=.3)
lfo.ctrl()
delay = Delay(instr, delay=.3, feedback=lfo, maxdelay=5).out()
delay.ctrl()

# set master volume to -20 dB to protect your ears and equipment
s.setAmp(.1)
s.gui(locals())