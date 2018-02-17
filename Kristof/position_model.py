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

Position model class for Hachastron

"""
#=================================================
#IMPORTS
#=================================================
import numpy as np;
from scipy import stats;

#=================================================
#LOGGING
#=================================================
import logging;

log = logging.getLogger();
log.setLevel(logging.INFO);

#=================================================
#SUPPORT FUNCTIONS
#=================================================

def galaxy_obs(epoch, ID):
    """Return a row from the epoc matrix based on ID

    :param epoch: given epoch in a numpy array, already readed from .csv    
    :param ID: the ID of the galaxy in the given epoch
    """
    
    ID_index = np.argwhere(epoch[:,0] == ID);
    
    return epoch[ID_index,:][0,0];

#=================================================
#CLASSES
#=================================================
class observed_galaxy_position(object):
    """Describe a galaxy at a given epoch: position and flux
    """
    
    def __init__(self, epoch=np.inf, obs=None):    
        """Class attributes
        
        :parem obs: The row of the galaxy in the observation
        
        :param epoch: The epoch the galaxy was observed
        :param ID: The ID of the galaxy in which epoch the it was observed
        :param RA: RA of the galaxy in which epoch the it was observed
        :param RA_err: RA_err of the galaxy in which epoch the it was observed
        :param Dec: Dec of the galaxy in which epoch the it was observed
        :param Dec_err: Dec_err of the galaxy in which epoch the it was observed
        :param Flux: Flux of the galaxy in which epoch the it was observed
        :param Flux_err: Flux_err of the galaxy in which epoch the it was observed
        """
        
        if epoch == np.inf:
            log.info("No epoch is given");
            raise ValueError;
        try:
            if obs == None:
                obs = np.array([]);
        except:
            pass;
            
        self.epoch = int(epoch);
        self.ID = int(obs[0]);
        self.RA = obs[1];
        self.RA_err = obs[2];
        self.Dec = obs[3];
        self.Dec_err = obs[4];
        self.Flux = obs[5];
        self.Flux_err = obs[6];

class model_galaxy(object):
    """Describe a galaxy model: position and flux
    """
    
    def __init__(self, obs_list=None):    
        """Class attributes
        
        :parem obs_list: List of the observed galaxy positions identified as the model galaxy

        """
        if obs_list == None:
            obs_list = [];
            
        self.obs_list = obs_list;

    @property
    def sky_position(self):
        """return the (ra,dec) sky position tuple
        """
        return (np.average([x.RA for x in self.obs_list[:]]), np.average([x.Dec for x in self.obs_list[:]]));

    @property
    def sky_position_sigma(self):
        """return the (ra,dec) sky position tuple
        """
        if len(self.obs_list[:]) > 1:
            return (self.obs_list[0].RA_err,self.obs_list[0].Dec_err);
        else:
            return (np.std([x.RA_err for x in self.obs_list[:]]), np.std([x.Dec_err for x in self.obs_list[:]]));

    @property
    def sky_radial_sigma(self):
        """return the (ra,dec) sky position tuple
        """
        
        ra_sigma = self.sky_position_sigma[0];
        dec_sigma = self.sky_position_sigma[1];
        
        r_sigma = np.sqrt(ra_sigma *ra_sigma + dec_sigma * dec_sigma);

        return r_sigma;
        
    @property
    def RA_pdf(self):
        """return the mu and sigma of the gaussian distribution of the observed galaxies RA
        """
        RA_list = [];
        RA_err_list = [];
        for galaxy_pos in self.obs_list:
            RA_list.append(galaxy_pos.RA);
            RA_err_list.append(galaxy_pos.RA_err);
        
        vectorized_RA_list = np.array(RA_list);
        vectorized_RA_err_list = np.array(RA_err_list);
        
        if np.std(vectorized_RA_list) > 0:
            return np.average(vectorized_RA_list, weights=vectorized_RA_err_list), np.std(vectorized_RA_list);
        else:
            return np.average(vectorized_RA_list, weights=vectorized_RA_err_list), np.average(np.fabs(vectorized_RA_err_list));

    @property
    def Dec_pdf(self):
        """return the mu and sigma of the gaussian distribution of the observed galaxies RA
        """
        Dec_list = [];
        Dec_err_list = [];
        for galaxy_pos in self.obs_list:
            Dec_list.append(galaxy_pos.Dec);
            Dec_err_list.append(galaxy_pos.Dec_err);
        
        vectorized_Dec_list = np.array(Dec_list);
        vectorized_Dec_err_list = np.array(Dec_err_list);
        
        if np.std(vectorized_Dec_list) > 0:
            return np.average(vectorized_Dec_list, weights=vectorized_Dec_err_list), np.std(vectorized_Dec_list);
        else:
            return np.average(vectorized_Dec_list, weights=vectorized_Dec_err_list), np.average(np.fabs(vectorized_Dec_err_list));

    @property
    def Flux_pdf(self):
        """return the mu and sigma of the gaussian distribution of the observed galaxies RA
        """
        Flux_list = [];
        Flux_err_list = [];
        for galaxy_pos in self.obs_list:
            Flux_list.append(galaxy_pos.Flux);
            Flux_err_list.append(galaxy_pos.Flux_err);
        
        vectorized_Flux_list = np.array(Flux_list);
        vectorized_Flux_err_list = np.array(Flux_err_list);
        
        if np.std(vectorized_Flux_list) > 0:
            return np.average(vectorized_Flux_list, weights=vectorized_Flux_err_list), np.std(vectorized_Flux_list);
        else:
            return np.average(vectorized_Flux_list, weights=vectorized_Flux_err_list), np.average(np.fabs(vectorized_Flux_err_list));

#=================================================
#SUPPORT and EVALUATE FUNCTIONS
#=================================================
def add_observation(model_galaxy,obs):
    """Add an observed galaxy position to the model
    
    :param model_galaxy: The model of a 'real galaxy' consist a bunch of observations
    :param obs: The observed galaxy (observed_galaxy_poition class)
    """
    model_galaxy.obs_list.append(obs);
    
    return model_galaxy;

def p_value_of_observation(model_galaxy, obs):
    """Calculate the following probability of a given observation and model galaxy:
    
    - The probability of a given RA randomly choosen from the model RA_pdf is further away than the observed galaxy RA
    - The probability of a given Dec randomly choosen from the model Dec_pdf is further away than the observed galaxy Dec
    - The probability of a given Flux randomly choosen from the model Flux_pdf is further away than the observed galaxy Flux
      
      
      |
      |
      |
      |
    =   =
     = =
      =
       
    CALCULATES THE OPPOSITE!
    
      =
     = =
    =   =
      |
      |
      |
      |

    These values are calles (two sided) p values.
    
    The output is the averaged p-value.
    
    :param model_galaxy: The model of a 'real galaxy' consist a bunch of observations
    :param obs: The observed galaxy (observed_galaxy_position class)    
    """
    
    model_RA_mu, model_RA_sigma = model_galaxy.RA_pdf;
    model_Dec_mu, model_Dec_sigma = model_galaxy.Dec_pdf;
    model_Flux_mu, model_Flux_sigma = model_galaxy.Flux_pdf;

    #The cdf can be higher than 0.5!
    if obs.RA >= model_RA_mu:
        p_value_RA = (1 - stats.norm.cdf(obs.RA, model_RA_mu, model_RA_sigma)) * 2;#Two sided distribution p value for RA
    else:
        p_value_RA = stats.norm.cdf(obs.RA, model_RA_mu, model_RA_sigma) * 2;#Two sided distribution p value for RA
    
    if obs.Dec >= model_Dec_mu:
        p_value_Dec = (1 - stats.norm.cdf(obs.Dec, model_Dec_mu, model_Dec_sigma)) * 2;#Two sided distribution p value for Dec
    else:
        p_value_Dec = stats.norm.cdf(obs.Dec, model_Dec_mu, model_Dec_sigma) * 2;#Two sided distribution p value for Dec

    if obs.Flux >= model_Flux_mu:
        p_value_Flux = (1 - stats.norm.cdf(obs.Flux, model_Flux_mu, model_Flux_sigma)) * 2;#Two sided distribution p value for RA
    else:
        p_value_Flux = stats.norm.cdf(obs.Flux, model_Flux_mu, model_Flux_sigma) * 2;#Two sided distribution p value for RA
    
    final_p_value = 1 - ((p_value_RA + p_value_Dec + p_value_Flux) / 3);

    return final_p_value;
    
#=================================================
#MAIN
#=================================================
if __name__ == '__main__':
    """Test
    """

    #epoch_0 = np.genfromtxt('../Data/epoch00.csv',  dtype=float, delimiter=',',  skip_header=1);
    
    #ID =120;
    #galaxy = observed_galaxy_position(epoch=0, obs=galaxy_obs(epoch_0, ID));
    
    #print(galaxy_obs(epoch_0, ID));
    #print(galaxy.ID, galaxy.RA, galaxy.RA_err, galaxy.Dec, galaxy.Dec_err, galaxy.Flux, galaxy.Flux_err);

    obs1 = observed_galaxy_position(epoch=0, obs=[0,20,1,1,1,1,1]);
    obs2 = observed_galaxy_position(epoch=1, obs=[0,25,1,2,1,2,1]);
    
    obs3 = observed_galaxy_position(epoch=2, obs=[0,22.5,1,1.5,1,1.5,1]);
    
    simple_model1 = model_galaxy();

    add_observation(simple_model1,obs1);
    add_observation(simple_model1,obs2);

    #print(simple_model1.sky_position);
    #print(simple_model1.sky_position_sigma);
    #print(simple_model1.sky_radial_sigma);

    exit();

    obs11 = observed_galaxy_position(epoch=0, obs=[0,20,1,1,1,1,1]);
    obs21 = observed_galaxy_position(epoch=1, obs=[0,21,1,2,1,2,1]);
        
    simple_model11 = model_galaxy();

    add_observation(simple_model11,obs11);
    add_observation(simple_model11,obs21);
        
    print(p_value_of_observation(simple_model1,obs3));
    print(p_value_of_observation(simple_model11,obs3));
    
