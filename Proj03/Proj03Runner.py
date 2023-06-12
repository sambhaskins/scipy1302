import random
import numpy as np
import matplotlib.pyplot as plt


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


class Runner:
    def run():
        # Create a figure with two rows and two columns.
        fig, ax = plt.subplots(2, 2)

        xData = normalRandomGenerator(seed=1, dataLength=100, numberSamples=1, lowLim=0, highLim=150)
        noise = normalRandomGenerator(seed=2, dataLength=200, numberSamples=1, lowLim=0, highLim=10)

        yData = []
        for cnt in range(len(xData)):
            yData.append(xData[cnt] / 10 + noise[cnt])

        # Compute and draw the best fit line
        m, b = lmsBestFitLine(xData, yData)

        # Draw a best fit line
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

        # Plot a violin plot in the upper right quadrant
        ax[0, 1].violinplot(xData, vert=False, positions=[0.5])
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


# Run the code
Runner.run()
