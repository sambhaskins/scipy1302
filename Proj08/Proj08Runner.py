import matplotlib.pyplot as plt
import numpy as np

class Runner:
    def run():
        fig, ax0 = plt.subplots(1, 1, facecolor='0.75')
        fig.patch.set_edgecolor('black')  # Set the edge color
        fig.patch.set_linewidth(3)  # Set the line width

        t = np.arange(0, 6.0, 0.11)

        # Damped Sine
        damped_sine = np.exp(-t/2) * np.sin(np.pi*t)
        ax0.plot(t, damped_sine, 'go', label='Damped Sine')

        # Exponential, adjusted to skirt along the top of the damped sine
        exponential = np.exp(-t/2)
        ax0.plot(t, exponential, 'r-', label='Exponential')

        # Sine
        sine = np.sin(np.pi*t)
        ax0.plot(t, sine, 'b-', label='Sine')  # Draw line
        ax0.plot(t, sine, 'b+')  # Add vertical ticks

        ax0.legend(loc='lower right', framealpha=0.3, facecolor='Green')
        ax0.set_ylabel('Sam')
        ax0.set_xlabel('Haskins')

        # Set the x and y axis limits
        plt.xlim(-.25, 6.25)
        plt.ylim(-1.15, 1.15)  # Extend the range of y-axis

        # Set the ticks on the x and y axis
        plt.xticks(np.arange(0, 7, 1))
        plt.yticks(np.arange(-1.00, 1.01, 0.25))  # Adjust the y-ticks to match the new y-axis limit

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

        plt.show()

