import os
import sys
import numpy as np
import pandas as pd



# main function takes a dataframe with 2 labels as argument and returns the same
# dataframe[n x 2] -> dataframe[n x 2]
# removes peaks that satisfy some conditions on the peak roughly 1 Dalton lighter

def Isotope_Remover(df, isotope_weight_difference, isotope_probability):
    
    #get labels for later
    labels = df.columns.values

    #make a 2x(number of mz values) matrix
    df = df.to_numpy()
    df = df.transpose()

    #thing we want to return later/thing we're writing to
    new_df = df

    #loop over the frames or w/e they're called
    number_of_mz = len(df[0])
    
    for mz in range(0, number_of_mz - 1, 1):
        if ((df[mz][1] + isotope_weight_difference) == df[mz + 1][1]) 
        and df[mz][1] >= isotope_probability*df[mz][1])):
            newdf[mz+1][1] = 0


    #convert back to a dataframe for sending back into the program
    newdf = pd.Dataframe({f"{labels[0]}": newdf[:,0],f"{labels[1]}": newdf[:,1]})
    return newdf

#if this script is called, return the value of the function defined above
if __name__ == "__main__":
    #use system arguments
    Isotope_Remover(sys.argv[0], sys.argv[1], sys.argv[2])
