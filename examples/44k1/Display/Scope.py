#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 class Scope(input, length=0.05, gain=0.67)

    Oscilloscope - audio waveform display.

    Oscilloscopes are used to observe the change of an electrical signal over time.
    Parent:	PyoObject
    Args:	input : PyoObject
				Input signal to process.
			length : float, optional
				Length, in seconds, of the displayed window. Can’t be a list. Defaults to 0.05.
			gain : float, optional
				Linear gain applied to the signal to be displayed. Can’t be a list. Defaults to 0.67.

    Note:
	Scope has no out method.
	Scope has no mul and add attributes.



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
instr = Input(chnl=0).out()



# Processing
scope = Scope(instr)
#spec = Spectrum(instr, size=1024)



# GUI
s.gui(locals())