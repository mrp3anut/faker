import numpy as np
import pandas as pd
from noise import pnoise1



#This is a python module to create fake seismological data

def generate_noise(timeLength, noise_type='gaussian', samplingRate = 20 ,outputType ='ndarray', noise_octave = False, t_start = 0):
	
	
	if noise_type == 'perlin':
		
		t = np.linspace(0,timeLength,timeLength*samplingRate)
		y1 = np.array(list(map(lambda y: pnoise1(y), t)))

		noise = np.random.normal(size = samplingRate*timeLength)
		y2 = np.add(y1, noise)

		return y2

	else:
		return np.random.normal(size=timeLength*samplingRate)



def generate_eq(timeLength, eqCount=1,  samplingRate = 20 ,outputType ='ndarray', t_start = 0):
	return



def generate_noise_and_eq(timeLength, noise_type='gaussian', eqCount=1, samplingRate = 20 ,outputType ='ndarray', noise_octave = False, t_start = 0):

	return generate_eq(timeLength, eqCount, samplingRate, outputType, t_start) + generate_noise(timeLength, noise_type, samplingRate, outputType,noise_octave, t_start)

