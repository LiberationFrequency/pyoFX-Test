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
instr = Input(chnl=0)



# Processing
#t = SndTable("../snds/snd_1.aif")
t = SndTable("../snds/snd_2.aif")

#conv = Convolve(instr, table=t, size=t.getSize(), mul=.1).out()
conv = Convolve(instr, table=t, size=512, mul=.1).out()
#conv.ctrl()


# GUI
s.gui(locals())