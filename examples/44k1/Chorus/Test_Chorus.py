#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 class Chorus(input, depth=1, feedback=0.25, bal=0.5, mul=1, add=0)

    8 modulated delay lines chorus processor.

    A chorus effect occurs when individual sounds with roughly the same timbre and nearly (but never exactly) the same pitch converge and are perceived as one.
    
	Parent:	PyoObject
    Args:	input : PyoObject
				Input signal to process.
    depth : float or PyoObject, optional
				Chorus depth, between 0 and 5. Defaults to 1.
    feedback : float or PyoObject, optional
			Amount of output signal sent back into the delay lines. Defaults to 0.25.
    bal : float or PyoObject, optional
			Balance between wet and dry signals, between 0 and 1. 0 means no chorus. Defaults to 0.5.


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
cho = Chorus(instr, depth=0.2, feedback=0.3, bal=0.5, mul=0.6).out()
cho.ctrl()


# GUI
s.gui(locals())