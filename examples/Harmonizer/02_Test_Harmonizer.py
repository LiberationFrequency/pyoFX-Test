#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *

s = Server(sr=44100, buffersize=128, audio='portaudio', nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

# 0-7
env = WinTable(3)

wsize = .1
trans = -7

ratio = pow(2., trans/12.)
rate = -(ratio-1) / wsize

ind = Phasor(freq=rate, phase=[0,0.5])
ind.ctrl()
win = Pointer(table=env, index=ind, mul=.7)
snd = Delay(instr, delay=ind*wsize, mul=win).mix(1).out()
snd.ctrl()

# set master volume to -20 db to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())