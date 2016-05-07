#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description

"""


# import necessary libraries
from pyo import *



# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=96000, buffersize=128, audio='portaudio', nchnls=1)
#s = Server(sr=96000, buffersize=128, audio='portaudio', ichnls=1, nchnls=2)    #stereo out
s.setInputDevice(9)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)



# Input
instr = Input(chnl=[0], mul=0.9)    # chnl=[0,1] for stereo input



# Processing
#fol = Follower(instr, freq=63, mul=4000, add=40)
#fol.ctrl()
#f = Biquad(instr, freq=fol, q=1.5, type=2, mul=.9)
#f.ctrl()
#pva = PVAnal(f, size=1024)
pva = PVAnal(instr, size=1024)
pvt = PVTranspose(pva, transpo=[0.5,2])
pvt.ctrl()
pvm = PVAmpMod(pva, basefreq=2, spread=0.25)
t = SawTable(order=12).normalize()
pvs = PVSynth([pvt,pva], mul=.9)
pvs.ctrl()
delay = Delay(instr, delay=1024./s.getSamplingRate(), feedback=0.1, mul=0.9)
delay.ctrl()
compdel = Compress(delay, thresh=-24, ratio=2, risetime=.01, falltime=.2, knee=0.5, mul=.9).out()
compdel.ctrl()
comppvs = Compress(pvs, thresh=-24, ratio=2, risetime=.01, falltime=.2, knee=0.5, mul=.9).out()
comppvs.ctrl()

# GUI
s.gui(locals())