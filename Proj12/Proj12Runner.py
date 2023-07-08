import numpy as np
import matplotlib.pyplot as plt

class Runner:
    @staticmethod
    def run(names, test01, test02, test03):
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Width of a bar
        barWidth = 0.2

        # Set position of bar on X axis
        r1 = np.arange(len(test01))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        fig, ax = plt.subplots(1, 1)
        ax.bar(r1, test01, width = barWidth, label="Test 1")
        ax.bar(r2, test02, width = barWidth, label="Test 2")
        ax.bar(r3, test03, width = barWidth, label="Test 3")

        # Adding xticks
        ax.set_xticks([r + barWidth for r in range(len(test01))], names)

        ax.set_xlabel('Student Name')
        ax.set_ylabel('Student Scores')
        ax.set_title('Sam Beers Haskins')

        ax.grid()
        plt.legend(loc='upper right')
        plt.show()


