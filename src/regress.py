import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

# The two arrays be analyzed


x=[1,2,3,1]
y=[7,8,15,4]

def geo_regress(x,y):
    '''Write Later'''
    

    '''Caclculates the linear regression of XofY'''
    #Calculates the linear regression XofY
    print()
    stats.linregress(x,y)
    slopeXofY,intercept,r,p,stderr= stats.linregress(x,y)
    print('Slope XofY=',slopeXofY)
    print()

    '''Caculates the linear regression of YofX'''
    #calculates the linear regress YofX
    stats.linregress(y,x)
    slopeYofX,intercept,r,p,stderr= stats.linregress(y,x)
    print('Slope YofX=',slopeYofX)
    print()

    #Calcualtes the Geometric Mean
    '''This calculations gives the Geometric Mean'''
    geo_mean = ((slopeYofX)/(slopeXofY))**0.5
    print('Geometric Mean=',geo_mean)
    return geo_mean,intercept
    

slope,intercept= geo_regress(x,y)