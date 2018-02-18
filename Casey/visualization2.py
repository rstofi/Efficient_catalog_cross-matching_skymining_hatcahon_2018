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

Visualization for Hachastron

"""

#=================================================
#IMPORTS
#=================================================
import numpy as np;
from matplotlib import pylab;
from matplotlib import pyplot as plt;
import glob;

#=================================================
#LOGGING
#=================================================
import logging;

log = logging.getLogger();
log.setLevel(logging.INFO);

#=================================================
#SUPPORT FUNCTIONS
#=================================================

def get_position_model_colums(gal_model):
    """Return the data columns of a galaxy position model
    
    :param gal_model: One galaxy model from output of the sky model, already readed from .csv
    """
    
    ID = gal_model[:,0];
    RA = gal_model[:,1];
    RA_err = gal_model[:,2];
    Dec = gal_model[:,3];
    Dec_err = gal_model[:,4];
    Flux = gal_model[:,5];
    Flux_err = gal_model[:,6];
    Epoch = gal_model[:,7];

    return ID, RA, RA_err, Dec, Dec_err, Flux, Flux_err, Epoch;

#=================================================
#PLOT FUNCTIONS
#=================================================

    
def different_color_plot_of_model_galaxies(folder=None):
    """Plot each model galaxy in a given folder with different color
    
    :param folder: The folder where the data is
    """
    if folder == None:
        folder = './Final_sky_model/';
 
    galaxy_position_model_data_list = sorted(glob.glob("%s/*.csv" %folder));
    
    fig=plt.figure(figsize=(12,12));
    plt.clf();
    plt.title('Matched sources on the sky', size=24);
      
    c = ['purple', 'cyan', 'brown'];
   
    i = 0;
    for galaxy_position_model in galaxy_position_model_data_list:
        epoch = np.genfromtxt(galaxy_position_model,  dtype=float, delimiter=',');
        
        ID, RA, RA_err, Dec, Dec_err, Flux, Flux_err, Epoch = get_position_model_colums(epoch);

        plt.errorbar(RA, Dec, xerr=RA_err, yerr=Dec_err,
                    fmt='o', color=c[i], alpha=0.5);
                    
        i += 1;

    pylab.xlabel('RA [deg]', fontsize = 24);
    pylab.ylabel('Dec [deg]', fontsize = 24);
    plt.tick_params(labelsize=18);

    plt.tight_layout();
    
    plt.show();    

#=================================================
#MAIN
#=================================================
if __name__ == "__main__":
    """Testing
    """
    #epoch_0 = np.genfromtxt('../Data/epoch00.csv',  dtype=float, delimiter=',',  skip_header=1);
    #epoch_1 = np.genfromtxt('../Data/epoch01.csv',  dtype=float, delimiter=',',  skip_header=1);

    #plot_epoch_sky(epoch_0);
    #plot_two_epoch_sky(epoch_0, epoch_1)

    different_color_plot_of_model_galaxies();
    
    exit();

    #plot_test_data();
    plot_test_solution();
    #plot_test_data(folder='./Subdatacube');
    #plot_test_solution(folder='./Subdatacube/', initial_dataset='./Subdatacube/test_epoch00.csv');
