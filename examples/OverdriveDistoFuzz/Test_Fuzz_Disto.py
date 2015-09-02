#!/usr/bin/env python
# encoding: utf-8
"""
Fuzz distortion. High gain followed by, asymmetrical clipping, 
hard clip on top, soft compression on bottom.

"""

from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

BP_CENTER_FREQ = 250
BP_Q = 2
BOOST = 5
LP_CUTOFF_FREQ = 3500
BALANCE = 0.8


instr = Input(chnl=0)

# Transfert function for signal lower than 0
low_table = ExpTable([(0,-.25),(4096,0),(8192,0)], exp=10)
# Transfert function for signal higher than 0
high_table = CosTable([(0,0),(4096,0),(4598,1),(8192,1)])

# Bandpass filter and boost gain applied on input signal
bp = Biquad(instr, freq=BP_CENTER_FREQ, q=BP_Q, type=2, mul=.5)
bp.ctrl()
boost = Sig(bp, mul=BOOST)

# Split signal into positive and negative part
sign = Compare(boost, comp=0, mode=">=")
sw = Switch(boost, outs=2, voice=sign)

# Apply transfer function
lowsig = Lookup(low_table, sw[0])
highsig = Lookup(high_table, sw[1])

# Lowpass filter on distorted signal
lp = Tone(lowsig+highsig, freq=LP_CUTOFF_FREQ, mul=.3)
lp.ctrl()

# Balance between dry and wet signals
out = Interp(instr, lp, interp=BALANCE).out()
out.ctrl()

# set global Volume to -20 db to protect your ears and equipment
s.setAmp(0.1)
# start GUI
s.gui(locals())