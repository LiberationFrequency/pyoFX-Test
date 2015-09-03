#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

compdry = Compress(instr, thresh=-12, ratio=2, risetime=.01, falltime=.2, knee=0.5, mul=1).out()
compdry.ctrl()
compwet = Compress(instr, thresh=-48, ratio=6, risetime=.25, falltime=.25, knee=0.5, mul=2).out(1)
compwet.ctrl()


# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())