#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description

"""

from pyo import *

s = Server(sr=44100, buffersize=64, audio='portaudio', nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)


eqbass = EQ(instr, freq=[10,20,30,63,125,250,500,1000,2000,4000,8000,16000], q=0.15, boost=[-60,-40,-20,0.5,1,0,0,-0.5,-1,-20,-40,-60], type=2)
eqbass.ctrl()

cho = Chorus(eqbass, depth=0.4, feedback=0.35, bal=0.6, mul=0.8)
cho.ctrl()

compdry = Compress(eqbass, thresh=-15, ratio=3, risetime=.1, falltime=.25, knee=0.5, mul=1).out()
compdry.ctrl()
compchodry = Compress(cho, thresh=-12, ratio=2, risetime=.1, falltime=.25, knee=0.5, mul=1).out()
compchodry.ctrl()
compchowet = Compress(cho, thresh=-48, ratio=9, risetime=.25, falltime=.1, knee=0.5, mul=2).out()
compchowet.ctrl()

#limiter = Clip([compdry,compchodry,compchowet], min=-1, max=0.707, mul=.9).out()
#limiter.ctrl()

# set master volume to -20 db to protect your ears and equipment
s.setAmp(0.1)
# start GUI
s.gui(locals())