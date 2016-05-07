#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
10-Band Graphic Equalizer

"""


# import necessary libraries
from pyo import *



# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=44100, buffersize=64, audio='portaudio', nchnls=1)
#s = Server(sr=44100, buffersize=64, audio='portaudio', ichnls=1, nchnls=2)    #stereo out
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)



# Input
instr = Input(chnl=[0], mul=0.9)    # chnl=[0,1] for stereo input



# Processing
eq = EQ(instr, freq=[31.5,63,125,250,500,1000,2000,4000,8000,16000], q=1, boost=[0,0,0,0,0,0,0,0,0,0], type=0, mul=.9).out()
eq.ctrl(title='Graphic Equalizer')


# GUI
s.gui(locals())