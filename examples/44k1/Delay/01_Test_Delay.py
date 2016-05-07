#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 class Delay(input, delay=0.25, feedback=0, maxdelay=1, mul=1, add=0)

    Sweepable recursive delay.
    Parent:	PyoObject
    Args:	input : PyoObject
				Input signal to delayed.
    delay : float or PyoObject, optional
				Delay time in seconds. Defaults to 0.25.
    feedback : float or PyoObject, optional
				Amount of output signal sent back into the delay line. Defaults to 0.
    maxdelay : float, optional
				Maximum delay length in seconds. Available only at initialization. Defaults to 1.


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
s.setAmp(.1)


# Input
instr = Input(chnl=0)


# Processing
delay = Delay(instr, delay=0.3, feedback=0.1, mul=0.5).out()
delay.ctrl()


# GUI
s.gui(locals())