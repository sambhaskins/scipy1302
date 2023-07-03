import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from statistics import median
from statistics import stdev
import math

class Runner:

    @staticmethod
    def run(g01, g02, g03):
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")


        # Create a figure with three rows and three columns
        fig, axes = plt.subplots(3, 3, figsize=(6, 4), sharex=True)

        # Call the histBoxAndViolin function to process the first dataset
        Runner.histBoxAndViolin(g01, axes, axesRow=0, multiDim=True,
                         vFacecolor='red',  # violin facecolor
                         vEdgecolor='black',  # violin edgecolor
                         vAlpha=0.5  # violin transparency
                         )

        # Process the second dataset
        Runner.histBoxAndViolin(g02, axes, axesRow=1, multiDim=True,
                         vAlpha=0.5
                         )

        # Process the third dataset
        Runner.histBoxAndViolin(g03, axes, axesRow=2, multiDim=True,
                         vFacecolor='green',
                         vEdgecolor='red',
                         vAlpha=0.5,
                         vMedianLineStyle='dotted'  # violin median line style
                         )

        axes[0, 0].grid(True)
        axes[0, 1].grid(True)
        axes[0, 2].grid(True)
        axes[1, 0].grid(True)
        axes[1, 1].grid(True)
        axes[1, 2].grid(True)
        axes[2, 0].grid(True)
        axes[2, 1].grid(True)
        axes[2, 2].grid(True)

        plt.tight_layout()
        plt.show()



    @staticmethod
    def normalProbabilityDensity(x, mu=0, sigma=1.0):
            eVal = 2.718281828459045
            exp = -((x - mu) ** 2) / (2 * (sigma ** 2))
            numerator = pow(eVal, exp)
            denominator = sigma * (math.sqrt(2 * math.pi))
            return numerator / denominator

    @staticmethod
    def histBoxAndViolin(data, axes, axesRow=0, multiDim=False,
                         showmeans=None,
                         showmedians=True,
                         meanline=None,
                         showbox=None,
                         showcaps=None,
                         notch=None,
                         bootstrap=None,
                         showfliers=None,
                         sym=None,
                         widths=0.5,
                         showextrema=True,
                         boxprops=None,
                         flierprops=None,
                         medianprops=None,
                         meanprops=None,
                         capprops=None,
                         whiskerprops=None,
                         vFacecolor=None,
                         vEdgecolor=None,
                         vAlpha=None,
                         vMedianLineStyle='solid'
                         ):
        dataBar = mean(data)
        dataStd = stdev(data)

        if multiDim == True:
            ax0 = axes[axesRow, 0]
            ax1 = axes[axesRow, 1]
            ax2 = axes[axesRow, 2]
        else:
            ax0 = axes[0]
            ax1 = axes[1]
            ax2 = axes[2]

        # Plot and label histogram
        dataN, dataBins, dataPat = ax0.hist(
            data, bins=136, density=True, range=(min(data), max(data)))
        ax0.set_title('Histogram')
        ax0.set_xlabel('x')
        ax0.set_ylabel('Relative Freq')

        # Compute the values for a normal probability density curve for the
        # data mu and sigma across the same range of values.
        x = np.arange(dataBins[0], dataBins[len(dataBins) - 1], 0.1)
        y = [Runner.normalProbabilityDensity(
            val, mu=dataBar, sigma=dataStd) for val in x]
        # Superimpose the normal probability density curve on the histogram.
        ax0.plot(x, y, label='normal probability density')

        # Plot a boxplot
        ax1.boxplot(data,
                    vert=False,
                    showmeans=showmeans,
                    meanline=meanline,
                    showbox=showbox,
                    showcaps=showcaps,
                    notch=notch,
                    bootstrap=bootstrap,
                    showfliers=showfliers,
                    sym=sym,
                    widths=widths,
                    boxprops=boxprops,
                    flierprops=flierprops,
                    medianprops=medianprops,
                    meanprops=meanprops,
                    capprops=capprops,
                    whiskerprops=whiskerprops
                    )
        ax1.set_title('Box and Whisker Plot')
        ax1.set_xlabel('x')

        # Plot a violin plot
        parts = ax2.violinplot(data,
                               vert=False,
                               showmeans=showmeans,
                               showmedians=showmedians,
                               widths=widths,
                               showextrema=showextrema)

        # Set custom properties on the violin plot.
        for pc in parts['bodies']:
            pc.set_facecolor(vFacecolor)
            pc.set_edgecolor(vEdgecolor)
            pc.set_alpha(vAlpha)

        parts['cmedians'].set_linestyles(vMedianLineStyle)

        ax2.set_title('Violin Plot')
        ax2.set_xlabel('x')