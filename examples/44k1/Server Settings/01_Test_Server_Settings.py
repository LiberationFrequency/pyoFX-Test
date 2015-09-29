#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description

"""

# import necessary  libraries
from pyo import *

# dialog
print('List Devices:')
pa_list_devices()

AudioInput = input('Choose the number of the input device:\n')
AudioOutput = input('Choose the number of the output device:\n')
AudioSR = input('Choose the samplerate to start the server:\n')
AudioBuffer = input('Choose the sample buffersize:\n')

print('... booting pyo server\n')



# Server Settings:
## Latency is buffer size / sampling rate in seconds.
s = Server(sr=AudioSR, buffersize=AudioBuffer, audio='portaudio', nchnls=1)
s.setInputDevice(AudioInput)
s.setOutputDevice(AudioOutput)
s.boot()
s.start()
# set master volume to -20 dB to protect your ears and equipment
s.setAmp(0.1)



