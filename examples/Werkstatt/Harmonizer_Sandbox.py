#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Detuned waveguide bank.

"""

from pyo import *
import random


from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()


instr = Input(chnl=0)

harm = Harmonizer(instr, transpo=[5,7,-3,-5], feedback=0.01, winsize=0.1, mul=0.6)
harm.ctrl()

pva = PVAnal(harm, size=1024)
pvt = PVTranspose(pva, transpo=2)
pvs = PVSynth(pvt).out()
dry = Delay(instr, delay=1024./s.getSamplingRate(), mul=.7).out()
dry.ctrl()


env = WinTable(7)

wsize = .1
trans = -7

ratio = pow(2., trans/12.)
rate = -(ratio-1) / wsize

ind = Phasor(freq=rate, phase=[0,0.5])
win = Pointer(table=env, index=ind, mul=.7)

snd = Delay(instr, delay=ind*wsize, mul=win)




# This gives a factor for both the wind intensity and frequency. Intensity
# and frequency go together in the two first filters in order to generate a
# more natural wind. Q variation gives a kind of wind blows.
j = Randi(1,1.4,Randi(.5,1))

# Filter 1 - sort of continuos bass wind
freqs1 = Randi(150, 300)
q1 = Randi(4, 6)
f1 = ButBP(instr, freq=freqs1, q=q1, mul=.2*j)

# Filter 2 - main wind frequency with slow variation, following wind intensity
freqs2 = [Randi(300, 400)*j for i in range(3)]
q2 = Randi(40, 300)
f2 = ButBP(instr, freq=freqs2, q=q2, mul=j*1.5)

# Filter 3 - very high component, almost fixed in frequency
freqs3 = [Randi(2990, 3000)*j for i in range(2)]
q3 = Randi(10, 33)
f3 = ButBP(instr, freq=freqs3, q=q3, mul=.01)

# Filter 4 - the highest frequency wind component, also quite fixed
freqs4 = [Randi(10000, 10100)*j for i in range(2)]
q4 = Randi(10, 33)
f4 = ButBP(instr, freq=freqs4, q=q4, mul=.01)

total = snd + f4

comp = Compress(total, thresh=-24, ratio=2, risetime=.01, falltime=.2, knee=0.5).out(1)
comp.ctrl()




# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)
s.gui(locals())