#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 class Spectrum(input, size=1024, wintype=2, function=None)

    Spectrum analyzer and display.

    Spectrum measures the magnitude of an input signal versus frequency within a user defined range. 
	It can show both magnitude and frequency on linear or logarithmic scale.
    
	Parent:	PyoObject
    Args:	input : PyoObject
				Input signal to process.
			size : int {pow-of-two > 4}, optional
				FFT size. Must be a power of two greater than 4. The FFT size is the number of samples used in each analysis frame. Defaults to 1024.
    wintype : int, optional
				Shape of the envelope used to filter each input frame. Possible shapes are :

					0. rectangular (no windowing)
					1. Hamming
					2. Hanning
					3. Bartlett (triangular)
					4. Blackman 3-term
					5. Blackman-Harris 4-term
					6. Blackman-Harris 7-term
					7. Tuckey (alpha = 0.66)
					8. Sine (half-sine window)

    function : python callable, optional
		If set, this function will be called with magnitudes (as list of lists, one list per channel). 
		Useful if someone wants to save the analysis data into a text file. Defaults to None.

    Note:
	Spectrum has no out method.
	Spectrum has no mul and add attributes.


"""


# import necessary  libraries
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
instr = Input(chnl=0).out()



# Processing
spec = Spectrum(instr, size=1024)
#scope = Scope(instr)




# GUI
s.gui(locals())