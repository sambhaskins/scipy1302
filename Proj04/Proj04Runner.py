import matplotlib.pyplot as plt
import numpy as np
from statistics import mean, stdev
from matplotlib.ticker import FormatStrFormatter


class Runner:
    def run(data01, data02, data03, data04):
        # Create a 2x2 figure containing four plots with shaorange x and y tick marks and labels.
        fig, ax = plt.subplots(2, 2, sharey=True, sharex=True)

        # Plot data01
        cnt, bins, _ = ax[0, 0].hist(
            data01,
            bins=50,
            density=True,
            range=(min(data01), max(data01))
        )
        data_mean = mean(data01)
        data_std = stdev(data01)
        x = np.linspace(min(data01), max(data01), 100)
        y = (1 / (data_std * np.sqrt(2 * np.pi))) * \
            np.exp(-(x - data_mean)**2 / (2 * data_std**2))
        line, = ax[0, 0].plot(x, y, color='orange', marker='.', markevery=10)
        ax[0, 0].legend([line], ['norm prob density'], loc='upper left')
        ax[0, 0].grid(True)
        ax[0, 0].set_title('Upper Left')
        ax[0, 0].set_ylabel('Relative Frequency')
        ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter('%.3f'))



        # Plot data02
        cnt, bins, _ = ax[0, 1].hist(
            data02,
            bins=50,
            density=True,
            range=(min(data02), max(data02))
        )
        data_mean = mean(data02)
        data_std = stdev(data02)
        x = np.linspace(min(data02), max(data02), 100)
        y = (1 / (data_std * np.sqrt(2 * np.pi))) * \
            np.exp(-(x - data_mean)**2 / (2 * data_std**2))
        line, = ax[0, 1].plot(x, y, color='orange', marker='.', markevery=5)
        ax[0, 1].legend([line], ['norm prob density'], loc='upper left')
        ax[0, 1].plot(x, y, color='orange')
        ax[0, 1].grid(True)
        ax[0, 1].set_title('Upper Right')
        ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter('%.3f'))


        # Plot data03
        cnt, bins, _ = ax[1, 0].hist(
            data03,
            bins=50,
            density=True,
            range=(min(data03), max(data03))
        )
        data_mean = mean(data03)
        data_std = stdev(data03)
        x = np.linspace(min(data03), max(data03), 100)
        y = (1 / (data_std * np.sqrt(2 * np.pi))) * \
            np.exp(-(x - data_mean)**2 / (2 * data_std**2))
        line, = ax[1, 0].plot(x, y, color='orange', marker='.', markevery=3)
        ax[1, 0].legend([line], ['norm prob density'], loc='upper left')
        ax[1, 0].grid(True)
        ax[1, 0].set_title('Lower Left')
        ax[1, 0].set_xlabel('x')
        ax[1, 0].set_ylabel('Relative Frequency')
        ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter('%.3f'))


        # Plot data04
        cnt, bins, _ = ax[1, 1].hist(
            data04,
            bins=50,
            density=True,
            range=(min(data04), max(data04))
        )
        data_mean = mean(data04)
        data_std = stdev(data04)
        x = np.linspace(min(data04), max(data04), 100)
        y = (1 / (data_std * np.sqrt(2 * np.pi))) * \
            np.exp(-(x - data_mean)**2 / (2 * data_std**2))
        line, = ax[1, 1].plot(x, y, color='orange', marker='.', markevery=2)
        ax[1, 1].legend([line], ['norm prob density'], loc='lower left')
        ax[1, 1].grid(True)
        ax[1, 1].set_title('Lower Right')
        ax[1, 1].set_xlabel('x')
        ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter('%.3f'))


        # Display the number of bins in all histograms
        num_bins = len(bins) - 1

        # Display the number of all bins in all histograms
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")
        print()
        print(f"Number of bins in all histograms = {num_bins}")

        # Display a title at the top
        plt.suptitle("Sam Beers Haskins")

        # Cause the plot to become visible
        plt.tight_layout()
        plt.show()
