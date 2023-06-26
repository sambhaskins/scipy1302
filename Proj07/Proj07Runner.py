import matplotlib.pyplot as plt
import numpy as np

"""
This code will display a 2x2 plot with each subplot representing a different mathematical function.
We'll work on producing & graphing the following functions:

1. Sine function
2. 2*Cosine function
3. Negative cubic function
4. Half-square function

The code in this program covers lessons / exercises including Visualizations Chapter 2.
"""

class Runner:
    def run():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Setup 2x2 subplots with specific dimensions and edge styles
        fig,axes = plt.subplots(2,2, facecolor='0.75', linewidth=10, edgecolor='Green')
        
        # Create a range of t values for the plots
        t = np.arange(-3.0, 3.0, 0.05)
        
        # Unpack the 2D array into separate variables for easier access
        ax0, ax1, ax2, ax3 = axes.flatten()

        # Plot Sine function on the first subplot (upper left)
        ax0.spines['left'].set_position('center')
        ax0.spines['right'].set_color('none')
        ax0.spines['bottom'].set_position('center')
        ax0.spines['top'].set_color('none')
        ax0.set_xticks(np.arange(-2,3,2))
        ax0.text(-3,0.5,'$Sine$')
        ax0.plot(t,np.sin(1*np.pi*t))

        # Plot 2*Cosine function on the second subplot (upper right)
        ax1.spines['left'].set_position('center')
        ax1.spines['right'].set_color('none')
        ax1.spines['bottom'].set_position('center')
        ax1.spines['top'].set_color('none')
        ax1.set_xticks(np.arange(-2,3,2))
        ax1.text(-3,1,'$2*Cosine$')
        ax1.plot(t, 2*np.cos(0.5*np.pi*t))

        # Plot Negative cubic function on the third subplot (lower left)
        ax2.plot(t, -t**3, label='')
        ax2.spines['left'].set_position('center')
        ax2.spines['bottom'].set_position('center')
        ax2.spines['right'].set_color('none')
        ax2.spines['top'].set_color('none')
        ax2.xaxis.set_ticks_position('bottom')
        ax2.yaxis.set_ticks_position('left')
        ax2.text(.5, 8, '$y=-x^3$')

        # Plot Half-square function on the fourth subplot (lower right)
        ax3.plot(t, 0.5 * t**2)
        ax3.spines['left'].set_position('center')
        ax3.spines['bottom'].set_position('center')
        ax3.spines['right'].set_color('none')
        ax3.spines['top'].set_color('none')
        ax3.xaxis.set_ticks_position('bottom')
        ax3.yaxis.set_ticks_position('left')
        ax3.text(0.25, 3.5, '$y=0.5*x^2$')
        ax3.set_ylim(-4.5,4.5)

        # Render plot & display my name in bottom left corner
        plt.figtext(0.1,0.02,'Sam Beers Haskins')
        plt.show()
