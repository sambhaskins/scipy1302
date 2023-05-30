#DO NOT MODIFY THE CODE IN THIS FILE
#File: Proj02.py
#Revised: 04/23/23
'''
Among other things, this project requires you to 
demonstrate a basic knowledge of frequency 
distributions and histograms. In this project,
you will write code to create a frequency
distribution chart that emulates a histogram for a
given dataset without access to special libraries.

You will not be required to write the code to produce
the chart. You simply need to write the code to
produce the data that will be used by the following
code to produce the chart.
'''

from Proj02Runner import Runner
import sys

# Check if the user has entered three command-line arguments
if len(sys.argv) != 2 or len(sys.argv[1].split(',')) != 3:
    print("Error: You must enter exactly three command-line")
    print("arguments in the format 'a,b,c'.")
    sys.exit()

#Get the command-line arguments and put them in a
#list named args.
args = sys.argv[1].split(",")

#Use the command-line arguments to create a dataset.
data=list(range(0,11))+list(
    range(1,10))+list(
    range(2,9))+list(
    range(3,8))+list(
    range(4,7))+list(
    range(5,6))+list(
    range(int(args[0]),int(args[1])))*int(args[2])
print("The dataset is:")
print(data)
print("Your code may not import anything.")
print("The command-line arguments are: " , str(sys.argv))
print()
print("Execute student code.")

#Call student's run function to process the dataset
#and return the result.
result = Runner.run(data)
print("\nDisplay data returned by student code.")


#Use the list returned from student's run function to
#display a frequency distribution chart.
#Find the maximum value in the result
max_value = max(result)

# Loop through each row
for i in range(max_value, 0, -1):
    # Loop through each value in the result
    for j in range(len(result)):
        if result[j] >= i:
            print(" x ", end="")
        else:
            print("   ", end="")
    print()

# Print the x-axis labels
for i in range(len(result)):
    print("---", end="")
print()

#Print the list returned by the student's run function.
print(result)
