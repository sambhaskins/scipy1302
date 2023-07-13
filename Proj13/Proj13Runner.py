import numpy as np
import matplotlib.pyplot as plt


class Runner:
    @staticmethod
    def run(scores):
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        tests = 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7'
        explodeSlices = (0, 0, 0, 0, 0.3, 0, 0.2)  # explode largest and smallest
        percentages = '%1.1f%%'  # show percentage of each slice

        fig1, ax = plt.subplots()
        ax.pie(scores, explode=explodeSlices, labels=tests, autopct=percentages,
               shadow=True, startangle=90)
        ax.axis('equal')  # ensure that pie is drawn as a circle.
        ax.set_title('Sam Beers Haskins')
        plt.show()
