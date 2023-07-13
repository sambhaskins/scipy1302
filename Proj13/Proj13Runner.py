import matplotlib.pyplot as plt

"""
This program visualizes a set of test scores using a pie chart. Each slice of the pie represents the score 
for a particular test. Two of the tests are emphasized with "exploded" slices.
"""


class Runner:
    @staticmethod
    def run(scores):
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

        # Define the labels for each test
        tests = 'Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'Test 6', 'Test 7'

        # Define which slices to "explode" for emphasis
        explodeSlices = (0, 0, 0, 0, 0.3, 0, 0.3)

        # Define the format for the percentage labels on each slice
        percentages = '%1.1f%%'

        # Create a new figure and a single subplot
        fig1, ax = plt.subplots()

        # Create the pie chart
        ax.pie(scores, explode=explodeSlices, labels=tests, autopct=percentages,
               shadow=True, startangle=90)

        # Ensure that the pie chart is drawn as a circle (i.e., the aspect ratio is equal)
        ax.axis('equal')

        # Set the title of the pie chart
        ax.set_title('Sam Beers Haskins')

        # Display the pie chart
        plt.show()
