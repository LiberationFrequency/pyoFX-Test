#!/usr/bin/env python
# encode: utf-8

from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

cho = Chorus(instr, depth=0.2, feedback=0.3, bal=0.5, mul=0.6).out()
cho.ctrl()

# set global Volume to -20 db to protect your ears and equipment
s.setAmp(0.1)
# start GUI
s.gui(locals())