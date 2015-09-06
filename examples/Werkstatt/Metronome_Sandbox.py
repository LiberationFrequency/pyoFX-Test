#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple Metronome.

ToDo: Convert the slider from time to bpm.
"""

from pyo import *

"""
Server Settings:

Latency is buffer size / sampling rate in seconds.

"""
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

######
#time = 240.0 / tap / bpm


#bpm = 120
taps = 4
time = 1


master = Metro(time).play()
master.ctrl()
# SLMap(min, max, scale, name, init
#master.ctrl(map_list=SLMap(20, 240, 'lin', 'bpm', 0))
tapcount = Counter(master, max=taps)
beat = Select(tapcount, value=[100,0,0,0]).out()
beat.ctrl()





### Clicks ###
clickamp1 = TrigExpseg(master, [(0,0),(0.005,1),(.05,0)], mul=0.5)
click1 = Biquad(Noise(clickamp1), freq=2000, q=10, type=2).out()
clickamp2 = TrigExpseg(beat, [(0,0),(0.005,1),(.05,0)], mul=0.5)
click2 = Biquad(Noise(clickamp2), freq=1000, q=10, type=2).out(1)




# GUI
s.gui(locals())