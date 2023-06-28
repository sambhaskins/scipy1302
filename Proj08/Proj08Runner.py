import matplotlib.pyplot as plt
import numpy as np

"""
This program will display a single plot with three different mathematical functions: a Damped Sine, an Exponential,
and a Sine function. The plot features custom annotations and a legend for each function, as well as a custom grid.
"""

class Runner:
    def run():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Setup single subplot with specific dimensions and edge styles
        fig, ax0 = plt.subplots(1, 1, facecolor='0.75')
        fig.patch.set_edgecolor('black') 
        fig.patch.set_linewidth(3)  

        # Create a range of t values for the plots
        t = np.arange(0, 6.0, 0.08)

        # Plot Damped Sine function
        damped_sine = np.exp(-t/2) * np.sin(np.pi*t)
        ax0.plot(t, damped_sine, 'go', label='Damped Sine')

        # Plot Exponential function, adjusted to skirt along the top of the damped sine
        exponential = np.exp(-t/2)
        ax0.plot(t, exponential, 'r-', label='Exponential')

        # Plot Sine function
        sine = np.sin(np.pi*t)
        ax0.plot(t, sine, 'b-+', label='Sine')

        # Legend + my first & last name on X-Axis and Y-Axis
        ax0.legend(loc='lower right', framealpha=0.3, facecolor='Green')
        ax0.set_ylabel('Sam')
        ax0.set_xlabel('Haskins')

        # Set the x and y axis limits
        plt.xlim(-.25, 6.25)
        plt.ylim(-1.15, 1.15)

        # Set the ticks on the x and y axis
        plt.xticks(np.arange(0, 7, 1))
        plt.yticks(np.arange(-1.00, 1.01, 0.25)) 

        ax0.grid(True)

        # Annotations
        ax0.annotate('Damped Sine', xy=[1.5, -.50], xytext=(-90, -50),
                    textcoords='offset points',arrowprops=dict(arrowstyle="->", 
                    connectionstyle="arc3,rad=0.2"))
        ax0.annotate('Exponential', xy=[1.49, .50], xytext=(-40, 50),
                    textcoords='offset points', arrowprops=dict(arrowstyle="->",
                    connectionstyle="arc3,rad=0.2"))
        ax0.annotate('Sine', xy=[4.1,.5], xytext=(-45, 10), 
                    textcoords='offset points', arrowprops=dict(arrowstyle="->",
                    connectionstyle="arc3,rad=0.2"))

        # Render plot
        plt.show()
