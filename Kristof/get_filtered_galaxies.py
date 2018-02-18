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

Get the galaxies that are matched trough all epoch using Karl's filtering algorithm

"""
#=================================================
#IMPORTS
#=================================================
import numpy as np;
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


def get_filtered_galaxy_ID_list(folder=None):
    """Returns a matrix of (max_filtered_rows x epoch) each element is a galaxy ID
    observed in the given epoch and filtered.
    
    If we lost a galaxy halfway, the number is -1
    
    :param folder: The folder where the filtered data is
    """
    if folder == None:
        folder = './Two_filtered_epoch/';
    
    filtered_match_first_iteration_list = sorted(glob.glob("%s*.csv" %folder));
    
    max_filter = np.genfromtxt(filtered_match_first_iteration_list[0],  dtype=float, delimiter=',').shape[0];
    
    source_index_matrix = np.zeros((max_filter,len(filtered_match_first_iteration_list)));#empty matrix for indices
   
    source_index_matrix[:,0] = np.genfromtxt(filtered_match_first_iteration_list[0],  dtype=float, delimiter=',')[:,0];
    
    j = 0;
    for filtered_match_file in filtered_match_first_iteration_list[:1]:
        epoch = np.genfromtxt(filtered_match_file,  dtype=float, delimiter=',');
        
        for i in range(0,max_filter):
            if source_index_matrix[i,j] in epoch[:,0]:
                source_index_matrix[i,j+1] = epoch[np.argwhere(epoch[:,0] == source_index_matrix[i,j]),7];
            else:
                source_index_matrix[i,j+1] = -1;
                                
        j += 1;

    return source_index_matrix;

#=================================================
#MAIN
#=================================================
if __name__ == '__main__':
    """Test
    """
    

    source_index_matrix = get_filtered_galaxy_ID_list();    

    folder = '../Data/';
    
    observed_epoch_list = sorted(glob.glob("%s*.csv" %folder));
    
    
    
    
    
    print(source_index_matrix);
        
        
    
    
