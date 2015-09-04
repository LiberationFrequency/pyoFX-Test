#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
static equalizer stereo enhancer

Knüppelstereofonie

"""


from pyo import *

s = Server(sr=44100, buffersize=64, audio='portaudio', nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

eq1 = EQ(instr, freq=[63,125,250,500,1000,2000,4000,8000,16000], q=1, boost=[12,-12,12,-12,12,-12,12,-12,12], type=0)
eq1.ctrl()
eq2 = EQ(instr, freq=[63,125,250,500,1000,2000,4000,8000,16000], q=1, boost=[-12,12,-12,12,-12,12,-12,12,-12], type=0)
eq2.ctrl()
p1 = Pan(eq1, outs=2, pan=1)
p1.ctrl()
p2 = Pan(eq2, outs=2, pan=0)
p2.ctrl()

psum = p1 + p2

comp = Compress(psum, thresh=-18, ratio=3, risetime=.1, falltime=.2, knee=0.5).out()
comp.ctrl()

#prelay1 = SDelay(instr, delay=0.002, mul=0.5)
#prelay.ctrl()

#harm1 = Harmonizer(prelay, transpo=0.07, feedback=0.01, winsize=0.1, mul=.6)
#harm1.ctrl()
#p1 = Pan(harm1, outs=2, pan=1)

#harm2 = Harmonizer(prelay, transpo=-0.07, feedback=0.01, winsize=0.1, mul=.6)
#harm2.ctrl()
#p2 = Pan(harm2, outs=2, pan=0)



#mm = Mixer(outs=3, chnls=2, time=.025)

#mm.addInput(0, a)
#mm.addInput(1, b)
#mm.setAmp(0,1,.5)
#mm.setAmp(1,2,.5)
#mm.setAmp(1,1,.5)



# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())