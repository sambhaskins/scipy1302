import random
import numpy as np
import matplotlib.pyplot as plt
import math


def normalRandomGenerator(seed=1, dataLength=10000, numberSamples=50, lowLim=0, highLim=100):
    data = []
    random.seed(seed)

    for cnt in range(dataLength):
        theSum = 0
        for cnt1 in range(numberSamples):
            theSum += random.uniform(lowLim, highLim)
            data.append(theSum / numberSamples)

    return data


def lmsBestFitLine(xDataIn, yDataIn):
    xBar = np.mean(xDataIn)
    yBar = np.mean(yDataIn)

    numerator = np.sum((xDataIn - xBar) * (yDataIn - yBar))
    denominator = np.sum((xDataIn - xBar) ** 2)

    m = numerator / denominator
    b = yBar - m * xBar

    return m, b


def standardNormalDistribution(x):
    eVal = 2.718281828459045
    exp = (-x ** 2) / 2
    numerator = pow(eVal, exp)
    denominator = math.sqrt(2 * math.pi)
    return numerator / denominator


class Runner:
    def run():
        # Create a figure with two rows and two columns.
        fig, ax = plt.subplots(2, 2)

        xData = normalRandomGenerator(seed=1, dataLength=100, numberSamples=1, lowLim=0, highLim=200)
        noise = normalRandomGenerator(seed=2, dataLength=200, numberSamples=1, lowLim=0, highLim=10)

        yData = []
        for cnt in range(len(xData)):
            yData.append(xData[cnt] / 10 + noise[cnt])

        m, b = lmsBestFitLine(xData, yData)

        x1 = min(xData)
        y1 = m * x1 + b
        x2 = max(xData)
        y2 = m * x2 + b
        ax[0, 0].plot([x1, x2], [y1, y2])
        ax[0, 0].scatter(xData, yData, c='red', s=50, edgecolor='blue')
        ax[0, 0].grid(True)

        # Plot a box plot in lower left quadrant
        ax[1, 0].boxplot(xData, vert=False)
        ax[1, 0].grid(True)

        # Create an array of uniformly spaced values
        x = np.arange(-3, 3, 0.1)
        # Create a list containing a distribution value for each value in x
        # using list comprehension.
        y = [standardNormalDistribution(val) for val in x]

        # Use matplotlib to plot the data.
        ax[0, 1].plot(x, y)
        ax[0, 1].grid(True)

        # Plot a flipped histogram in the lower right quadrant
        mean = np.mean(xData)
        centered_data = xData - mean
        flipped_data = -centered_data
        flipped_data += mean
        ax[1, 1].hist(flipped_data, bins=50, density=True)
        ax[1, 1].grid(True)

        # Add title to the figure and show it
        fig.suptitle('Sam Beers Haskins')
        plt.tight_layout()
        plt.show()

        print("I certify that this program is my own work and is not the work of others.")
        print("I agree not to share my solution with others.")
        print("Sam Beers Haskins")
