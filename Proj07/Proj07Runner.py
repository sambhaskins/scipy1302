import matplotlib.pyplot as plt
import numpy as np


class Runner:
    def run():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Setup 2x2 subplots with specific dimensions and edge styles
        fig, ax = plt.subplots(2, 2, figsize=(
            7, 5), facecolor='0.75', linewidth=10, edgecolor='Green')
        
        # Unpack the 2D array into separate var iables for easier access
        t = np.arange(-3.0, 3.0, 0.05)

        ax[0, 0], ax[0, 1], ax[1, 0], ax[1, 1] = ax.flatten()

        # Sin plot
        ax[0, 0].plot(t, np.sin(t), label='A Sine')
        ax[0, 0].spines['left'].set_position('center')
        ax[0, 0].spines['bottom'].set_position('center')
        ax[0, 0].spines['right'].set_color('none')
        ax[0, 0].spines['top'].set_color('none')
        ax[0, 0].xaxis.set_ticks_position('bottom')
        ax[0, 0].yaxis.set_ticks_position('left')
        ax[0, 0].set_title('y = sin(t)')
        ax[0, 0].text(-2, 0.5, 'sin(t)', fontsize=12)
        ax[0, 0].legend()

        # 2 * Cos plot
        ax[0, 1].plot(t, 2 * np.cos(t), label='2*Cosine', color='orange')
        ax[0, 1].spines['left'].set_position('center')
        ax[0, 1].spines['bottom'].set_position('center')
        ax[0, 1].spines['right'].set_color('none')
        ax[0, 1].spines['top'].set_color('none')
        ax[0, 1].xaxis.set_ticks_position('bottom')
        ax[0, 1].yaxis.set_ticks_position('left')
        ax[0, 1].set_title('y = 2cos(t)')
        ax[0, 1].text(-2, 1, '2cos(t)', fontsize=12)
        ax[0, 1].legend()

        # -t^3 plot
        ax[1, 0].plot(t, -t**3, label='-t^3', color='green')
        ax[1, 0].spines['left'].set_position('center')
        ax[1, 0].spines['bottom'].set_position('center')
        ax[1, 0].spines['right'].set_color('none')
        ax[1, 0].spines['top'].set_color('none')
        ax[1, 0].xaxis.set_ticks_position('bottom')
        ax[1, 0].yaxis.set_ticks_position('left')
        ax[1, 0].set_title('y = -t^3')
        ax[1, 0].text(-2, 2, '-t^3', fontsize=12)
        ax[1, 0].legend()

        # 0.5 * t^2 plot
        ax[1, 1].plot(t, 0.5 * t**2, label='0.5t^2', color='red')
        ax[1, 1].spines['left'].set_position('center')
        ax[1, 1].spines['bottom'].set_position('center')
        ax[1, 1].spines['right'].set_color('none')
        ax[1, 1].spines['top'].set_color('none')
        ax[1, 1].xaxis.set_ticks_position('bottom')
        ax[1, 1].yaxis.set_ticks_position('left')
        ax[1, 1].set_title('y = 0.5t^2')
        ax[1, 1].text(-2, 1, '0.5t^2', fontsize=12)
        ax[1, 1].legend()

        # Improve the layout
        plt.tight_layout()
        plt.show()
