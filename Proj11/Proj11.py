# DO NOT MODIFY THE CODE IN THIS FILE
# File: Proj11.py
# Rev 12/05/22
'''
This assignment requires you to write a program demonstrating your 
ability to create a visualization comparing box and violin plots.
'''

import random
from statistics import mean
from Proj11Runner import Runner


# Utility function

def normalRandomGenerator(seed=1, dataLength=10000, numberSamples=50, lowLim=0, highLim=100):
    '''
    Create a new dataset of dataLength values consisting of the average of numberSamples 
    samples taken from a population of uniformly distributed values between lowLim 
    and highLim generated with a seed of seed.

    Input keyword argument and their default values:

    seed = 1 seed used to generate the uniformly distributed values
    dataLength = 10000 number of samples in the returned list of values
    numberSamples = 50 number of samples taken from the uniformly distributed population
                       and averaged into the output
    lowLim = 0 lower limit value of the uniformly distributed population
    highLim = 100 high limit value of the uniformly distributed population

    returns: a list containing the dataset

    '''
    data = []
    random.seed(seed)

    for cnt in range(dataLength):
        theSum = 0
        for cnt1 in range(numberSamples):
            theSum += random.uniform(lowLim, highLim)
        data.append(theSum / numberSamples)

    return data
    # ==================================================================


g01 = normalRandomGenerator(dataLength=10000,
                            numberSamples=3, lowLim=5, highLim=50, seed=1)
g02 = normalRandomGenerator(dataLength=7000,
                            numberSamples=2, lowLim=20, highLim=80, seed=2)
g03 = normalRandomGenerator(dataLength=4000,
                            numberSamples=1, lowLim=30, highLim=90, seed=3)

# Call the student's run method passing two datasets as parameters.
Runner.run(g01, g01 + g02, g01 + g03)
