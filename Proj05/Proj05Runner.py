import statistics
import matplotlib.pyplot as plt

class Runner:
    def run(data01):
        # Print a certification statement
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")
        
        # Sort data in ascending order
        data01.sort()

        # Calculate the median of the data set
        Q2 = round(statistics.median(data01), 3)
        # Split the data set into two halves based on the median
        topHalf = [x for x in data01 if x >= Q2]
        bottomHalf = [x for x in data01 if x < Q2]

        # Calculate the median for each half (Q1 and Q3)
        Q3 = round(statistics.median(topHalf), 3)
        Q1 = round(statistics.median(bottomHalf), 3)
        # Calculate interquartile range (IQR)
        IQR = round(Q3 - Q1, 3)
        # Calculate the outlier limits
        LOL = round(Q1 - 1.5*IQR, 3)
        UOL = round(Q3 + 1.5*IQR, 3)

        # Calculate the minimum and maximum of the data set
        MIN = round(min(data01), 3)
        MAX = round(max(data01), 3)

        # Calculate mean and standard deviation of the data set
        original_mean = round(statistics.mean(data01), 3)
        original_stdev = round(statistics.stdev(data01), 3)

        # Apply transformations to create new data sets
        data02 = [round(x - original_mean, 3) for x in data01]   # Shift mean to zero
        data03 = [round(-x, 3) for x in data02]                  # Mirror image of data02
        data04 = [round((x - original_mean) * 0.75 + 100, 3) for x in data01] # Shift mean and scale standard deviation

        # Create a figure with four subplots (2x2)
        fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

        # Create histogram for each data set
        ax[0, 0].hist(data01, density=True, bins=50)  # Original data
        ax[0, 1].hist(data02, density=True, bins=50)  # Mean-shifted data
        ax[1, 0].hist(data03, density=True, bins=50)  # Mirror image of data02
        ax[1, 1].hist(data04, density=True, bins=50)  # Scaled and shifted data

        # Label the subplots
        ax[0, 0].set_title('Histogram')
        ax[0, 0].set_ylabel('Relative Frequency')
        ax[0, 1].set_title('Histogram (Mean Reset to Zero)')
        ax[1, 0].set_title('Histogram (Mirror Image)')
        ax[1, 0].set_xlabel('X')
        ax[1, 0].set_ylabel('Relative Frequency')
        ax[1, 1].set_title('Histogram (75% Reduced Std Dev)')
        ax[1, 1].set_xlabel('X')

        # Set grid for all subplots
        for axs in ax.flat:
            axs.grid(True)
            axs.set_xticks(range(-100, 101, 100))

        # Set a super title for all subplots
        plt.suptitle("Sam Beers Haskins")

        # Return quartile values, outlier limits, min, max and the transformed data sets
        return (Q1,Q2,Q3,IQR,LOL,UOL,MIN,MAX,ax,data02,data03,data04)
