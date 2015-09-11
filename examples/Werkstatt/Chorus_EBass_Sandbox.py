#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description

"""

# import necessary libraries
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
instr = Input(chnl=0)


# Processing
eq_Bass = EQ(instr, freq=[10,20,2000,4000,8000,16000], q=1, boost=[-40,-3,-3,-20,-40,-60], type=0)
eq_Bass.ctrl()
#eq_BoostNote = EQ(instr, freq=[30.9,32.7,34.6,36.7,38.9,41.2,43.7,46.2,49,51.9,55,58.3,61.7,65.4,69.3,73.4,77.8,82.4,87.3,92.5,98,103.8,110,116.5,123.5,130.8,138.6,146.8,155.6,164.8,174.6,185,196,207.7,220,233.1,246.9,261.6,277.2,293.7,311.1,329.6,349.2,370,392], q=1, boost=1, type=1)
#eq_BoostNote.ctrl()

cho = Chorus(eq_Bass, depth=0.35, feedback=0.1, bal=0.6, mul=0.8)
cho.ctrl()

compchodry = Compress(cho, thresh=-12, ratio=1.5, risetime=.001, falltime=.05, knee=0.5, mul=0.9).out()
compchodry.ctrl()
compchowet = Compress(cho, thresh=-48, ratio=9, risetime=.015, falltime=.3, knee=0.5, mul=0.6).out()
compchowet.ctrl()


# GUI
s.gui(locals())