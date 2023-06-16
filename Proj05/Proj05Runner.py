import sys
import numpy as np
from statistics import mean, stdev
import matplotlib.pyplot as plt


class Runner:
    @staticmethod
    def run(data01):
        Q1 = np.percentile(data01, 25)
        Q2 = np.percentile(data01, 50)
        Q3 = np.percentile(data01, 75)
        IQR = Q3 - Q1
        LOL = Q1 - 1.5 * IQR
        UOL = Q3 + 1.5 * IQR
        MIN = min(data01)
        MAX = max(data01)

        data02 = data01[:len(data01) // 2]
        data03 = data01[len(data01) // 2:]
        data04 = data01

        # Calculate means and standard deviations
        topLeftMean = round(mean(data01), 3)
        bottomLeftMean = round(mean(data03), 3)
        topRightMean = round(mean(data02), 3)
        bottomRightMean = round(mean(data04), 3)
        topLeftStd = round(stdev(data01), 3)
        bottomRightStd = round(stdev(data04), 3)

        # Create the histogram with four quadrants
        fig, axs = plt.subplots(2, 2, figsize=(10, 8))

        axs[0, 0].hist(data01, bins='auto', color='skyblue')
        axs[0, 0].set_title('Top Left Quadrant')

        axs[0, 1].hist(data02, bins='auto', color='lightgreen')
        axs[0, 1].set_title('Top Right Quadrant')

        axs[1, 0].hist(data03, bins='auto', color='lightcoral')
        axs[1, 0].set_title('Bottom Left Quadrant')

        axs[1, 1].hist(data04, bins='auto', color='gold')
        axs[1, 1].set_title('Bottom Right Quadrant')

        return Q1, Q2, Q3, IQR, LOL, UOL, MIN, MAX, axs, data02, \
            data03, data04
