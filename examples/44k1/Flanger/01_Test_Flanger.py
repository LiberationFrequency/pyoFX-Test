#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description:
see flanger_lib.py

"""


# import necessary libraries
from pyo import *
from flanger_lib import Flanger


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
lfo = Sine(75, mul=0.25, add=0.5)
lfo.ctrl()
flg = Flanger(instr, depth=0.8, lfofreq=0.5, feedback=lfo).out()
flg.ctrl()



# GUI
s.gui(locals())