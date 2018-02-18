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

Solution for the small dataset

"""

#=================================================
#IMPORTS
#=================================================
import numpy as np;
from scipy import stats;
from scipy.optimize import linear_sum_assignment; #Hungarian algorithm
import glob;

from position_model import *;
from matching_algorithm import *;
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
def create_solution_file(folder=None):
    """Create the solution matrix
    
    :param folder: The output folder of where the solution mgalaxy models are
    """
    
    if folder == None:
        folder = './Small_solution/';
    
    final_galaxy_position_model_list = sorted(glob.glob("%s*.csv" %folder));
        
    num_of_sources = np.genfromtxt(final_galaxy_position_model_list[0],  dtype=float, delimiter=',').shape[0];
    
    solution_matrix = np.zeros((len(final_galaxy_position_model_list),num_of_sources));
    
    i = 0;
    for final_galaxy_position in final_galaxy_position_model_list:
        observed_galaxy = np.genfromtxt(final_galaxy_position,  dtype=float, delimiter=',')
        
        observed_galaxy_ID_list = observed_galaxy[:,0];
        
        #print(observed_galaxy.shape);
        #print(observed_galaxy_ID_list);
        
        solution_matrix[i,:] = observed_galaxy_ID_list;
        
        
#        for j in range(0,num_of_sources):
#            a=2;
#            print(observed_galaxy[j]);
#            solution_matrix[i,j] = observed_galaxy[j][0];
        
        i += 1;
    
    #print(solution_matrix[:,0]);
    #print(solution_matrix);
    
    #sort by first column ID
    solution_matrix = solution_matrix[solution_matrix[:,0].argsort()];
    
    np.savetxt('./Small_solution_with_hungarian_algorithm.csv', solution_matrix, delimiter=',');

#=================================================
#MAIN
#=================================================
if __name__ == '__main__':
    """Solution
    """
    
    #folder = '../Small/';
    #initial_dataset = '../Small/epoch00.csv'
    
    #sm = tinder_for_galaxy_positions(folder=folder, initial_dataset=initial_dataset);

    #final_sky_model = human_readable_sky_model(sm);
    
    #output_folder = './Small_solution/';
    
    #save_sky_model(final_sky_model, folder=output_folder);

    create_solution_file();
