import numpy as np
from matplotlib import pylab;
from matplotlib import pyplot as plt;

#=================================================
#MAIN
#=================================================
epoch_0 = np.genfromtxt('../Data/epoch00.csv',  dtype=float, delimiter=',',  skip_header=1);
epoch_1 = np.genfromtxt('../Data/epoch01.csv',  dtype=float, delimiter=',',  skip_header=1);
epoch_2 = np.genfromtxt('../Data/epoch02.csv',  dtype=float, delimiter=',',  skip_header=1);

ID = epoch_0[:,0];
RA = epoch_0[:,1];
RA_err = epoch_0[:,2];
Dec = epoch_0[:,3];
Dec_err = epoch_0[:,4];
Flux = epoch_0[:,5];
Flux_err = epoch_0[:,6];

ID10 = []

ID10 = epoch_0[1:10,0];
RA10 = epoch_0[1:10,1];
RA_err10 = epoch_0[1:10,2];
Dec10 = epoch_0[1:10,3];
Dec_err10 = epoch_0[1:10,4];
Flux10 = epoch_0[1:10,5];
Flux_err10 = epoch_0[1:10,6];


plt.clf(); #Clear the current function
plt.plot(RA,Dec,'.');
plt.show();
