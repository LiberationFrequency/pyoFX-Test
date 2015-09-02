#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *
import Flanger

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

lfo = Sine(75, mul=0.25, add=0.5)
lfo.ctrl()
flg = Flanger.Flanger(instr, depth=0.8, lfofreq=0.5, feedback=lfo).out()
flg.ctrl()

# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())