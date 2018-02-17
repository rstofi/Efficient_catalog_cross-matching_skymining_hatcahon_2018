import numpy as np
from matplotlib import pylab;
from matplotlib import pyplot as plt;

#=================================================
#MAIN
#=================================================
epoch_0 = np.genfromtxt('../Data/epoch00.csv',  dtype=float, delimiter=',',  skip_header=1);

ID = epoch_0[:,0];
RA = epoch_0[:,1];
RA_err = epoch_0[:,2];
Dec = epoch_0[:,3];
Dec_err = epoch_0[:,4];
Flux = epoch_0[:,5];
Flux_err = epoch_0[:,6];

plt.clf();
plt.plot(RA,Dec,'.');
plt.show();
