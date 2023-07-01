import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from statistics import median
from statistics import stdev
import math


class Runner:
    def run(g04, g05):
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        fig,axes = plt.subplots(3,2,figsize=(4,4))

        #Process the second dataset
        Runner.plotHistAndBox(g04,axes,axesRow=1,multiDim=True)
                    
        #Process the third dataset
        Runner.plotHistAndBox(g05,axes,axesRow=2,multiDim=True)


        axes[0,0].grid(True)
        axes[0,1].grid(True)
        axes[1,0].grid(True)
        axes[1,1].grid(True)
        axes[2,0].grid(True)
        axes[2,1].grid(True)

        plt.tight_layout()
        plt.show()
    
    def normalProbabilityDensity(x,mu=0,sigma=1.0):
        eVal = 2.718281828459045
        exp = -((x-mu)**2)/(2*(sigma**2))
        numerator = pow(eVal,exp)
        denominator = sigma*(math.sqrt(2*math.pi))
        return numerator/denominator

    def plotHistAndBox(data,axes,axesRow=0,multiDim=False,
                showmeans=None,
                meanline=None,
                showbox=None, 
                showcaps=None,
                notch=None, 
                bootstrap=None,
                showfliers=None,
                sym=None,
                boxprops=None,
                flierprops=None, 
                medianprops=None, 
                meanprops=None, 
                capprops=None, 
                whiskerprops=None
                ):

        dataBar = mean(data)
        dataStd = stdev(data)

        if multiDim == True:
            #Plot and label histogram
            dataN,dataBins,dataPat = axes[axesRow,0].hist(
                data,bins=136,density=True)
            axes[axesRow,0].set_title('data')
            axes[axesRow,0].set_xlabel('x')
            axes[axesRow,0].set_ylabel('Relative Freq')

            #Plot a boxplot
            axes[axesRow,1].boxplot(data,vert=False,widths=0.75,
                                showmeans=showmeans,
                                meanline=meanline,
                                showbox=showbox, 
                                showcaps=showcaps,
                                notch=notch, 
                                bootstrap=bootstrap,
                                showfliers=showfliers,
                                sym=sym,
                                boxprops=boxprops,
                                flierprops=flierprops, 
                                medianprops=medianprops, 
                                meanprops=meanprops, 
                                capprops=capprops, 
                                whiskerprops=whiskerprops
                                )
            axes[axesRow,1].set_title('Box and Whisker Plot')
            axes[axesRow,1].set_xlabel('x')
            
        else:
            #Plot and label histogram
            dataN,dataBins,dataPat = axes[0].hist(
                data,bins=136,density=True,range=(min(data),max(data)))
            axes[0].set_title('data')
            axes[0].set_xlabel('x')
            axes[0].set_ylabel('Relative Freq')

            #Plot a boxplot
            axes[1].boxplot(data,vert=False,widths=0.75,
                        showmeans=showmeans,
                        meanline=meanline,
                        showbox=showbox, 
                        showcaps=showcaps,
                        notch=notch, 
                        bootstrap=bootstrap,
                        showfliers=showfliers,
                        sym=sym,
                        boxprops=boxprops,
                        flierprops=flierprops, 
                        medianprops=medianprops, 
                        meanprops=meanprops, 
                        capprops=capprops, 
                        whiskerprops=whiskerprops
                        )
            axes[1].set_title('Box and Whisker Plot')
            axes[1].set_xlabel('x')

        #Compute the values for a normal probability density curve for the 
        # data mu and sigma across the same range of values.
        x = np.arange(dataBins[136],dataBins[len(dataBins)-1],0.1)
        y = [Runner.normalProbabilityDensity(
            val,mu=dataBar,sigma=dataStd) for val in x]

        #Superimpose the normal probability density curve on the histogram.
        if multiDim == True:
            axes[axesRow,0].plot(x,y,label='normal probability density')
        else:
            axes[0].plot(x,y,label='normal probability density')

