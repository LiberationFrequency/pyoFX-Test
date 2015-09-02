#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *
import RingMod

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

lfo = Sine(75, phase=[0,.5], mul=.5, add=.5)
lfo.ctrl()
ring = RingMod.RingMod(instr, freq=[800,1000], mul=lfo).out()
ring.ctrl()

# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())