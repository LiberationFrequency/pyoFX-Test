#!/usr/bin/env python
# encoding: utf-8
"""
To record sound from input mic in the buffer (4 seconds), call:
rec.play() 
The buffer is looped with some funny parameters...
"""
from pyo import *

s = Server(sr=44100, buffersize=64, audio='portaudio', nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)

#pit = Choice(choice=[.5,.5,.75,.75,1,1,1.25,1.5], freq=[3,4])
#start = Phasor(freq=.025, mul=tab.getDur()-.5)
#dur = Choice(choice=[.0625,.125,.125,.125,.25,.25,.5], freq=4)
#a = Looper( table=tab, # table to loop in
#            pitch=pit, # transposition
#            start=start, # loop start position
#            dur=dur, # loop duration
#            xfade=20, # crossfade duration in %
#            mode=1, # looping mode 
#            xfadeshape=0, # crossfade shape
#            startfromloop=False, # first start position, False means from beginning of the table
#            interp=2 # interpolation method
#            ).out()




bpm = 120.0
# takt = 4/4
bars = 4
beat = 4	# 1/4
#### ueber 8 Takte sind das 32 Beats
sec = (60 / bpm) * bars * beat 


tab = NewTable(length=sec)
rec = TableRec(Input(chnl=0), tab)


loop = Looper(table=tab, pitch=1, start=0, dur=sec, xfade=10, mode=1, xfadeshape=0,	startfromloop=True, interp=2,autosmooth=False, mul=1, add=0).out()

			
rec.play()
			
s.gui(locals())