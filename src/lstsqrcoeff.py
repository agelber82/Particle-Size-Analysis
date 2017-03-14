# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:25:08 2017

@author: alang
"""

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt


def harmonics(y,t,unit):
    '''this function will calculate the least square differences for the coeffecients'''
    if unit is 'years':
        t = t
    elif unit is 'days':
        t = t/365
    elif unit is 'hours':
        t = t/24
    elif unit is 'seconds':
        t = t/31557600
    else:
        print('Imporper Units')
   
    y =np.array(y)
    t =np.array(t)
    n = len(y)
    
    
    '''This is the matrix which all the data will be stored'''
    '''Constant'''
    col0 = np.ones(n)
    col0.resize((n,1))
    '''Annual harmonic sine of a 1 year period'''
    col1=np.sin((2*np.pi*t)/12)
    col1.resize((n,1))
    '''Annual harmonic cosine of a 1 year period'''  
    col2=np.cos((2*np.pi*t)/12)
    col2.resize((n,1))
    '''Annual harmonic sine of a 6 month period'''
    col3=np.sin((2*np.pi*t)/6)
    col3.resize((n,1))
    '''annual harmonic cosine of a 6 month period''' 
    col4=np.cos((2*np.pi*t)/6)
    col4.resize((n,1))
    '''Linear trend'''   
    col5=t
    col5.resize((n,1))
        
    matrix = np.concatenate(((col0,col1,col2,col3,col4,col5)), axis=1) #patches the matrix together

    print()
    coeffs = np.linalg.lstsq(matrix,y)[0] #will give only coeffecients
    cons= 'Constant is =', coeffs[0] #constant
    lintre = 'Linear Trend is=',coeffs[5] #linear trend
    anlsin = 'Annual sine is =', coeffs[1] #annual harmonic sine of a 1 year period
    anlcos = 'Annual cosine is =', coeffs[2] #annual harmonic cosine of  1 year period
    seanlsin = 'Seminannual sine is =', coeffs[3] #semiannual harmonic sine of a 6 month period
    seanlcos = 'Semiannual cosine is =', coeffs[4] #semiannual harmonic cosine of a 6 month period
    return cons,lintre,anlsin,anlcos,seanlsin,seanlcos
    

