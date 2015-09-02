#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

lfo = Sine(freq=[.2,.25], mul=.1, add=.5)
lfo.ctrl()
#disto = Disto(instr, drive=0.5, slope=0.3, mul=0.6, add=0).out()
disto = Disto(instr, drive=lfo, slope=0.3, mul=0.3, add=0).out()
disto.ctrl()

# set global Volume to -20 db to protect your ears and equipment
s.setAmp(0.1)
# start GUI
s.gui(locals())