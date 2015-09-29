#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 class Convolve(input, table, size, mul=1, add=0)

    Implements filtering using circular convolution.

    A circular convolution is defined as the integral of the product of two functions after one is reversed and shifted.
    Parent:	PyoObject
    Args:	input : PyoObject
				Input signal to process.
    table : PyoTableObject
				Table containning the impulse response.
    size : int
				Length, in samples, of the convolution. Available at initialization time only.
				If the table changes during the performance, its size must egal or greater than this value.
				If greater only the first size samples will be used.

    Note:
	Convolution is very expensive to compute, so the impulse response must be kept very short to run in real time.
	Usually convolution generates a high amplitude level, take care of the mul parameter!


"""


# import necessary  libraries
from pyo import *



# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=44100, buffersize=64, audio='portaudio', nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)



# Input
instr = Input(chnl=[0], mul=0.9)    # chnl=[0,1] for stereo input



# Processing
sf = Noise(.5)

TLEN = 512

#inmic = Input()

t1 = NewTable(length=sampsToSec(TLEN), chnls=1)
r1 = TableRec(instr, table=t1, fadetime=.001)

t2 = NewTable(length=sampsToSec(TLEN), chnls=1)
r2 = TableRec(instr, table=t2, fadetime=.001)

t3 = NewTable(length=sampsToSec(TLEN), chnls=1)
r3 = TableRec(instr, table=t3, fadetime=.001)

t4 = NewTable(length=sampsToSec(TLEN), chnls=1)
r4 = TableRec(instr, table=t4, fadetime=.001)

pha = Sig(0)
pha.ctrl()

t = NewTable(length=sampsToSec(TLEN), chnls=1)
m = TableMorph(pha, t, [t1,t2,t3,t4])
conv = Convolve(sf, table=t, size=t.getSize(), mul=.1).out()



# GUI
s.gui(locals())