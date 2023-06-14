from statistics import mean, stdev
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

"""
 We'll use and repurpose the normal_probability_function from the textbook. I changed the function to follow 
 the snake_case naming convention, out of personal preference. This function wil be used to calculate the normal
 probability density of our dataset(s). I have used np.linspace() to generate evenly spaced points to plot the 
 normal probability density line.Furthermore, I have set the `num` value to 1000, to generate more points, 
 hopefully creating more precision. I used `markevery` to plot the datapoints in respect to the required output
   in Figure 2.
"""


def normal_probability_density(x, mu=0, sigma=2.0):
    e_val = 2.718281828459045
    exp = -((x - mu) ** 2) / (2 * (sigma ** 2))
    numerator = pow(e_val, exp)
    denominator = sigma * (np.sqrt(2 * np.pi))
    return numerator / denominator


class Runner:
    def run(data_01, data_02, data_03, data_04):
        # Make a 2x2 figure containing four plots with shared x and y tick marks and labels
        fig, ax = plt.subplots(2, 2, sharey=True, sharex=True)

        # Plot first batch of data in upper left quadrant
        cnt, bins, _ = ax[0, 0].hist(
            data_01,
            bins=50,
            density=True,
            range=(min(data_01), max(data_01))
        )
        data_mean = mean(data_01)
        data_std = stdev(data_01)
        x = np.linspace(min(data_01), max(data_01), num=1000)
        y = normal_probability_density(x, data_mean, data_std)
        line, = ax[0, 0].plot(x, y, color='orange', marker='.', markevery=100)
        ax[0, 0].legend([line], ['norm prob density'], loc='upper left')
        ax[0, 0].grid(True)
        ax[0, 0].set_title('Upper Left')
        ax[0, 0].set_ylabel('Relative Frequency')

        # Plot second batch of data in upper right quadrant
        cnt, bins, _ = ax[0, 1].hist(
            data_02,
            bins=50,
            density=True,
            range=(min(data_02), max(data_02))
        )
        data_mean = mean(data_02)
        data_std = stdev(data_02)
        x = np.linspace(min(data_02), max(data_02), num=1000)
        y = normal_probability_density(x, data_mean, data_std)
        line, = ax[0, 1].plot(x, y, color='orange', marker='.', markevery=50)
        ax[0, 1].legend([line], ['norm prob density'], loc='upper left')
        ax[0, 1].grid(True)
        ax[0, 1].set_title('Upper Right')

        # Plot third batch of data in lower left quadrant
        cnt, bins, _ = ax[1, 0].hist(
            data_03,
            bins=50,
            density=True,
            range=(min(data_03), max(data_03))
        )
        data_mean = mean(data_03)
        data_std = stdev(data_03)
        x = np.linspace(min(data_03), max(data_03), num=1000)
        y = normal_probability_density(x, data_mean, data_std)
        line, = ax[1, 0].plot(x, y, color='orange', marker='.', markevery=25)
        ax[1, 0].legend([line], ['norm prob density'], loc='upper left')
        ax[1, 0].grid(True)
        ax[1, 0].set_title('Lower Left')
        ax[1, 0].set_xlabel('x')
        ax[1, 0].set_ylabel('Relative Frequency')

        # Plot the fourth and final batch of data in the lower left quadrant
        cnt, bins, _ = ax[1, 1].hist(
            data_04,
            bins=50,
            density=True,
            range=(min(data_04), max(data_04))
        )
        data_mean = mean(data_04)
        data_std = stdev(data_04)
        x = np.linspace(min(data_04), max(data_04), num=1000)
        y = normal_probability_density(x, data_mean, data_std)
        line, = ax[1, 1].plot(x, y, color='orange', marker='.', markevery=20)
        ax[1, 1].legend([line], ['norm prob density'], loc='lower left')
        ax[1, 1].grid(True)
        ax[1, 1].set_title('Lower Right')
        ax[1, 1].set_xlabel('x')

        # Display the number of bins across all histograms, subract one to account for the bin edges
        num_bins = len(bins) - 1

        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")
        print()
        print(f"Number of bins in all histograms = {num_bins}")

        # Display a title at top of output window
        plt.suptitle("Sam Beers Haskins")

        # Display plots
        plt.tight_layout()
        plt.show()
