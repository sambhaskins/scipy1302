import statistics
import matplotlib.pyplot as plt


class Runner:
    @staticmethod
    def run(data01):
        Q1 = statistics.quantiles(data01, n=4)[0]
        Q2 = statistics.median(data01)
        Q3 = statistics.quantiles(data01, n=4)[-1]
        IQR = Q3 - Q1
        LOL = Q1 - 1.5 * IQR
        UOL = Q3 + 1.5 * IQR
        MIN = min(data01)
        MAX = max(data01)

        data02 = data01[:len(data01) // 2]
        data03 = data02[::-1]
        data04 = [x * 0.75 for x in data01]

        # Calculate means and standard deviations
        topLeftMean = round(statistics.mean(data01), 3)
        bottomLeftMean = round(statistics.mean(data04), 3)
        topRightMean = 0.0
        bottomRightMean = round(statistics.mean(data01), 3)
        topLeftStd = round(statistics.stdev(data01), 3)
        bottomRightStd = round(statistics.stdev(data04), 3)

        # Create the histogram with four quadrants
        fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

        ax[0, 0].hist(data01, density=True, bins=50)
        ax[0, 0].set_title('Histogram')
        ax[0, 0].grid(True)
        ax[0, 0].set_ylabel('Relative Frequency')

        ax[0, 1].hist([x - topLeftMean for x in data01], density=True, bins=50)
        ax[0, 1].set_title('Histogram (Mean Reset to Zero)')
        ax[0, 1].grid(True)
        ax[0, 1].set_ylabel('Relative Frequency')

        ax[1, 0].hist(data03, density=True, bins=50)
        ax[1, 0].set_title('Histogram (Mirror Image)')
        ax[1, 0].set_xlabel('X')
        ax[1, 0].grid(True)

        ax[1, 1].hist(data04, density=True, bins=50)
        ax[1, 1].set_title('Histogram (75% Reduced Std Dev)')
        ax[1, 1].set_xlabel('X')
        ax[1, 1].grid(True)

        # Update the mean and standard deviation
        ax[0, 1].set_xlim(ax[0, 0].get_xlim())
        ax[1, 1].set_xlim(ax[0, 0].get_xlim())
        ax[1, 1].set_ylim(ax[0, 0].get_ylim())

        # Set x-axis tick values for all histograms
        for axs in ax.flat:
            axs.set_xticks(range(-100, 101, 100))

        return (Q1, Q2, Q3, IQR, LOL, UOL, MIN, MAX, ax, data02,
                data03, data04)
