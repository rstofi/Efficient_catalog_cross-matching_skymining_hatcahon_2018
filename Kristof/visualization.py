"""
------------------------------
MIT License

Copyright (c) 2018 Hachastron

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
------------------------------

Plotting functions for basic uv gridding simulations -> see the corresponding simulations

IMPORTANT: simulations uses arl thus this module is not strongly related to the radio surveys data rate support library
"""

#=================================================
#IMPORTS
#=================================================
import numpy as np;
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
