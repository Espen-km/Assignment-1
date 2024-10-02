
# The solutions for part A
from math import sqrt 

#1 - Finding the Standard deviation with loops
def std_loops(x):
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

data = [1, 2, 3, 4, 5]
StandardDeviationLoops = std_loops(data)


print(f"Standard Deviation using loops: {StandardDeviationLoops:.3f}")


#2 - Finding the standard deviation using built-in functions

def std_builtin(x): 
    # Compute standard deviation of x using loops

    #Parameters
    # x: sequence of numbers
        N = len(x)
        meanX = x[0]*sum(x)/N
        sumSquares = sum(i**2 for i in x)
        meanSquares = sumSquares/N


        vSquared =  meanSquares - (meanX)**2
        LoopStandardDeviation = float(sqrt(vSquared))

        return LoopStandardDeviation

result = std_builtin([1, 2, 3, 4, 5])
print(f"Standard Deviation using builtin: {result:.3f}")



#3 - Finding the Standard Deviation with numpy

import numpy as np

num_lst1 = [1, 2, 3, 4, 5]

NumpyStd = np.std(num_lst1)

print(f'Standard Deviation using numpy: {NumpyStd:.3f}')