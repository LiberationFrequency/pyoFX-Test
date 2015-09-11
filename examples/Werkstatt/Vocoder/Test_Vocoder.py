#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Vocoder Test
"""

from pyo import *
from vocoder_lib import MyVocoder


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

comp = Compress(instr, thresh=-6, ratio=1.5, risetime=.02, falltime=.25, knee=0.5)
comp.ctrl()

a = SfPlayer('../../snds/baseballmajeur_m.aif', loop=True)
#b = PinkNoise(.1)
#c = SfPlayer('../../snds/ounkmaster.aif', loop=True)

voc = MyVocoder(in1=a, in2=comp, base=220, spread=[1.2,1.22], q=20, num=12, mul=.6).out()
voc.ctrl()

#comp = Compress(voc, thresh=-12, ratio=2, risetime=.125, falltime=2, knee=0.5).out()
#comp.ctrl()


# GUI
s.gui(locals())