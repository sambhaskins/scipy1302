#DO NOT MODIFY THE CODE IN THIS FILE
#File: Proj04.py
#Rev 12/03/22
'''
Among other things, this project requires that you write a program to
  demonstrate your knowledge of the following topics.
How to plot histograms using matplotlib
How to populate a figure using matplotlib
How to decorate a figure using matplotlib
How to find the mean and standard deviation of a dataset
How to create a normal distribution curve for a given mean 
  and standard deviation
How to overlay a normal distribution curve on a histogram

Revised 02/19/23 to terminate with an error message
if the user fails to enter five command-line
arguments in the format 1,2,3,4,5
'''

from Proj04Runner import Runner
import sys
import random

# Check if the user has entered five command-line arguments
if len(sys.argv) != 2 or len(sys.argv[1].split(',')) != 5:
    print("Error: You must enter exactly five command-line arguments in the format '1,2,3,4,5'.")
    sys.exit()

#Define a utility function that will be used later to create
#several datasets.
def normalRandomGenerator(seed=1,dataLength=10000,numberSamples=50,\
                          lowLim=0,highLim=100):
    '''
    Create a new dataset of dataLength values consisting of the 
    average of numberSamples samples taken from a population of 
    uniformly distributed values between lowLim and highLim 
    generated with a seed of seed.

    Input keyword parameters and their default values:

    seed = 1 seed used to generate the uniformly distributed values
    dataLength = 10000 number of samples in the returned list of values
    numberSamples = 50 number of samples taken from the uniformly 
                    distributed population and averaged into the output
    lowLim = 0 lower limit value of the uniformly distributed population
    highLim = 100 high limit value of the uniformly distributed population

    returns: a list containing the dataset
    '''
    data = []
    random.seed(seed)

    for cnt in range(dataLength):
        theSum = 0
        for cnt1 in range(numberSamples):
            theSum += random.uniform(lowLim,highLim)
        data.append(theSum/numberSamples)
        
    return data
    #=========================================================================#
#Display the command-line arguments
print("The command-line arguments are: " , str(sys.argv))

#Create a list named args containing the command-line arguments
args = sys.argv[1].split(",")

#Populate variables that will be used to create four datasets.
xSeed = int(args[0])
xDataLength = int(args[1])
xNumberSamples = int(args[2])
xLowLim = int(args[3])
xHighLim = int(args[4])
print("xSeed =",xSeed)
print("xDataLength =",xDataLength)
print('xNumberSamples =',xNumberSamples)
print('xLowLim =',xLowLim)
print('xHighLim =',xHighLim)
print()

#Create four datasets using command-line argument values.
data01 = normalRandomGenerator(seed=xSeed,dataLength=xDataLength,\
       numberSamples=xNumberSamples,\
       lowLim=xLowLim,\
       highLim=xHighLim\
       )
data02 = normalRandomGenerator(seed=xSeed,dataLength=xDataLength,\
       numberSamples = 2*xNumberSamples,\
       lowLim=xLowLim,\
       highLim=xHighLim\
       )
       
data03 = normalRandomGenerator(seed=xSeed,dataLength=xDataLength,\
       numberSamples = 4*xNumberSamples,\
       lowLim=xLowLim,\
       highLim=xHighLim\
       )
       
data04 = normalRandomGenerator(seed=xSeed,dataLength=xDataLength,\
       numberSamples = 8*xNumberSamples,\
       lowLim=xLowLim,\
       highLim=xHighLim\
       )
       
       
print("Output from student code begins here.")
#Call the student's run method in the class named Runner in the 
#file named Proj04Runner.py, passing four datasets as parameters.
Runner.run(data01,data02,data03,data04)




