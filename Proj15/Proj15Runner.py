import numpy as np

class Runner:
    @staticmethod
    def certify():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")


    def run(multiplier, list1, array1):
        '''
        Multiplies every element in list1 and array1 by the given multiplier.
        Returns two objects:
            - A list resulting from the multiplication of list1,
            - A numpy array resulting from the multiplication of array1.
        '''
        # Apply the multiplier to every element in the list
        result_list = [multiplier * x for x in list1]

        # Apply the multiplier to every element in the array
        result_array = array1 * multiplier

        return result_list, result_array