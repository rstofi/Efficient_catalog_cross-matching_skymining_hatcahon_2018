import numpy as np
from matplotlib import pylab;
from matplotlib import pyplot as plt;

#=================================================
#MAIN
#=================================================

def get_data_colums(epoch):
    """Return the data columns of a given epoch

    :param epoch: given epoch in a numpy array, already readed from .csv
    """

    ID = epoch[:,0];
    RA = epoch[:,1];
    RA_err = epoch[:,2];
    Dec = epoch[:,3];
    Dec_err = epoch[:,4];
    Flux = epoch[:,5];
    Flux_err = epoch[:,6];
    if epoch.shape[1] > 7:
        Neighbr = epoch[:,7];
        Nhbr1_d = epoch[:,8];
        Nhbr2_d = epoch[:,9];

        return ID, RA, RA_err, Dec, Dec_err, Flux, Flux_err, Neighbr, Nhbr1_d, Nhbr2_d ;
    else:
        return ID, RA, RA_err, Dec, Dec_err, Flux, Flux_err;

#=================================================
#PLOT FUNCTIONS
#=================================================

def plot_epoch_sky(epoch):
    """Plot the observed galaxy positions in the sky

    :param epoch: given epoch in a numpy array, already readed from .csv
    """

    ID, RA, RA_err, Dec, Dec_err, Flux, Flux_err = get_data_colums(epoch);

    fig=plt.figure(figsize=(12,12));
    plt.clf();
    plt.title('Sources on the sky', size=24);
    plt.errorbar(RA, Dec, xerr=RA_err, yerr=Dec_err, fmt='o');
    pylab.xlabel('RA [deg]', fontsize = 24);
    pylab.ylabel('Dec [deg]', fontsize = 24);
    plt.tick_params(labelsize=18);
    plt.tight_layout();
    plt.show();

def plot_two_epoch_sky(epoch1, epoch2):
    """Plot the observed galaxy positions in the sky

    :param epoch1: The firs given epoch in a numpy array, already readed from .csv
    :param epoch2: The second given epoch in a numpy array, already readed from .csv
    """

    ID_1, RA_1, RA_err_1, Dec_1, Dec_err_1, Flux_1, Flux_err_1 = get_data_colums(epoch1);
    ID_2, RA_2, RA_err_2, Dec_2, Dec_err_2, Flux_2, Flux_err_2 = get_data_colums(epoch2);

    fig=plt.figure(figsize=(12,12));
    plt.clf();
    plt.title('Sources on the sky', size=24);

    plt.errorbar(RA_1, Dec_1, xerr=RA_err_1, yerr=Dec_err_1, fmt='o', color='blue', alpha=0.5);
    plt.errorbar(RA_2, Dec_2, xerr=RA_err_2, yerr=Dec_err_2, fmt='o', color='red', alpha=0.5);

    pylab.xlabel('RA [deg]', fontsize = 24);
    pylab.ylabel('Dec [deg]', fontsize = 24);
    plt.tick_params(labelsize=18);

    plt.tight_layout();
    plt.show();


def plot_two_epoch_sky_cl(epoch1, epoch2):
    """Plot the observed galaxy positions in the sky

    :param epoch1: The firs given epoch in a numpy array, already readed from .csv
    :param epoch2: The second given epoch in a numpy array, already readed from .csv
    """

    ID_1, RA_1, RA_err_1, Dec_1, Dec_err_1, Flux_1, Flux_err_1 = get_data_colums(epoch1);
    ID_2, RA_2, RA_err_2, Dec_2, Dec_err_2, Flux_2, Flux_err_2, Neighbr, Nhbr1_d, Nhbr2_d = get_data_colums(epoch2);

    Nhbr1_d_ave = np.average(Nhbr1_d)
    Nhbr1_d_mdn = np.median(Nhbr1_d)

    plt.clf();
    plt.title('Sources on the sky', size=24);

    plt.errorbar(RA_1, Dec_1, xerr=RA_err_1, yerr=Dec_err_1, fmt='o', color='blue', alpha=0.5);
    plt.errorbar(RA_2, Dec_2, xerr=RA_err_2, yerr=Dec_err_2, fmt='o', color='red', alpha=0.5);
    #plt.errorbar(RA_2,Dec_2,yerr=Min_dist, color='gray', fmt='o', mfc='white', zorder=1)

    ax = plt.gca()

    # Clumbsy but I don't know how to get the for loop working
    i = 1
    circ = plt.Circle((RA_2[i], Dec_2[i]), 2, color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d[i], color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr2_d[i], color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d_ave, color='purple', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d_mdn, color='yellow', fill=False)
    ax.add_artist(circ)

    i = ID_2.size-1
    circ = plt.Circle((RA_2[i], Dec_2[i]), 2, color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d[i], color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr2_d[i], color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d_ave, color='purple', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d_mdn, color='yellow', fill=False)
    ax.add_artist(circ)
    i = 1000
    circ = plt.Circle((RA_2[i], Dec_2[i]), 2, color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d[i], color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr2_d[i], color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d_ave, color='purple', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d_mdn, color='yellow', fill=False)
    ax.add_artist(circ)
    i = 2000
    circ = plt.Circle((RA_2[i], Dec_2[i]), 2, color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d[i], color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr2_d[i], color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d_ave, color='purple', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d_mdn, color='yellow', fill=False)
    ax.add_artist(circ)

    i = 3000
    circ = plt.Circle((RA_2[i], Dec_2[i]), 2, color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d[i], color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr2_d[i], color='black', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d_ave, color='purple', fill=False)
    ax.add_artist(circ)
    circ = plt.Circle((RA_2[i], Dec_2[i]), Nhbr1_d_mdn, color='yellow', fill=False)
    ax.add_artist(circ)

    circ = []
    for i in range(0,ID_2.size):
        #circ.append = plt.Circle((ID_2[i], RA_2[i]), 1, color='green', fill=False)
        circ = plt.Circle((ID_2[i], RA_2[i]), 1, color='green', fill=False)

        ax.add_artist(circ)
        circ = plt.Circle((ID_2[i], RA_2[i]), Nhbr1_d[i], color='black', fill=False)

        ax.add_artist(circ)
        #circ[i] = plt.Circle((ID_2[i], RA_2[i]), Nhbr2_d[i], color='black', fill=False)
        ax.add_artist(circ)
        #ax.add_artist(circ)[i]




    pylab.xlabel('RA [deg]', fontsize = 24);
    pylab.ylabel('Dec [deg]', fontsize = 24);
    plt.tick_params(labelsize=18);

    plt.tight_layout();

    plt.show();

"""
y_array1 = np.array((1,1,0,1))
y_array2 = np.array((1,3,0,3))
y_array3 = np.array((1,5,0,5))

y_array1 = np.row_stack((y_array1,y_array2))
y_array = np.row_stack((y_array1,y_array3))

x_array1 = np.array((1,3,0,5))
x_array2 = np.array((1,0.5,0,0.5))
x_array3 = np.array((1,5.5,0,6))
x_array1 = np.row_stack((x_array1,x_array2))
x_array = np.row_stack((x_array1,x_array3))
"""


# Karl attempt
def find_index_of_nearest_xy(y_array, x_array, y_point, x_point, distance_filter):
    distance = ((y_array-y_point)**2 + (x_array-x_point)**2)**(.5)
    #idy,idx = np.where(distance1==distance1.min())
    index = np.where(distance==distance.min())
    distance1 = distance[distance==distance.min()]
    distance2 =  np.sort(distance)[1]
    fltr = distance_filter*np.array(distance1[0])
    filter_bool = distance2 > fltr
    return index[0][0], distance1[0], distance2, filter_bool

def do_all(y_array, x_array, distance_filter):
    store = []
    for i in range(0,y_array.shape[0]):
        store.append(find_index_of_nearest_xy(
            x_array[:,3],x_array[:,1],y_array[i,3],y_array[i,1], distance_filter)) #2nd and 4th cols are ones of interest
    return store
"""
distance_filter = 3
do_all(y_array, x_array, distance_filter)
"""
def fltrd_nghbr_dupl(epoch01_ref00):
    # Check if any 'accepted in' values have duplicate neighbours in epoch00_ref
    indices = np.setdiff1d(np.arange(len(epoch01_ref00)),
        np.unique(epoch01_ref00, return_index=True)[1])
    duplicates = epoch01_ref00[indices]

    #for i in range(0,epoch00.shape[0]):
    return duplicates
#------------------------------------------------------------------------------------------------------------------
def update_epoch01_for_dups(dup_list,epoch01):
#    store = []
    for i in range(0,dup_list.shape[0]):
        epoch01[epoch01[:,7]==dup_list[i],10] = False

    return epoch01[:,7]

def update_epoch00_for_filter(epoch00,epoch01fltrd):
    epoch00t = []
    for i in range(0,epoch01fltrd.shape[0]):
        #epoch00t[epoch00[:,0]==epoch01fltrd[i,7],0]= epoch01fltrd[i,0]
        #epoch00[epoch01fltrd[i,7],0]= epoch01fltrd[i,0]
        epoch00[epoch00[:,0]==epoch01fltrd[i,7],0]= True
        #epoch00t[epoch00[:,0] != 1,0] == False
    epoch00[epoch00[:,0] != 1,0] == False
    return epoch00[:,0]

#=================================================
#MAIN
#=================================================
if __name__ == "__main__":
    epoch_0 = np.genfromtxt('../Data/epoch00.csv',  dtype=float, delimiter=',',  skip_header=1);
    epoch_1 = np.genfromtxt('../Data/epoch01.csv',  dtype=float, delimiter=',',  skip_header=1);

    distance_filter = 2 #is the proportion between 1st and 2nd neighbour to filter 1st neighbour as certain
    results = do_all(epoch_1, epoch_0, distance_filter)

    epoch01temp = np.concatenate((epoch_1, results), axis=1) #combine matrices by additional columns
    perc_filter = np.sum(epoch01temp[:,9]) / epoch01temp[:,9].shape
    # with distance_filter = 3 , filter 59%. filter = 2, filter 77%.

    # Below takes epoch00, epoch row reference, and epoch filter boolean
    #update_epoch00 = update_first_epoch_for_filter(epoch00,epoch01temp[:,7],epoch01temp[:,10])
    dup_list = fltrd_nghbr_dupl(epoch01temp[:,7])
    epoch01temp[:,7] = update_epoch01_for_dups(dup_list,epoch01temp) # Remove double ups
    epoch01fltrd = epoch01temp[epoch01temp[:,10]==True,:]
    np.savetxt('../Data/epoch01filtered.csv', epoch01fltrd, delimiter=",") # 7th col = index of epoch00 neighbour, 8th col = distance
    #np.savetxt('../Data/epoch01temp.csv', epoch01temp, delimiter=",") # 7th col = index of epoch00 neighbour, 8th col = distance

    #epoch00temp[:,7:8] = update_epoch00_for_filter(epoch00temp,epoch01fltrd)

    epoch00temp = update_epoch00_for_filter(epoch_0,epoch01fltrd)
    epoch00temp = np.column_stack([np.array(epoch_0), epoch00temp])
    epoch00fltrd = epoch01temp[epoch00temp[:,0]==True,:]
    np.savetxt('../Data/epoch00filtered.csv', epoch00fltrd, delimiter=",") # 7th col = index of epoch00 neighbour, 8th col = distance
    np.savetxt('../Data/epoch00temp.csv', epoch00temp, delimiter=",") # 7th col = index of epoch00 neighbour, 8th col = distance

    #print(np.array(results).shape)
    #print(epoch_1.shape)


    #epoch_0 = np.genfromtxt('C:/Users/karl_/Dropbox/Study, business/Data Science, John Hopkins, Coursera/Hackastron/epoch00.csv',  dtype=float, delimiter=',',  skip_header=1)
    #epoch_1 = np.genfromtxt('C:/Users/karl_/Dropbox/Study, business/Data Science, John Hopkins, Coursera/Hackastron/epoch01.csv',  dtype=float, delimiter=',',  skip_header=1)

    #plot_epoch_sky(epoch_0);
    #plot_two_epoch_sky(epoch_0, epoch_1)
    #plot_two_epoch_sky(x_array, y_array)

    #plot_two_epoch_sky_cl(epoch_0, epoch01temp) #KR: Plot with circles

    #filter_pcnt
#-----------------------------------
    ID_1, RA_1, RA_err_1, Dec_1, Dec_err_1, Flux_1, Flux_err_1 = get_data_colums(epoch_0);
    ID_2, RA_2, RA_err_2, Dec_2, Dec_err_2, Flux_2, Flux_err_2 = get_data_colums(epoch_1);

    fig=plt.figure(figsize=(12,12));
    plt.clf();
    plt.title('Sources on the sky', size=24);

    plt.errorbar(RA_1, Dec_1, xerr=RA_err_1, yerr=Dec_err_1, fmt='o', color='blue', alpha=0.5);
    plt.errorbar(RA_2, Dec_2, xerr=RA_err_2, yerr=Dec_err_2, fmt='o', color='red', alpha=0.5);

    pylab.xlabel('RA [deg]', fontsize = 24);
    pylab.ylabel('Dec [deg]', fontsize = 24);
    plt.tick_params(labelsize=18);

    ID_1, RA_1, RA_err_1, Dec_1, Dec_err_1, Flux_1, Flux_err_1, Neighbr, Nhbr1_d, Nhbr2_d  = get_data_colums(epoch00fltrd);
    #ID_2, RA_2, RA_err_2, Dec_2, Dec_err_2, Flux_2, Flux_err_2 = get_data_colums(epoch01fltrd);
    ID_2, RA_2, RA_err_2, Dec_2, Dec_err_2, Flux_2, Flux_err_2, Neighbr, Nhbr1_d, Nhbr2_d = get_data_colums(epoch01fltrd);

    plt.errorbar(RA_1, Dec_1, xerr=RA_err_1, yerr=Dec_err_1, fmt='o', color='green', alpha=0.5);
    plt.errorbar(RA_2, Dec_2, xerr=RA_err_2, yerr=Dec_err_2, fmt='o', color='black', alpha=0.5);

    plt.tight_layout();
    plt.show();



""""
results = do_all(y_array, x_array)
results
from matplotlib import pyplot as plt;
plt.plot(x_array[:,1], x_array[:,3], "o",color='blue')
plt.plot(y_array[:,1], y_array[:,3], "o",color='red')
plt.tick_params(labelsize=18);

plt.tight_layout();

plt.show();
#np.savetxt("C:/Users/karl_/Dropbox/Study, business/Data Science, John Hopkins, Coursera/Hackastron/epoch01temp.csv", results, delimiter=",")
#np.savetxt('../Data/epoch01temp.csv', epoch01temp, delimiter=",") # 7th col = index of epoch00 neighbour, 8th col = distance
    
"""
