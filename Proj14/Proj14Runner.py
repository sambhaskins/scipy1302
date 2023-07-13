import numpy as np


class Runner:
    @staticmethod
    def certify():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

    def run(list_args, array_2d):
        """
        This function takes a list and a 2D array as input. It returns a new list and 2D array, where 
        the new list is the original list duplicated and the 2D array is the original array with each 
        element multiplied by 2.
        """
        # Duplicates the list_args
        r1 = list_args * 2

        # Mulitiply each element in the array by 2
        r2 = array_2d * 2

        # Return the new list and array
        return r1, r2
