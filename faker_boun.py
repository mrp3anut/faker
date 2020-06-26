import numpy as np
import pandas as pd
from noise import pnoise1

import matplotlib.pyplot as plt 

#This is a python module to create fake seismological data

def generate_noise(timeLength, noise_type='gaussian', samplingRate = 100 ,outputType ='ndarray', noise_octave = False, t_start = 0):
	
	
	if noise_type == 'perlin':
		
		t = np.linspace(0,timeLength,timeLength*samplingRate)
		y1 = np.array(list(map(lambda y: pnoise1(y), t)))

		noise = np.random.normal(size = samplingRate*timeLength)
		y2 = np.add(y1, noise)

		return y2

	else:
		return np.random.normal(size=timeLength*samplingRate)

	

def generate_eq(timeLength, eqCount=1,  samplingRate = 100 ,outputType ='ndarray', t_start = 0,scale=10,zeta = 0.3, sigma = 0.9,fn =5,T90 = 0.3,eps = 0.4,tn = 30):
    

    #Init
    f = np.linspace(t_start,40,timeLength*samplingRate)
    w = 2 * np.pi * f
    fs = f[-1]
    dt = 1 / fs
    f0 = np.median(np.diff(f))
    Nfreq = len(f)
    t = np.arange(0,dt*(Nfreq),dt)
    
    #Generation of spectrum S
    
    fn = fn * 2 * np.pi #transformation in rad
    s0 = 2 * zeta * (sigma**2) / (np.pi * fn * (4 * (zeta**2) + 1))
    A = (fn**4) + (2*zeta*fn*w)**2
    B = ((fn**2 -  w**2)**2) + (2*zeta*fn*w)**2
    S = s0 * A / B #Single sided PSD
    
    #Time series generation - Monte Carlo simulation
    
    A = np.sqrt(2 * S * f0)
    B = np.cos((w.T * t )+ 2*np.pi * np.tile(np.random.randint(0,Nfreq), (1,Nfreq)))
    #print(np.shape(B))
    x = A * B #stationary process
    
    #Envelop function E
    b = -eps * np.log(T90) / (1 + eps * (np.log(T90) - 1))
    c = b / eps
    a = (np.exp(1) / eps)**b
    E = a * (t /tn)**b * np.exp(-c*t/tn)
    
    #Envelop multiplied with stationary process to get y
    
    y = x * E
    
    return y[0]*scale*100




def generate_noise_and_eq(timeLength, noise_type='gaussian', eqCount=1, samplingRate = 20 ,outputType ='ndarray', noise_octave = False, t_start = 0, scale=10):

	return generate_eq(timeLength, eqCount, samplingRate, outputType, t_start, scale) + generate_noise(timeLength, noise_type, samplingRate, outputType,noise_octave, t_start)
