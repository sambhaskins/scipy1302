import random
from statistics import stdev, mean
import numpy as np
import matplotlib.pyplot as plt
import math


def normalRandomGenerator(seed=1, dataLength=10000, numberSamples=50, lowLim=0, highLim=100):
    """
    Generate random data from a normal distribution.

    Args:
        seed (int): Seed for the random number generator.
        dataLength (int): Length of the generated data.
        numberSamples (int): Number of samples used to compute the average at each step.
        lowLim (float): Lower limit of the uniform distribution.
        highLim (float): Upper limit of the uniform distribution.

    Returns:
        list: Randomly generated data from a normal distribution.

    """
    data = []
    np.random.seed(seed)

    for cnt in range(dataLength):
        theSum = 0
        for cnt1 in range(numberSamples):
            theSum += random.uniform(lowLim, highLim)
        data.append(theSum / numberSamples)

    return data


def other_data(seed, dataLength, numberSamples, lowLim, highLim):
    np.random.seed(seed)

    new_data = np.random.uniform(low=lowLim, high=highLim, size=(dataLength, numberSamples))
    new_avg = np.mean(new_data, axis=1)
    new_skew = np.sqrt(new_avg)
    return new_skew.tolist()


def lmsBestFitLine(xDataIn, yDataIn):
    """
    Compute the parameters of the best-fit line using the Least Mean Squares (LMS) method.

    Args:
        xDataIn (numpy.ndarray): Input data for the x-axis.
        yDataIn (numpy.ndarray): Input data for the y-axis.

    Returns:
        tuple: Slope (m) and intercept (b) of the best-fit line.

    """
    xBar = np.mean(xDataIn)
    yBar = np.mean(yDataIn)

    numerator = np.sum((xDataIn - xBar) * (yDataIn - yBar))
    denominator = np.sum((xDataIn - xBar) ** 2)

    m = numerator / denominator
    b = yBar - m * xBar

    return m, b


def standardNormalDistribution(x):
    """
    Compute the value of the standard normal distribution at a given point.

    Args:
        x (float): Input value.

    Returns:
        float: Value of the standard normal distribution at the given point.

    """
    eVal = 2.718281828459045
    exp = (-x ** 2) / 2
    numerator = pow(eVal, exp)
    denominator = math.sqrt(2 * math.pi)
    return numerator / denominator


def normalProbabilityDensity(x, mu=0, sigma=1.0):
    """
    Compute the value of the normal probability density function at a given point.

    Args:
        x (float): Input value.
        mu (float): Mean of the distribution. Default is 0.
        sigma (float): Standard deviation of the distribution. Default is 1.0.

    Returns:
        float: Value of the normal probability density function at the given point.

    """
    eVal = 2.718281828459045
    exp = -((x - mu) ** 2) / (2 * (sigma ** 2))
    numerator = pow(eVal, exp)
    denominator = sigma * (math.sqrt(2 * math.pi))
    return numerator / denominator


def cumulativeDistribution(x):
    # constants
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911

    # Save the sign of x
    sign = 1
    if x < 0:
        sign = -1
    x = abs(x) / math.sqrt(2.0)

    # A&S formula 7.1.26
    t = 1.0 / (1.0 + p * x)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * math.exp(-x * x)

    return 0.5 * (1.0 + sign * y)


print("I certify that this program is my own work and is not the work of others.")
print("I agree not to share my solution with others.")
print("Sam Beers Haskins")


class Runner:
    def run():
        """
        Run the program and generate the plots.

        """
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

        # Plot a box in the upper left quadrant
        ax[0, 0].plot([x1, x2], [y1, y2])
        ax[0, 0].scatter(xData, yData, c='red', s=50, edgecolor='blue')
        ax[0, 0].grid(True)

        # Create an array of uniformly spaced values, -3 sigma to +3 sigma
        x = np.arange(-3, 3, 0.1)
        # Create a list containing a distribution value for each value in x
        y = [standardNormalDistribution(val) for val in x]

        # Use plot in the upper right quadrant
        ax[0, 1].plot(x, y)
        ax[0, 1].grid(True)

        # Plot a positively skewed histogram in lower left quadrant
        data = other_data(seed=1, dataLength=2000, numberSamples=20, lowLim=0, highLim=2500)
        ax[1, 0].hist(data, bins=50)
        ax[1, 0].grid(True)

        # Plot a flipped histogram in the lower right quadrant
        x = np.arange(-3, 3, 0.1)
        y = [cumulativeDistribution(val) for val in x]

        # Use matplotlib to plot the data.
        ax[1, 1].plot(x, y)

        # Add title to the figure and show it
        fig.suptitle('Sam Beers Haskins')
        plt.tight_layout()
        plt.show()
