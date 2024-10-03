
"""
TECH2 mandatory assignment - Part A
"""

from math import sqrt 

data = [1, 2, 3, 4, 5]

#1 - Finding the Standard deviation with loops
def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    sum_x = 0
    sum_x_squared = 0
    N = 0

    for i in x:
        sum_x += i
        sum_x_squared += i**2
        N += 1

    mean = sum_x / N
    mean_x_squared = sum_x_squared/N

    return sqrt(mean_x_squared - mean**2)

StandardDeviationLoops = std_loops(data)

print(f"1. Standard Deviation using loops: {StandardDeviationLoops:.3f}")




#2 - Finding the standard deviation using built-in functions

def std_builtin(x): 
        
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
        
    N = len(x)
    meanX = x[0]*sum(x)/N
    sumSquares = sum(i**2 for i in x)
    meanSquares = sumSquares/N


    vSquared =  meanSquares - (meanX)**2
    LoopStandardDeviation = float(sqrt(vSquared))

    return LoopStandardDeviation

result = std_builtin(data)
print(f"2. Standard Deviation using builtin: {result:.3f}")



#3 - Finding the Standard Deviation with numpy

"""
    Compute standard deviation of x using numpy functions

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

import numpy as np

NumpyStd = np.std(data)

print(f'3. Standard Deviation using numpy: {NumpyStd:.3f}')

