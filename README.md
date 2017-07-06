README.md file describes:
Steps needed to run the code on another computer
Data sources
Dependencies
Location of data in repository, or how to access data

Welcome to the project by Alan Gelber.

To run this code:
The original data files are in the data folder.  The modified data files for the 5 sites are in the source (src) folder and have extension _atom.csv. These files have been cleaned up for erroneous data and missing values.  The headers have also been modified to ensure simplicity when calling a data frame. 

How to access Repository:

	go to www.github.com
	pull from: /agelber82/Particle-Size-Analysis

External Packages Needed:
	
	-%matplotlib notebook
	-import numpy as np
	-import pandas as pd
	-from scipy import stats
	-from matplotlib import pyplot as plt
	-import os
	-import cartopy.crs as ccrs
	-import cartopy as cart
	-import cartopy.feature as cfeature
	-from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
	-from maptools import make_map


Steps to Run Code:
	
	1) Import Libraries listed above
	2) Open data sources
	3) Import data frames for 'Mean:' and 'Depth'
	4) Plot mean and depth
	5) Run 1D linear Regression

Data Sources: http://publications.iodp.org/preliminary_report/363/

	U1484A_atom.csv (modified and cleaned up file)
	U1485A_atom.csv (modified and cleaned up file)
	U1486B_atom.csv (modified and cleaned up file)
	U1489B_atom.csv (modified and cleaned up file)
	U1489C_atom.csv (modified and cleaned up file)
