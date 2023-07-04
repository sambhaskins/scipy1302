import numpy as np
import matplotlib.pyplot as plt

"""
 This Python class Runner includes a function run which produces a 2x2 plot with each subplot representing a different 
 mathematical function. The four mathematical functions are:
 
 1. Sine function
 2. Damped cosine function
 3. Inverse exponential function (thanks for emailing this out!)
 4. Sine and Damped negative sine functions
 
 The grid is enabled for all subplots for better visualization of data points. Also, the title, x-label and y-label are
 set for each subplot. In the fourth subplot, a legend is also added, per the assignment specs. 
"""

class Runner:
    def run():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Setup 2x2 subplots with specific dimensions and edge styles
        fig, ax = plt.subplots(2, 2, figsize=(7, 5), facecolor='0.75', linewidth=10, edgecolor='Red')
        
        # Create a range of t values for the plots
        t = np.arange(0, 6.0, 0.025)
        # Unpack the 2D array into separate variables for easier access
        ax[0, 0], ax[0, 1], ax[1, 0], ax[1, 1] = ax.flatten()

        # Plot Sine function on the first subplot (upper left)
        ax[0, 0].set_title('A Sine')
        ax[0, 0].set_xlabel('This is an x label')
        ax[0, 0].set_ylabel('This is a y label')
        ax[0, 0].plot(t, np.sin(1.5 * np.pi * t)) 

        # Plot Damped cosine function on the second subplot (upper right)
        ax[0, 1].plot(t, np.exp(-t) * np.cos(5 * np.pi * t)) 
        ax[0, 1].set_xlim(0,1) 
        ax[0, 1].set_title('A damped cosine')
        ax[0, 1].set_xlabel('This is an x label')
        ax[0, 1].set_ylabel('This is a y label')

        # Plot Inverse exponential function on the third subplot (lower left)
        ax[1, 0].plot(t, 1.0 - np.exp(-t))
        ax[1, 0].set_title('An inverse exponential')
        ax[1, 0].set_xlabel('This is an x label')
        ax[1, 0].set_ylabel('This is a y label')

        # Plot Sine and Damped negative sine functions on the fourth subplot (lower right)
        ax[1, 1].plot(t, np.exp(-t) * np.sin(-2 * np.pi * t / 2), label='Damped Negative Sine') 
        ax[1, 1].plot(t, np.sin(2 * np.pi * t), label='Sine') 
        ax[1, 1].legend(loc='upper right', framealpha=0.3, facecolor='Green')
        ax[1, 1].set_title('Subplot with a legend')
        ax[1, 1].set_xlabel('This is an x label')
        ax[1, 1].set_ylabel('This is a y label')

        # Enable grid on all subplots, using a for loop
        for ax in [ax[0, 0], ax[0, 1], ax[ 1, 0], ax[1, 1]]:
            ax.grid(True)

        # Add layout optimization and my name
        fig.tight_layout()
        plt.suptitle('Sam Beers Haskins')

        # Render the plot
        plt.show()
