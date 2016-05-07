#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description

"""


# import necessary libraries
from pyo import *



# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=96000, buffersize=128, audio='portaudio', nchnls=1)
#s = Server(sr=96000, buffersize=128, audio='portaudio', ichnls=1, nchnls=2)    #stereo out
s.setInputDevice(9)
s.setOutputDevice(9)
#s.setMidiInputDevice(pyo.pm_get_default_input())    # pm_list_devices()
s.setMidiInputDevice(2)    # pm_list_devices()
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)



# Input
instr = Input(chnl=[0], mul=0.9)    # chnl=[0,1] for stereo input



# Processing
pedal = Midictl(64, minscale=200, maxscale=1500)
#pedal = Midictl(64, minscale=2000, maxscale=200) # inverted
pedal.ctrl()
f = Biquad (instr, freq=pedal, q=5, type=2).out()
f.ctrl()



# start GUI
s.gui(locals())