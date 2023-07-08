import numpy as np
import matplotlib.pyplot as plt

"""
This program visualizes three sets of test data (scores of three different tests for a group of students)
using a bar chart. Each bar represents a student's score in a particular test, and these are grouped by student.
"""

class Runner:
    @staticmethod
    def run(names, test01, test02, test03):

        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Set bar width
        barWidth = 0.2

        # Set position of bar on X axis
        # Here, the positions of the bars are computed relative to the bars of the previous test
        r1 = np.arange(len(test01))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        # Create a new figure and a single subplot
        fig, ax = plt.subplots(1, 1)

        # Plot the bars for each test
        ax.bar(r1, test01, width = barWidth, label="Test 1")
        ax.bar(r2, test02, width = barWidth, label="Test 2")
        ax.bar(r3, test03, width = barWidth, label="Test 3")

        # Set the names of students as the x-ticks labels
        ax.set_xticks([r + barWidth for r in range(len(test01))])
        ax.set_xticklabels(names)

        # Set the labels and display my name as the title
        ax.set_xlabel('Student Name')
        ax.set_ylabel('Student Scores')
        ax.set_title('Sam Beers Haskins')
        ax.grid()

        # Add the legend to the plot
        plt.legend(loc='upper right')

        # Display the plot
        plt.show()


