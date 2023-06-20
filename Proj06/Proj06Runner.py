import numpy as np
import matplotlib.pyplot as plt
import random

class Runner:

    def __init__(self, seed=1, data_length=10000, number_samples=50, low_lim=0, high_lim=100):
        self.seed = seed
        self.data_length = data_length
        self.number_samples = number_samples
        self.low_lim = low_lim
        self.high_lim = high_lim

    def normal_random_generator(self):
        """
        generates a list of random numbers from a normal distribution
        """
        data = []
        np.random.seed(self.seed)

        for cnt in range(self.data_length):
            the_sum = 0
            for cnt1 in range(self.number_samples):
                the_sum += random.uniform(self.low_lim, self.high_lim)
            data.append(the_sum / self.number_samples)

        return data

    def run(self):
        # Generate data
        x = np.linspace(0, 10, self.data_length)
        y1 = np.sin(self.normal_random_generator())
        y2 = np.cos(self.normal_random_generator()) * np.exp(-np.array(self.normal_random_generator())/3)
        y3 = np.exp(-np.array(self.normal_random_generator()))
        y4 = np.sin(self.normal_random_generator())
        y5 = -np.cos(self.normal_random_generator()) * np.exp(-np.array(self.normal_random_generator())/3)

        # Create a figure
        fig, axs = plt.subplots(2, 2, figsize=(10, 10))

        # Flatten axes for convenient access
        axs = axs.flatten()

        # Plot y1 (sine function)
        axs[0].plot(x, y1, label='sin(x)')
        axs[0].set_title('Sine function')
        axs[0].set_xlabel('x')
        axs[0].set_ylabel('y')
        axs[0].grid(True)

        # Plot y2 (damped cosine function)
        axs[1].plot(x, y2, label='cos(x) * exp(-x/3)')
        axs[1].set_title('Damped Cosine function')
        axs[1].set_xlabel('x')
        axs[1].set_ylabel('y')
        axs[1].grid(True)

        # Plot y3 (inverse exponential function)
        axs[2].plot(x, y3, label='exp(-x)')
        axs[2].set_title('Inverse Exponential function')
        axs[2].set_xlabel('x')
        axs[2].set_ylabel('y')
        axs[2].grid(True)

        # Plot y4 and y5 (sine function and damped negative cosine function)
        axs[3].plot(x, y4, label='sin(x)')
        axs[3].plot(x, y5, label='-cos(x) * exp(-x/3)')
        axs[3].set_title('Sine function and Damped negative cosine function')
        axs[3].set_xlabel('x')
        axs[3].set_ylabel('y')
        axs[3].grid(True)
        axs[3].legend()

        # Set a display limit on the horizontal axis of a subplot
        axs[2].set_xlim(0, 5)

        # Set a title on the figure
        fig.suptitle('Subplots of different functions')

        # Show the figure
        plt.show()