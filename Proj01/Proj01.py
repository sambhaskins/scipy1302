'''
This script is a test for a set of functions that calculate 
the mean, median, standard deviation, and population standard 
deviation of a dataset. The script takes command-line arguments 
as the dataset and converts them to integers.

    import sys: This imports the built-in Python module 'sys' 
    which provides access to variables and functions related 
    to the Python interpreter.
    
    import statistics: This imports the built-in Python module 
    'statistics' which provides mathematical statistics functions.
    
    from Proj01Runner import mean, median, stdev, pstdev: This 
    imports the functions mean, median, stdev, and pstdev from 
    the module Proj01Runner.

An explanation for each line of code follows:

    random_dataset = list(map(int, sys.argv[1:])): This takes the 
    command-line arguments and converts them to integers and stores 
    them in a list called random_dataset.
    
    print("random_dataset",random_dataset): This line prints the dataset.
    
    m = mean(random_dataset): This calls the function mean from the 
    Proj01Runner module and passes the random_dataset list as an argument.
    This could also be interpreted as creating an object of the class
    named mean and passing the random_dataset list to the constructor 
    where it will be saved for use by the method named calculate.
    
    calculated_mean = m.calculate(): This calls the calculate method 
    on the object returned by the mean function (constructor).
    
    correct_mean = statistics.mean(random_dataset): This calls the 
    built-in mean function from the statistics module and passes 
    the random_dataset list as an argument.
    
    if calculated_mean == correct_mean:: This compares the calculated 
    mean with the correct mean from the statistics module.
    
    print('mean okay',calculated_mean): If the means match, this line 
    is executed and prints that the mean is okay and the calculated mean.
    
    else:: If the means do not match, the else block is executed.
    
    print('OOPS: mean'): This prints an error message.
    print(calculated_mean,"was calculated"): This prints the calculated mean.
    print(correct_mean,"is correct"): This prints the correct mean.

The script then proceeds to repeat the same process for median, 
standard deviation, and population standard deviation, using the 
corresponding functions and methods from the Proj01Runner module 
and the statistics module.
'''
import math
import sys
import statistics
from Proj01Runner import mean, median, stdev, pstdev

try:
    # Try to retrieve command-line arguments and convert them to int
    random_dataset = list(map(int, sys.argv[1:]))

    # Check if there are at least two arguments
    if len(random_dataset) < 2:
        raise ValueError("Error: At least two command-line arguments are required.")

except ValueError as error:
    # Catch any ValueError that might occur while converting the arguments to int
    print(error)
    sys.exit()

print("random_dataset", random_dataset)



m = mean(random_dataset)
calculated_mean = m.calculate()
correct_mean = statistics.mean(random_dataset)
if math.isclose(calculated_mean, correct_mean, rel_tol=1e-9):
    print('\nmean okay',calculated_mean)
else:
    print('\nOOPS: mean not okay')
    print(calculated_mean,"was calculated")
    print(correct_mean,"is correct")

me = median(random_dataset)
calculated_median = me.calculate()
correct_median = statistics.median(random_dataset)
if math.isclose(calculated_median, correct_median, rel_tol=1e-9):
    print('\nmedian okay',calculated_median)
else:
    print('\nOOPS: median not okay')
    print(calculated_median,"was calculated")
    print(correct_median,"is correct")

sd = stdev(random_dataset)
calculated_stdev = sd.calculate()
correct_stdev = statistics.stdev(random_dataset)
if math.isclose(calculated_stdev, correct_stdev, rel_tol=1e-9):
    print('\nsample standard deviation okay',calculated_stdev)
else:
    print('\nOOPS: sample standard deviation not okay')
    print(calculated_stdev,"was calculated")
    print(correct_stdev,"is correct")

psd = pstdev(random_dataset)
calculated_pstdev = psd.calculate()
correct_pstdev = statistics.pstdev(random_dataset)
if math.isclose(calculated_pstdev, correct_pstdev, rel_tol=1e-9):
    print('\npopulation standard deviation okay',calculated_pstdev)
else:
    print('\nOOPS: population standard deviation not okay')
    print(calculated_pstdev,"was calculated")
    print(correct_pstdev,"is correct")

