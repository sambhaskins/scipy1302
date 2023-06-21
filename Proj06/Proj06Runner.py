import numpy as np
import matplotlib.pyplot as plt


class Runner:
    @staticmethod
    def run():
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        fig, axes = plt.subplots(2, 2,
                                 figsize=(7, 5),
                                 facecolor='0.75',
                                 linewidth=10,
                                 edgecolor='Red')

        t = np.arange(0, 6.0, 0.05)
        ax0, ax1, ax2, ax3 = axes.flatten()

        ax0.plot(t, np.sin(5 * t))
        ax1.plot(t, np.exp(-t) * np.cos(4 * np.pi * t))
        ax2.plot(t, 1.0 - np.exp(-t))

        ax3.plot(t, np.exp(-t) * np.cos(4 * np.pi * t), label='Damped cosine')
        ax3.plot(t, np.cos(4 * np.pi * t), label='Cosine')
        ax3.legend(loc='upper right', framealpha=0.3, facecolor='Green')
        ax3.set_title('Subplot with a legend')

        ax0.grid(True)
        ax1.grid(True)
        ax2.grid(True)
        ax3.grid(True)

        fig.tight_layout()
        plt.show()
