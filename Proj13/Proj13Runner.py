import numpy as np
import matplotlib.pyplot as plt


class Runner:
    @staticmethod
    def run(tests, scores):
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        tests = 'Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5', 'Game 6', 'Game 7'
        scores = [78, 34, 48, 20, 62, 37, 29]  # points scored during each game
        explodeSlices = (0.2, 0, 0, 0.3, 0, 0, 0)  # explode largest and smallest
        percentages = '%1.1f%%'  # show percentage of each slice

        fig1, ax = plt.subplots()
        ax.pie(points, explode=explodeSlices, labels=games, autopct=percentages,
               shadow=True, startangle=90)
        ax.axis('equal')  # ensure that pie is drawn as a circle.
        ax.set_title('Comparison of scores by game for Alex')
        plt.show()
