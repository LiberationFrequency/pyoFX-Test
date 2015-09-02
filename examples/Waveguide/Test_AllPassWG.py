#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()


instr = Input(chnl=0)

gt = Gate(instr, thresh=-45, risetime=0.005, falltime=0.01, lookahead=5, mul=0.08)
gt.ctrl()
rnd = Randi(min=0.5, max=1.0, freq=[.13,.22,.155,.171])
rnd.ctrl()
rnd2 = Randi(min=0.95, max=1.05, freq=[145,.2002,.1055,.071])
rnd2.ctrl()
fx = AllpassWG(gt, freq=rnd2*[74.87,75,75.07,75.21], feed=1, detune=rnd, mul=0.15).out()
fx.ctrl()

# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())