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
p1 = Pan(eq1, outs=2, pan=1).out()
p1.ctrl()

eq2 = EQ(instr, freq=[63,125,250,500,1000,2000,4000,8000,16000], q=1, boost=[-12,12,-12,12,-12,12,-12,12,-12], type=0)
eq2.ctrl()
p2 = Pan(eq2, outs=2, pan=0).out()
p2.ctrl()

#comp = Compress(instr, thresh=-12, ratio=1.5, risetime=.1, falltime=.2, knee=0.5).out()
#comp.ctrl()


#mm = Mixer(outs=3, chnls=2, time=.025)

#mm.addInput(0, a)
#mm.addInput(1, b)
#mm.setAmp(0,1,.5)
#mm.setAmp(1,2,.5)
#mm.setAmp(1,1,.5)



# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())