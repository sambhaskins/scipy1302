
import math
import sys
import statistics
from Proj01Runner import mean, median #stdev, pstdev

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

# sd = stdev(random_dataset)
# calculated_stdev = sd.calculate()
# correct_stdev = statistics.stdev(random_dataset)
# if math.isclose(calculated_stdev, correct_stdev, rel_tol=1e-9):
#     print('\nsample standard deviation okay',calculated_stdev)
# else:
#     print('\nOOPS: sample standard deviation not okay')
#     print(calculated_stdev,"was calculated")
#     print(correct_stdev,"is correct")

# psd = pstdev(random_dataset)
# calculated_pstdev = psd.calculate()
# correct_pstdev = statistics.pstdev(random_dataset)
# if math.isclose(calculated_pstdev, correct_pstdev, rel_tol=1e-9):
#     print('\npopulation standard deviation okay',calculated_pstdev)
# else:
#     print('\nOOPS: population standard deviation not okay')
#     print(calculated_pstdev,"was calculated")
#     print(correct_pstdev,"is correct")

