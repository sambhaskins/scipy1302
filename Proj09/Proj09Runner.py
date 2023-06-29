import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


class Runner:
    def run():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        fig, ax0 = plt.subplots(1, 1,
                                facecolor='0.75',
                                linewidth=3,)

        t = np.arange(0, 6.0, 0.11)
        line0, = ax0.plot(t, 1 * np.exp(-t/2) * np.cos(np.pi*t - np.pi/2), color='red', linestyle='--')
        line1, = ax0.plot(t, np.cos(np.pi*t - np.pi/2), color='green', marker='o', linestyle='-.')

        ax0.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
        ax0.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
        ax0.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

        ax0.tick_params(axis='both', which='major', colors='black', width=2, length=10)
        ax0.tick_params(axis='both', which='minor', colors='black', width=2)

        ax0.grid(visible=True, which='major', color='green')
        ax0.grid(visible=True, which='minor', color='red',
                 linestyle='dotted', alpha=0.6)

        ax0.set_ylabel('Sam')
        ax0.set_xlabel('Haskins')
        ax0.grid(True)

        plt.show()


