#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Phaser Test
"""

from pyo import *



"""
Server Settings:

Latency is buffer size / sampling rate in seconds.

"""
s = Server(sr=44100, buffersize=64, audio='portaudio', nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)


# Input
instr = Input(chnl=0)



# Processing

fade = Fader(fadein=.1,mul=0.7).play()
fade.ctrl()
#noise = Noise(mul=.25,add=0)
#noise.ctrl()
lf1 = Sine(freq=[.1,.15],mul=100,add=250)
lf1.ctrl()
lf2 = Sine(freq=[.18,.15],mul=.4,add=1.5)
lf2.ctrl()
phaser = Phaser(instr,freq=lf1,spread=lf2,q=1,feedback=0.5,num=20,mul=.5)
phaser.ctrl()

comp = Compress(phaser, thresh=-24, ratio=2, risetime=.01, falltime=.15, knee=0.5).out()
comp.ctrl()



# GUI
s.gui(locals())