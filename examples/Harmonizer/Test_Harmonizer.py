#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyo import *

s = Server(sr=44100, buffersize=128, nchnls=1)
s.setInputDevice(10)
s.setOutputDevice(9)
s.boot()
s.start()

instr = Input(chnl=0)

harm = Harmonizer(instr, transpo=7, feedback=0.25, winsize=0.15, mul=0.6).out()
harm.ctrl()


# set global Volume to -20 db to protect your ears and equipment
s.setAmp(.1)
# start GUI
s.gui(locals())