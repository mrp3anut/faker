import numpy as np
import pandas as pd
import noise



#This is a python module to create fake seismological data

def noisef(time, noise_type='gaussian', std=1, mean=0, outtype ='ndarray', noise_octave = False):
	
	return np.random.normal(mean,std,time)
	if noise_type == 'perlin':
		

		t = np.linspace(0,time,20*100)
		y1 = np.array(list(map(lambda y: pnoise1(y), t)))

		noise = np.random.normal(mean,std,time)
		y2 = np.add(y1,noise.pnoise1)

		return y2

	#if noise_type == 'simplex' Not now



def noisef_and_signal(time, noise_type='gaussian', std=1,mean=0,outtype='ndarray',signal = 'seismic'):
	import noise
	return

