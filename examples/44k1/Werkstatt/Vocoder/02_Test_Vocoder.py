#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 class Vocoder(input, input2, freq=60, spread=1.25, q=20, slope=0.5, stages=24, mul=1, add=0)

    Applies the spectral envelope of a first sound to the spectrum of a second sound.

    The vocoder is an analysis/synthesis system, historically used to reproduce human speech. 
	In the encoder, the first input (spectral envelope) is passed through a multiband filter, 
	each band is passed through an envelope follower, and the control signals from the envelope followers are communicated to the decoder. 
	The decoder applies these (amplitude) control signals to corresponding filters modifying the second source (exciter).
    
	Parent:	PyoObject
    Args:	input : PyoObject
				Spectral envelope. Gives the spectral properties of the bank of filters. For best results, this signal must have a dynamic spectrum, both for amplitudes and frequencies.
			input2 : PyoObject
				Exciter. Spectrum to filter. For best results, this signal must have a broadband spectrum with few amplitude variations.
			freq : float or PyoObject, optional
				Center frequency of the first band. This is the base frequency used to compute the upper bands. Defaults to 60.
			spread : float or PyoObject, optional
				Spreading factor for upper band frequencies. Each band is freq * pow(order, spread), where order is the harmonic rank of the band. Defaults to 1.25.
			q : float or PyoObject, optional
				Q of the filters as center frequency / bandwidth. Higher values imply more resonance around the center frequency. Defaults to 20.
			slope : float or PyoObject, optional
				Time response of the envelope follower. Lower values mean smoother changes, while higher values mean a better time accuracy. Defaults to 0.5.
			stages : int, optional
				The number of bands in the filter bank. Defines the number of notches in the spectrum. Defaults to 24.

    Note:
	Altough parameters can be audio signals, values are sampled only four times per buffer size. 
	To avoid artefacts, it is recommended to keep variations at low rate (< 20 Hz). 

"""

# import necessary libraries
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
comp = Compress(instr, thresh=-6, ratio=1.5, risetime=.02, falltime=.25, knee=0.5)
comp.ctrl()

a = SfPlayer('../../snds/baseballmajeur_m.aif', loop=True)
#b = PinkNoise(.1)
#c = SfPlayer('../../snds/ounkmaster.aif', loop=True)

voc = Vocoder(a, comp, freq=220, spread=[1.2,1.22], q=20, slope=.5, stages=24, mul=.6).out()
voc.ctrl()

#comp = Compress(voc, thresh=-12, ratio=2, risetime=.125, falltime=2, knee=0.5).out()
#comp.ctrl()


# GUI
s.gui(locals())