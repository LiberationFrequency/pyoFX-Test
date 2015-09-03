#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Detuned waveguide bank.

"""

from pyo import *
import random


from pyo import *

s = Server(sr=44100, buffersize=128, audio='portaudio', nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()


instr = Input(chnl=0)

#comp = Compress(instr, thresh=-24, ratio=3, risetime=.01, falltime=.2, knee=0.5)
#comp.ctrl()

#lf = Sine(freq=[random.uniform(.005, .015) for i in range(8)],
#          mul=[.02,.04,.06,.08,.1,.12,.14,.16],
#          add=[50,100,150,200,250,300,350,400])
#lf2 = Sine(.005, mul=.2, add=.7)
#lf.ctrl()
#lf2.ctrl()
det_wg = AllpassWG(instr, freq=82.4, feed=.15, detune=0.5, mul=.25).out()
det_wg.ctrl()
#lowpass filter
#lfo = Sine(freq=[.2, .25], mul=1000, add=1500)
lpf = Biquad(det_wg, freq=400, q=5, type=2)
lpf.ctrl()

compdry = Compress(lpf, thresh=-24, ratio=1.5, risetime=.2, falltime=.2, knee=0.5, mul=.9).out()
compdry.ctrl()
compwet = Compress(compdry, thresh=-48, ratio=6, risetime=.5, falltime=.5, knee=0.5, mul=0.9).out()
compwet.ctrl()

# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())