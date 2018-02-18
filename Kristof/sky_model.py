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

Sky model

"""

#=================================================
#IMPORTS
#=================================================
import numpy as np;
from scipy import stats;

from position_model import *;
from matching_algorithm import *;

#=================================================
#LOGGING
#=================================================
import logging;

log = logging.getLogger();
log.setLevel(logging.INFO);

#=================================================
#CLASSES
#=================================================
class sky_model(object):
    """Describe The whole sky model: position and flux of all detected galaxies
    """
    
    def __init__(self, galax_model_list=None):    
        """Class attributes
        
        :param galax_model_list: List of galaxy models

        """
        if galax_model_list == None:
            galax_model_list = [];
            
        self.galax_model_list = galax_model_list;

#=================================================
#SUPPORT FUNCTIONS
#=================================================

def human_readable_sky_model(sm):
    """Converts the sky model a human readable, and programable format
    
    - A list of galaxy models from which each one is a matrix
    
    :param sm: Sky model (final hopefuly)
    """
    
    human_readable_sm = [];

    #print(len(sm.galax_model_list[0].obs_list));#Number of element in each galaxy model of the sky model

    model_ID = 0;#The index in the sky model list    
    for galaxy_model in sm.galax_model_list:
        
        human_readable_galaxy_model = np.zeros((len(sm.galax_model_list[0].obs_list),7));
        
        obs_ID = 0;
        for obs in sm.galax_model_list[model_ID].obs_list:
            
            human_readable_galaxy_model[obs_ID,:] = obs.ID, obs.RA, obs.RA_err, obs.Dec, obs.Dec_err, obs.Flux, obs.Flux_err;
            obs_ID += 1;
        
        #Sort galaxy model by obs ID
        #if sort == True:
        #    human_readable_galaxy_model = human_readable_galaxy_model[human_readable_galaxy_model[:,0].argsort()];
        
        #Add galaxy model to sky model
        human_readable_sm.append(human_readable_galaxy_model);
    
        model_ID += 1;
    
    return human_readable_sm;

def get_model_columns(sm,model_index):
    """Return the data columns of the galaxy model (given by index)
    
    :param sm: Sky model in human readable format (final hopefuly)
    :param model_index: The index of the galaxy model 
    """
    
    ID = sm[model_index][:,0];
    RA = sm[model_index][:,1];
    RA_err = sm[model_index][:,2];
    Dec = sm[model_index][:,3];
    Dec_err = sm[model_index][:,4];
    Flux = sm[model_index][:,5];
    Flux_err = sm[model_index][:,6];

    return ID, RA, RA_err, Dec, Dec_err, Flux, Flux_err;

#=================================================
#MAIN
#=================================================
if __name__ == '__main__':
    """Test
    """
    sm = tinder_for_galaxy_positions();
    
    final_sky_model = human_readable_sky_model(sm);
    
    print(len(final_sky_model));
    print(final_sky_model[0][:,0]);
    

    
