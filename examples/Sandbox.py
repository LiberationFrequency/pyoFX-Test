#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description

"""

from pyo import *



#Server Settings:
#Latency is buffer size / sampling rate in seconds.
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






# GUI
s.gui(locals())