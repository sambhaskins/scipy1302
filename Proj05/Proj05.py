#DO NOT MODIFY THE CODE IN THIS FILE
#File: Proj05.py
#Rev 06/11/23
'''
Among other things, this project requires that you write code
 to demonstrate your knowledge of:
How to compute quartiles and the interquartile range
How to determine if a value is an outlier
How to manipulate the mean and the standard deviation of a dataset
'''

from Proj05Runner import Runner
import sys
import random
from statistics import mean
from statistics import stdev
import matplotlib.pyplot as plt
import numpy as np

# Check if the user has entered three command-line arguments
if len(sys.argv) != 2 or len(sys.argv[1].split(',')) != 3:
    print("Error: You must enter exactly three command-line")
    print("arguments in the format '1,2,3'.")
    sys.exit()

#Display the command-line arguments
print("The command-line arguments are: \n",str(sys.argv))
#Put the command-line arguments in a list named args
args = sys.argv[1].split(",")

#Prepare and print variables that will be used to create 
#a dataset based on command-line arguments.
theMean = int(args[0])
theStd_dev = int(args[1])
theNumberSamples = int(args[2])
print('theMean =',theMean)
print('theStd_dev =',theStd_dev)
print('theNumberSamples =',theNumberSamples)
print()

# Generate an approximately normal or Gaussian dataset
np.random.seed(1)
data01 = list(np.random.normal(theMean, theStd_dev, 
          theNumberSamples))

#Disable the following code to test your code against an 
#approximately Gaussian dataset.
#Update the dataset to make it bimodal
data01 += list(np.random.normal(int(theMean/4), 
          theStd_dev, int(theNumberSamples/4)))

print("Output from student code begins here.")
#Call the student's run method in a class named Runner in
# the student's file named Proj05Runner passing the dataset 
# as a parameter. 

#The student's code must return the following values in the 
# correct order for the #dataset received by the student's code:
'''
Q1 (lower quartile)
Q2 (middle quartile)
Q3 (upper quartile)
IQR (Interquartile range)
LOL lowerOutlierLimit
UOL upperOutlierLimit
MIN minimum value
MAX maximum value
'''
#In addition, the student's code must return the following
#in the correct order:
'''
ax The figure that is to be displayed on the screen
data02 The dataset shown in the upper-right quadrant
data03 The datsset shown in the lower-left quadrant
data04 The dataset shown in the lower-right quadrant
'''

#Call the student code and save the return values.
Q1,Q2,Q3,IQR,LOL,UOL,MIN,MAX,ax,data02,\
  data03,data04 = Runner.run(data01)

print("\nReturn to code in the driver script.")
print("using values returned from student's code.\n")
print("Q1 (lower quartile) =",round(Q1,3))
print("Q2 (middle quartile) =",round(Q2,3))
print("Q3 (upper quartile) =",round(Q3,3))
print("IQR (Interquartile range) =",round(IQR,3))
print("lowerOutlierLimit =",round(LOL,3))
print("upperOutlierLimit",round(UOL,3))
print("min =",MIN)
print("max =",MAX)
print("\nComparison of the histogram on top left with \n"
      "the other histograms.")


topLeftMean = round(mean(data01),3)
bottomLeftMean = round(mean(data03),3)
topRightMean = round(mean(data02),3)
bottomRightMean = round(mean(data04),3)
topLeftStd = round(stdev(data01),3)
bottomRightStd = round(stdev(data04),3)

print("Mean of top left =",topLeftMean)
print("Mean of bottom left =",bottomLeftMean)
print("Mean of top right =",topRightMean)
print("Mean of bottom right =",bottomRightMean)
print()

print("Standard deviation of top left =",topLeftStd)
print("Standard deviation of bottom right =",bottomRightStd)
print("Standard deviation ratio =",round(bottomRightStd/topLeftStd,2))


#DO NOT include plt.show() in your code. Instead, return your figure
#as shown above in the call to your run method.

#Display the graph created and returned by the student's code.
plt.tight_layout()
plt.show()





