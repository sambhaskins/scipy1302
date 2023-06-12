import random
import numpy as np
import matplotlib.pyplot as plt


def normal_random_generator(seed=1, data_length=10000, number_samples=50, low_lim=0, high_lim=100):
    """
    generates a list of random numbers from a normal distribution
    """
    data = []
    np.random.seed(seed)

    for cnt in range(data_length):
        the_sum = 0
        for cnt1 in range(number_samples):
            the_sum += random.uniform(low_lim, high_lim)
        data.append(the_sum / number_samples)

    return data


def other_data():
    """
    generates additional, positively skewed data using a uniform distribution
    """
    new_data = np.random.gamma(8, scale=100, size=5000)
    data = new_data * 2000 / np.max(new_data)
    return data


def lms_best_fit_line(x_data_in, y_data_in):
    """
    calculates the best-fit line using the least mean squares (LMS) method
    """
    x_bar = np.mean(x_data_in)
    y_bar = np.mean(y_data_in)

    numerator = np.sum((x_data_in - x_bar) * (y_data_in - y_bar))
    denominator = np.sum((x_data_in - x_bar) ** 2)

    m = numerator / denominator
    b = y_bar - m * x_bar

    return m, b


def standard_normal_distribution(x):
    """
    calculates the value of the standard normal distribution at a given point
    """
    e_val = 2.718281828459045
    exp = (-x ** 2) / 2
    numerator = pow(e_val, exp)
    denominator = np.sqrt(2 * np.pi)
    return numerator / denominator


def normal_probability_density(x, mu=0, sigma=1.0):
    """
    calculates the value of the normal probability density function at a given point
    """
    e_val = 2.718281828459045
    exp = -((x - mu) ** 2) / (2 * (sigma ** 2))
    numerator = pow(e_val, exp)
    denominator = sigma * (np.sqrt(2 * np.pi))
    return numerator / denominator


def cumulative_distribution(x):
    """
    calculates the cumulative distribution function at a given point
    """
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911

    sign = 1
    if x < 0:
        sign = -1
    x = abs(x) / np.sqrt(2.0)

    t = 1.0 / (1.0 + p * x)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * np.exp(-x * x)

    return 0.5 * (1.0 + sign * y)


print("I certify that this program is my own work and not the work of others")
print("I agree not to share my solution with others")
print("Sam Beers Haskins")


class Runner:
    def run():
        """
        runs the main code for generating plots and visualizations
        """
        fig, ax = plt.subplots(2, 2)

        x_data = normal_random_generator(seed=1, data_length=100, number_samples=1, low_lim=0, high_lim=200)
        noise = normal_random_generator(seed=2, data_length=200, number_samples=1, low_lim=0, high_lim=10)

        y_data = []
        for cnt in range(len(x_data)):
            y_data.append(x_data[cnt] / 10 + noise[cnt])

        m, b = lms_best_fit_line(x_data, y_data)

        x1 = min(x_data)
        y1 = m * x1 + b
        x2 = max(x_data)
        y2 = m * x2 + b

        # plot in the upper left quadrant
        ax[0, 0].plot([x1, x2], [y1, y2])
        ax[0, 0].scatter(x_data, y_data, c='red', s=50, edgecolor='blue')
        ax[0, 0].grid(True)

        x = np.arange(-3, 3, 0.1)
        y = [standard_normal_distribution(val) for val in x]

        # plot in the upper right quadrant
        ax[0, 1].plot(x, y)
        ax[0, 1].grid(True)

        # plot in the lower left quadrant, using positively skewed data
        data = other_data()
        ax[1, 0].hist(data, bins=50)
        ax[1, 0].grid(True)

        x = np.arange(-3, 3, 0.1)
        y = [cumulative_distribution(val) for val in x]

        # plot in the lower right quadrant
        ax[1, 1].plot(x, y)

        fig.suptitle('Sam Beers Haskins')
        plt.tight_layout()
        plt.show()
