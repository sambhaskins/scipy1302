
#File: Proj01Rnner.txt

import math
#You may not import any libraries other than math
'''
The following is a Python class named mean that calculates the mean 
of a dataset.

The class has two methods:

    __init__(self, dataset): This is the constructor method. It is called 
    when an object of this class is created. It takes one parameter, 
    'dataset', which is the data that the mean will be calculated from. 
    It assigns this dataset to the instance variable self.dataset.

    calculate(self): This method calculates the mean of the dataset. 
    It takes no parameters, but it uses the dataset that was passed to 
    the constructor and stored in self.dataset. The result is the mean 
    of the dataset and returned.

This class is used in the driver script in the file named Proj01.py, 
where m = mean(random_dataset) creates an object of the class 
and m.calculate() calls the calculate method on the object, 
returning the mean of the dataset.
'''
class mean:
    def __init__(self, dataset):
        self.dataset = dataset
        print("\nI certify that this program is my own work\n" +
              "and is not the work of others. I agree not\n" +
              "to share my solution with others.\n" +
              "Sam Haskins")

    def calculate(self):
        mean = sum
# Insert code to calculate and return the mean of the dataset.

class median:
    def __init__(self, dataset):
        self.dataset = dataset

    def calculate(self):
# Insert code to calculate and return the median of the dataset.

class stdev:
    def __init__(self, dataset):
        self.dataset = dataset

    def calculate(self):
# Insert code to calculate and return the sample standard deviation
# of the dataset.

class pstdev:
    def __init__(self, dataset):
        self.dataset = dataset

    def calculate(self):
# Insert code to calculate and return the population standard 
# deviation of the dataset.