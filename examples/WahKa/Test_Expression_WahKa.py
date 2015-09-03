#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *

s = Server(sr=44100, buffersize=128, audio='portaudio', nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.setMidiInputDevice(pyo.pm_get_default_input())
s.boot()
s.start()

instr = Input(chnl=0)

pedal = Midictl(7, minscale=200, maxscale=2000)
f = Biquad (instr, freq=pedal, q=5, type=2).out()


# set master volume to -20 db to protect your ears and equipment
s.setAmp(0.1)
# start GUI
s.gui(locals())