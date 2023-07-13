import numpy as np


class Runner:
    @staticmethod
    def certify():
        # Certification
        print("I certify that this program is my own work and not the work of others")
        print("I agree not to share my solution with others")
        print("Sam Beers Haskins")

    def run(list_args, array_2d):
        r1 = list_args * 2
        r2 = array_2d + list_args
        return r1, r2
