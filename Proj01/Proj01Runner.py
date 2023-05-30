

import math


class mean:
    def __init__(self, dataset):
        self.dataset = dataset
        print("\nI certify that this program is my own work\n" +
              "and is not the work of others. I agree not\n" +
              "to share my solution with others.\n" +
              "Sam Haskins")

    def calculate(self):
        mean = sum(self.dataset) / len(self.dataset)

        return mean


class median:
    def __init__(self, dataset):
        self.dataset = dataset

    def calculate(self):
        sorted_nums = sorted(self.dataset)
        length = len(sorted_nums)
        mid = length // 2

        if length % 2 == 1:
            median = sorted_nums[mid]
        else:
            median = ((sorted_nums[mid - 1] + sorted_nums[mid]) / 2)

        return median


class stdev:
    def __init__(self, dataset):
        self.dataset = dataset

    def calculate(self):
        mean = sum(self.dataset) / len(self.dataset)
        square_diff_sum = sum((x - mean) ** 2 for x in self.dataset)
        variance = square_diff_sum / (len(self.dataset) - 1)
        stdev = math.sqrt(variance)

        return stdev

class pstdev:
    def __init__(self, dataset):
        self.dataset = dataset

    def calculate(self):
        mean = sum(self.dataset) / len(self.dataset)
        square_diff_sum = sum((x - mean) ** 2 for x in self.dataset)
        variance = square_diff_sum / (len(self.dataset))
        pstdev = math.sqrt(variance)

        return pstdev
