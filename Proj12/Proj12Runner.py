import numpy as np
import matplotlib.pyplot as plt

class Runner:
    @staticmethod
    def run(names, test01, test02, test03):
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        names = []
        xPosition = range(1, 6)

        fig, ax = plt.subplots(1, 1)
        ax.bar(xPosition, test01, label="Test 1")
        ax.bar(xPosition, test02, label="Test 2", tick_label=names)
        ax.bar(xPosition, test03, label="Test 3")
        ax.set_xlabel('Player Name')
        ax.set_ylabel('Player Scores')
        ax.set_title('Player Score Comparison')

        ax.grid()
        plt.legend(loc='lower left')
        plt.show()
