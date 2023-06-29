import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

"""
This program displays a single plot with two mathematical functions. Both functions represent transformations 
of cosine with a phase shift so they start at 0,0. The first is a damped cosine and the second is a simple 
cosine. The plot features an adaptive grid with major and minor lines in different colors and styles, per the 
assignment requirements.
"""

class Runner:
    def run():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Setup plot
        fig, ax0 = plt.subplots(1, 1, facecolor='0.75', linewidth=3)

        # Create a range of t values for the plots
        t = np.arange(0, 6.0, 0.11)

        # Plot Damped Cosine function
        ax0.plot(t, 1 * np.exp(-t/2) * np.cos(np.pi*t - np.pi/2), color='red', linestyle='--')

        # Plot Cosine 
        ax0.plot(t, np.cos(np.pi*t - np.pi/2), color='green', marker='o', linestyle='-.')

        # Set the minor and major locators for x and y axis
        ax0.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
        ax0.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
        ax0.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

        # Configure tick parameters for both minor and major ticks
        ax0.tick_params(axis='both', which='major', colors='black', width=2, length=10)
        ax0.tick_params(axis='both', which='minor', colors='black', width=2)

        # Set grid to match assignment specs
        ax0.grid(visible=True, which='major', color='green')
        ax0.grid(visible=True, which='minor', color='red', linestyle='dotted', alpha=0.6)

        # First and last name on X and Y axis
        ax0.set_ylabel('Sam')
        ax0.set_xlabel('Haskins')

        ax0.grid(True)

        # Display the plot
        plt.show()
