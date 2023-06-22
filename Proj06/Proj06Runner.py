import numpy as np
import matplotlib.pyplot as plt

class Runner:
    @staticmethod
    def run():
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        fig,axes = plt.subplots(2,2,
                        figsize=(7,5),
                        facecolor='0.75',
                        linewidth=10,
                        edgecolor='Red')

        t = np.arange(0, 6.0, 0.025) 
        ax0, ax1, ax2, ax3 = axes.flatten()

        ax0.plot(t, np.sin(1.5 * np.pi * t)) 
        ax0.set_title('A Sine')
        ax0.set_xlabel('This is an x label')
        ax0.set_ylabel('This is a y label')

        ax1.plot(t, np.exp(-t) * np.cos(5 * np.pi * t)) 
        ax1.set_xlim(0,1) 
        ax1.set_title('A damped cosine')
        ax1.set_xlabel('This is an x label')
        ax1.set_ylabel('This is a y label')

        ax2.plot(t, 1.0 - np.exp(-t))
        ax2.set_title('An inverse exponential')
        ax2.set_xlabel('This is an x label')
        ax2.set_ylabel('This is a y label')

        ax3.plot(t, np.exp(-t) * np.sin(-2 * np.pi * t / 2), label='Damped Negative Sine') 
        ax3.plot(t, np.sin(2 * np.pi * t), label='Sine') 
        ax3.legend(loc='upper right', framealpha=0.3, facecolor='Green')
        ax3.set_title('Subplot with a legend')
        ax3.set_xlabel('This is an x label')
        ax3.set_ylabel('This is a y label')

        for ax in [ax0, ax1, ax2, ax3]:
            ax.grid(True)

        fig.tight_layout()
        plt.suptitle('Sam Beers Haskins')
        plt.show()

