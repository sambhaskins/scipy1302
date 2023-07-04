# DO NOT MODIFY THE CODE IN THIS FILE
# File: Proj10.py
# Rev 03/30/23
'''
This assignment requires you to write a program demonstrating 
your knowledge of various aspects of box and whisker plots.
'''

import random
from statistics import mean
from Proj10Runner import Runner


# This is a utility function.
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
    # =====================================================================


# Create a dataset based on a random number generator that can be used to
# illustrate Box & Whisker plots.
g01 = normalRandomGenerator(dataLength=10000,
                            numberSamples=3, lowLim=10, highLim=40, seed=1)
g02 = normalRandomGenerator(dataLength=6000,
                            numberSamples=2, lowLim=20, highLim=80, seed=2)
g03 = normalRandomGenerator(dataLength=4000,
                            numberSamples=1, lowLim=30, highLim=90, seed=3)
g04 = g01 + g02 + g03 + [120]

# Create another dataset that can be used to illustrates a Box & Whisker
# plot with a notch.
g05 = [110] + normalRandomGenerator(dataLength=1000,
                                    numberSamples=1, lowLim=60, highLim=90, seed=1)


# Call the student's run method passing the two datasets as parameters
Runner.run(g04, g05)
