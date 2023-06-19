import statistics
import matplotlib.pyplot as plt

class Runner:
    @staticmethod
    def run(data01):
        data01.sort()

        Q2 = statistics.median(data01)
        topHalf = [x for x in data01 if x >= Q2]
        bottomHalf = [x for x in data01 if x < Q2]

        # Get the median for each half
        Q3 = statistics.median(topHalf)
        Q1 = statistics.median(bottomHalf)
        IQR = Q3 - Q1
        lowerOutlierLimit = Q1 - 1.5*IQR
        upperOutlierLimit = Q3 + 1.5*IQR

        MIN = min(data01)
        MAX = max(data01)

        data02 = [x - statistics.mean(data01) for x in data01]
        data03 = [2*statistics.mean(data01) - x for x in data01]
        data04 = [x * 0.75 for x in data01]

        # Create the histogram with four quadrants
        fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

        ax[0, 0].hist(data01, density=True, bins=50)
        ax[0, 0].set_title('Histogram')
        ax[0, 0].grid(True)
        ax[0, 0].set_ylabel('Relative Frequency')

        ax[0, 1].hist(data02, density=True, bins=50)
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

        # Set x-axis tick values for all histograms
        for axs in ax.flat:
            axs.set_xticks(range(-100, 101, 100))

        return (Q1,Q2,Q3,IQR,lowerOutlierLimit,upperOutlierLimit,MIN,MAX,ax,data02,
        data03,data04)