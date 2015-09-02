#!/usr/bin/env python
# encode: utf-8

from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

fol = Follower(instr, freq=30, mul=4000, add=40)
fol.ctrl()
f = Biquad(instr, freq=fol, q=5, type=2).out()
f.ctrl()

# set global Volume to -20 db to protect your ears and equipment
s.setAmp(0.1)
# start GUI
s.gui(locals())