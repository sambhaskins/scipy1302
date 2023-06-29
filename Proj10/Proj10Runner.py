import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
from statistics import median
from statistics import stdev
import math
import Proj10 as p10


class Runner:
    def normalProbabilityDensity(x,mu=0,sigma=1.0):
        
        eVal = 2.718281828459045
        exp = -((x-mu)**2)/(2*(sigma**2))
        numerator = pow(eVal,exp)
        denominator = sigma*(math.sqrt(2*math.pi))
        return numerator/denominator

    def run():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        #Create three datasets with different spreads and with outliers.
        g01 = p10.normalRandomGenerator(dataLength=99,numberSamples=1,
                                    lowLim=10,highLim=70,seed=2) + [68.5] + [80] + [90]
        g02 = p10.normalRandomGenerator(dataLength=9999,numberSamples=2,
                                    lowLim=10,highLim=70,seed=2) + [68.5] + [80] + [90]
        g03 = p10.normalRandomGenerator(dataLength=9999,numberSamples=4,
                                    lowLim=10,highLim=70,seed=2) + [68.5] + [80] + [90]

        #Create a figure with three rows and two columns
        fig,axes = plt.subplots(3,2,figsize=(4,4))

        #Call the plotHistAndBox function to process the first dataset
        plotHistAndBox(g01,axes,axesRow=0,multiDim=True)

        #Process the second dataset
        plotHistAndBox(g02,axes,axesRow=1,multiDim=True)
                    
        #Process the third dataset
        plotHistAndBox(g03,axes,axesRow=2,multiDim=True)


        axes[0,0].grid(True)
        axes[0,1].grid(True)
        axes[1,0].grid(True)
        axes[1,1].grid(True)
        axes[2,0].grid(True)
        axes[2,1].grid(True)

        plt.tight_layout()
        plt.show()

    