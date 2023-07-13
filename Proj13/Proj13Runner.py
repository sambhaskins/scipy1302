import matplotlib.pyplot as plt

"""
This program visualizes a set of test scores using a pie chart. Each slice of the pie represents the score 
on a particular test. Two of the tests are emphasized with "exploded" slices I've changed the radius, and
how much the slices will "explode" in order to make the chart more presentable - and to adhere to assignment
specs.
"""


class Runner:
    @staticmethod
    def run(tests, scores):
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Define which slices to "explode" for emphasis
        explodeSlices = (0, 0, 0, 0, 0.7, 0, 0.8)

        # Define the format for the percentage labels on each slice
        percentages = '%1.1f%%'

        # Create a new figure and a single subplot
        fig1, ax = plt.subplots()

        # Create the pie chart
        ax.pie(scores, explode=explodeSlices, labels=tests, autopct=percentages,
               shadow=True, startangle=90, radius=2.0)

        # Ensure that the pie chart is drawn as a circle, set title, and display
        ax.axis('equal')
        ax.set_title('Sam Beers Haskins')
        plt.show()
