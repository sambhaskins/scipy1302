import numpy as np
import matplotlib.pyplot as plt
from statistics import mean, stdev

"""
This program visualizes two sets of data across six different subplots, using histograms and box & whisker plots. 
Customizations are applied to each subplot based on the data it represents, and according to assignment specs. 
"""

class Runner:
    @staticmethod
    def run(g04, g05):

        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Initialize a 3x2 grid of subplots
        fig, axes = plt.subplots(3, 2, figsize=(6, 5))

        # Process the first dataset in the first two rows
        Runner.plotHistAndBox(g04, axes, axesRow=0, showfliers=False)
        Runner.plotHistAndBox(g04, axes, axesRow=1, showcaps=False)

        # Process the second dataset in the third row
        Runner.plotHistAndBox(g05, axes, axesRow=2, notch=True)

        # Enable grid for all subplots
        for ax in axes.flatten():
            ax.grid(True)

        # Adjust layout and display the plot
        plt.tight_layout()
        plt.show()

    @staticmethod
    def normalProbabilityDensity(x, mu=0, sigma=1.0):

        exp = -((x - mu) ** 2) / (2 * sigma ** 2)
        numerator = np.exp(exp)
        denominator = sigma * np.sqrt(2 * np.pi)
        return numerator / denominator

    @staticmethod
    def plotHistAndBox(data, axes, axesRow=0, multiDim=False,
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

        # Calculate mean and standard deviation of the data
        dataBar = mean(data)
        dataStd = stdev(data)

        # Adjust x-axis ticks based on which row of subplots is being populated
        if axesRow == 0:
            axes[axesRow, 0].set_xticks([50, 100])
            axes[axesRow, 1].set_xticks([25, 50, 75])
        elif axesRow == 1:
            axes[axesRow, 0].set_xticks([50, 100])
            axes[axesRow, 1].set_xticks([50, 100])
        elif axesRow == 2:
            axes[axesRow, 0].set_xticks([20, 40, 60, 80, 100])
            axes[axesRow, 1].set_xticks([20, 40, 60, 80, 100])


        if multiDim == True:
            # Plot and label histogram
            dataN, dataBins, dataPat = axes[axesRow, 0].hist(
                data, bins=136, density=True)
            axes[axesRow, 0].set_title('data')
            axes[axesRow, 0].set_xlabel('Sam')
            axes[axesRow, 0].set_ylabel('Relative Freq')

            # Plot a boxplot
            axes[axesRow, 1].boxplot(data, vert=False, widths=0.75,
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
            axes[axesRow, 1].set_title('Box & Whisker Plot')
            axes[axesRow, 1].set_xlabel('Haskins')

        else:
            # Plot and label histogram
            dataN, dataBins, dataPat = axes[axesRow, 0].hist(
                data, bins=136, density=True, range=(min(data), max(data)))
            axes[axesRow, 0].set_title('data')
            axes[axesRow, 0].set_xlabel('Sam')
            axes[axesRow, 0].set_ylabel('Relative Freq')

            # Plot a boxplot
            axes[axesRow, 1].boxplot(data, vert=False, widths=0.75,
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
            axes[axesRow, 1].set_title('Box & Whisker Plot')
            axes[axesRow, 1].set_xlabel('Haskins')

        # Compute the values for a normal probability density curve for the
        # data mu and sigma across the same range of values.
        x = np.linspace(min(data), max(data), 100)  # Change here: create an array of evenly spaced values
        y = [Runner.normalProbabilityDensity(val, mu=dataBar, sigma=dataStd) for val in x]

        # Compute the values for a normal probability density curve
        x = np.linspace(min(data), max(data), 100)
        y = [Runner.normalProbabilityDensity(val, mu=dataBar, sigma=dataStd) for val in x]

        # Superimpose the normal probability density curve on the histogram
        axes[axesRow, 0].plot(x, y, label='normal probability density', color='orange')
