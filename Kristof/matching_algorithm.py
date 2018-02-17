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

Cost matrix for the Hungarian algorithm

"""

#=================================================
#IMPORTS
#=================================================
import numpy as np;
from scipy import stats;
from scipy.optimize import linear_sum_assignment; #Hungarian algorithm
import glob;

from position_model import *;
from cost_matrix import *;

#=================================================
#LOGGING
#=================================================
import logging;

log = logging.getLogger();
log.setLevel(logging.INFO);

#=================================================
#SUPPORT FUNCTIONS
#=================================================
def solve_matching_for_galaxy_positions(sm, observed_epoch,epoch_ID):
    """Solve the cost matrix and update sky model
    
    :param sm: Sky model
    :param observed_epoch: given epoch in a numpy array, already readed from .csv
    :param epoch_ID: The ID pf the observed epoch
    """
    cm = compute_cost_matrix(sm,observed_epoch,epoch_ID);
    
    ID_list = observed_epoch[:,0];
    
    #Solve the maching problem with the hungarian algorithm
    observed_ind, matched_model_ind = linear_sum_assignment(cm)
    
    for obs_position_indice in observed_ind:
        add_observation(sm.galax_model_list[matched_model_ind[obs_position_indice]],
                        observed_galaxy_position(epoch=epoch_ID, obs=galaxy_obs(observed_epoch, ID_list[obs_position_indice])));
    
    return sm;

def tinder_for_galaxy_positions(folder=None, initial_dataset=None):
    """Crosmatch the poitions for all the epochs while iterate trough all the observations

    :param folder: The folder where the data is
    :param initial_dataset: The dataset path (&name) which define the initial sky model
    """

    #Create Initial sky model
    if initial_dataset == None:
        initial_dataset = './Small_simulated_data/test_epoch00.csv';
    
    initial_epoch = np.genfromtxt(initial_dataset,  dtype=float, delimiter=',',  skip_header=0);
    initial_epoch_ID =0;

    sm = create_initial_sky_model(initial_epoch_ID, initial_epoch);
    #Setup datafile list
    
    if folder == None:
        folder = './Small_simulated_data/';
    
    epoch_data_list = glob.glob("%s*.csv" %folder);

    #Iterate trough observations
    ep = 1;#Epoch ID
    for epoch in epoch_data_list:
        epoch = np.genfromtxt(epoch,  dtype=float, delimiter=',');
    
        sm = solve_matching_for_galaxy_positions(sm, epoch, ep);
    
        log.info("Epoch %i solved" %ep);
        print('Epoch %i solved' %ep);#Logger not working somehow
        
        ep += 1;
        
    return sm;

#=================================================
#MAIN
#=================================================
if __name__ == '__main__':
    """Test
    """
    #Create Initial sky model
    #initial_epoch = np.genfromtxt('./Small_simulated_data/test_epoch00.csv',  dtype=float, delimiter=',',  skip_header=0);
    #initial_epoch_ID =0;

    #sm = create_initial_sky_model(initial_epoch_ID, initial_epoch);

    #Observation
    #observed_epoch = np.genfromtxt('./Small_simulated_data/test_epoch10.csv',  dtype=float, delimiter=',',  skip_header=0); 
    #epoch_ID = 1;    

    """
    cm = compute_cost_matrix(sm,observed_epoch,epoch_ID);
    
    print(cm)
    
    #Solve the maching problem with the hungarian algorithm
    observed_ind, matched_model_ind = linear_sum_assignment(cm)
    
    for obs_position_indice in observed_ind:
        add_observation(sm.galax_model_list[matched_model_ind[obs_position_indice]],
                        observed_galaxy_position(epoch=epoch_ID, obs=galaxy_obs(observed_epoch, obs_position_indice)));
    """

    #solve_matching_for_galaxy_positions(sm, observed_epoch,epoch_ID);

    sm = tinder_for_galaxy_positions(folder=None, initial_dataset=None);
    
    #sm = tinder_for_galaxy_positions(folder='../Data/', initial_dataset='../Data/epoch00.csv');
    
    #sm = tinder_for_galaxy_positions(folder='./Subdatacube/', initial_dataset='./Subdatacube/test_epoch00.csv');
    
    exit();
    
    print(len(sm.galax_model_list[0].obs_list));#Number of element in each galaxy model of the sky model
    
    #Print all the observations in a galaxy model
    model_ID = 0;#The index in the sky model list
    for obs in sm.galax_model_list[model_ID].obs_list:
        print(obs.ID, obs.RA, obs.RA_err, obs.Dec, obs.Dec_err, obs.Flux, obs.Flux_err);
