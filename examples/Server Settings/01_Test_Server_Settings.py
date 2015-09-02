#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *

print('List Devices:')
pa_list_devices()

AudioInput = input('Choose the number of the input device:\n')
AudioOutput = input('Choose the number of the output device:\n')
AudioSR = input('Choose the samplerate to start the server:\n')
AudioBuffer = input('Choose the sample buffersize:\n')

print('... booting pyo server\n')

s = Server(sr=AudioSR, buffersize=AudioBuffer, nchnls=1)
s.setInputDevice(AudioInput)
s.setOutputDevice(AudioOutput)
s.boot()
s.start()




