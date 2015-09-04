#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
monoEnhancer - PitchShifter 

"""

from pyo import *
import random


from pyo import *

s = Server(sr=44100, buffersize=64, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()


instr = Input(chnl=0)

#ind = LinTable([(0,.3), (20,.85), (300,.7), (1000,.5), (8191,.3)])
#m = Metro(4).play()
#tr = TrigEnv(m, table=ind, dur=4)
#f = SumOsc(freq=[0,40], ratio=[.2498,.2503], index=tr, mul=.2)

prelay = SDelay(instr, delay=0.002, mul=0.5)
prelay.ctrl()

harm1 = Harmonizer(prelay, transpo=0.05, feedback=0.01, winsize=0.1, mul=.6)
harm1.ctrl()
p1 = Pan(harm1, outs=2, pan=1)

harm2 = Harmonizer(prelay, transpo=-0.05, feedback=0.01, winsize=0.1, mul=.6)
harm2.ctrl()
p2 = Pan(harm2, outs=2, pan=0)

psum = p1 + p2

compdry = Compress(instr, thresh=-6, ratio=2, risetime=.12, falltime=.2, knee=0.5, mul=1.8).out()
compdry.ctrl()
compwet = Compress(psum, thresh=-32, ratio=6, risetime=.01, falltime=.2, knee=0.5, mul=2).out()
compwet.ctrl()



#mm = Mixer(outs=3, chnls=2, time=.025)

#mm.addInput(0, a)
#mm.addInput(1, b)
#mm.setAmp(0,1,.5)
#mm.setAmp(1,2,.5)
#mm.setAmp(1,1,.5)



# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())