import numpy as np
import random
import matplotlib.pyplot as plt


def normalRandomGenerator(seed=1, dataLength=10000, numberSamples=50, lowLim=0, highLim=100):
    dataset = []
    random.seed(seed)

    for nums in range(dataLength):
        samples = [random.uniform(lowLim, highLim) for _ in range(numberSamples)]
        avg = sum(samples) / numberSamples
        dataset.append(avg)

    return dataset


print("I certify this program is my own work and is not the work of others.")
print("I agree not to share my solution with others.")
print("Sam Haskins")


class Runner():
    def run():
        # Create a figure with two rows and two columns.
        fig, ax = plt.subplots(2, 2)

        # Create a dataset
        data = normalRandomGenerator(
            dataLength=10001,
            numberSamples=4,
            lowLim=0,
            highLim=400)

        # Plot histogram in upper left quadrant
        ax[0, 0].hist(data, bins=50, density=True)
        ax[0, 0].grid(True)
        ax[0, 0].set_title('Histogram')

        # Plot a box plot in lower left quadrant
        ax[1, 0].boxplot(data, vert=False)
        ax[1, 0].grid(True)
        ax[1, 0].set_title('Box Plot')

        # Plot a violin plot in the upper right quadrant
        ax[0, 1].violinplot(data, vert=False, positions=[0.5])
        ax[0, 1].grid(True)
        ax[0, 1].set_title('Violin Plot')

        # Plot a flipped histogram in the lower right quadrant
        mean = np.mean(data)
        centered_data = data - mean
        flipped_data = -centered_data
        flipped_data += mean
        ax[1, 1].hist(flipped_data, bins=50, density=True)
        ax[1, 1].grid(True)
        ax[1, 1].set_title('Flipped Histogram')

        # Add title to the figure and show it
        plt.suptitle('Sam Beers Haskins')
        plt.tight_layout()
        plt.show()

    # end run function
# end class Runner
