import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

class Runner:
    def run():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        fig,ax0 = plt.subplots(1,1)

        t = np.arange(0, 6.0, 0.11)
        ax0.plot(t, np.exp(-t/2) * np.cos(np.pi*t),'-.',
                            t, np.cos(np.pi*t),'--o')

        ax0.set_ylabel('This is a ylabel')
        ax0.set_xlabel('This is an xlabel')

        ax0.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
        ax0.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))

        ax0.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
        ax0.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

        ax0.tick_params(axis='both',which='minor',length=5)
        ax0.tick_params(axis='both',which='major',length=10,
                        labelcolor='blue',width=2)

        ax0.grid(b=True, which='major', color='cyan')
        ax0.grid(b=True, which='minor', color='blue',
                linestyle='dotted',alpha=0.6)

        plt.show()