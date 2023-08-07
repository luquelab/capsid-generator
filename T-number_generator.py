# This python script generates T-numbers

# Input parameters
Tmax = 52 # Maximum T-number
R0 = 1 # Reference radius.

# Libraries
import numpy as np
import pandas as pd


# Definitions
def Tnumber(h : int, k : int) -> int:
    """
    Tnumber(h,k)

    Function that calculates the T-number given the integers h and k, which are non-negative hexagonal coordinate values.

    Parameters
    ----------
    h : int
        Number of steps on the hexagonal coordinate h.
    k : int
        Number of steps on the hexagonal coordinate k.

    Returns
    -------
    Tnumber: int
        The T-number obtained.
    """

    T_hk = h*h + h*k + k*k
    T_hk = T_hk
    return T_hk


def Pnumber(h,k):
    """
    Function that returns the P-class, h0, k0, and f for a pair of h and k
    """
    f = np.gcd(h,k)
    h0 = int(h/f)
    k0 = int(k/f)
    P = h0*h0 + h0*k0 + k0*k0
    return P,f,h0,k0

def max_step(T):
    """
    Function to calculate the potential upper h step for a T-number
    """
    T_sqrt = np.sqrt(T)
    h_max = np.ceil(T_sqrt)
    h_max = int(h_max)
    return h_max

# Estimate upper step for the maximum T-number
h_max = max_step(Tmax) # upper h step
k_max = h_max # upper h step

# List of h and k steps to generate T-numbers
h_list = list(range(0,h_max+1))
k_list = h_list

# Generate T-numbers
dfTnumbers = pd.DataFrame(columns = ['T','h','k','P','f','h0','k0']) # data frame storing the T-numbers
runs = len(h_list)*len(k_list) # number of runs

index = 0 # data frame index counter
for h in h_list:
    for k in k_list:
        T = Tnumber(h,k)
        if 0<T<=Tmax:
            (P,f,h0,k0) = Pnumber(h,k)
            dfTnumbers.loc[index,['T']] = T
            dfTnumbers.loc[index,['h']] = h
            dfTnumbers.loc[index,['k']] = k
            dfTnumbers.loc[index,['P']] = P
            dfTnumbers.loc[index,['f']] = f
            dfTnumbers.loc[index,['h0']] = h0
            dfTnumbers.loc[index,['k0']] = k0
            # print("h = " + str(h) + "  k= " + str(k) + "  T= " + str(T))

            index = index + 1 # increase index counting

dfTnumbers.drop_duplicates ## remove duplicate rows
dfTnumbers.drop(dfTnumbers.index[dfTnumbers['h']==0], inplace = True) ## remove h=0 values to avoid duplicates of P = 1 class capsids
dfTnumbers.sort_values(by=['T'], inplace = True) 
dfTnumbers.reset_index(drop = True, inplace = True)
#print(dfTnumbers)

# Add radius
dfTnumbers['R'] = dfTnumbers['T'].apply(lambda T: R0 * float(T)**0.5)
dfTnumbers['R.80'] = dfTnumbers['R'].apply(lambda R: R*0.98)

dfTnumbers.to_csv("T-number_capsids_sequence.tsv", sep = "\t", index = False)