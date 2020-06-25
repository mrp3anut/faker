import numpy as np
import random as rd

def some_f(sigma, fn, zeta, f, T90, eps, tn):
    
    #Init
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
    
    print(np.shape(A))
    #Time series generation - Monte Carlo simulation
    
    A = np.sqrt(2*S*f0)
    B = np.cos((w.T @ t )+ 2*np.pi * np.tile(np.random.rand(Nfreq,), (1,Nfreq)))
    x = A * B #stationary process
    
    #Envelop function E
    b = -eps * np.log(T90) / (1 + eps * (np.log(T90) - 1))
    c = b / eps
    a = (np.exp(1) / eps)**b
    E = a * (t /tn)**b * np.exp(-c*t/tn)
    
    #Envelop multiplied with stationary process to get y
    
    y = x * E
    
    return(y,t)
