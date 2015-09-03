#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *

s = Server(sr=44100, buffersize=128, audio='portaudio', nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

pva = PVAnal(instr, size=1024)
pva.ctrl()
pvt = PVTranspose(pva, transpo=1.0144)
pvt.ctrl()
pvs = PVSynth(pvt).out()
pvs.ctrl()
delay = Delay(instr, delay=1024./s.getSamplingRate(), feedback=0.1, mul=0.5).out(1)
delay.ctrl()


# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())