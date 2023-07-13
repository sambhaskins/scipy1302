# DO NOT MODIFY THE CODE IN THIS FILE
# File: Proj14.py
# Rev 12/06/22
'''
This assignment requires the student to write a program
demonstrating knowledge of the material covered under 
"Addition of multi-dimensional arrays" in the Study Guide
as well as material leading up to that topic.

Revised 02/19/23 to terminate with an error message
if the user fails to enter nine command-line
arguments in the format 1,2,3,4,5,6,7,8,9 
'''
import numpy as np
from Proj14Runner import Runner
import sys

# Check if the user has entered nine command-line arguments
if len(sys.argv) != 2 or len(sys.argv[1].split(',')) != 9:
    print("Error: You must enter exactly nine command-line")
    print("arguments in the format '1,2,3,4,5,6,7,8,9.")
    sys.exit()

# Get the command-line arguments and put them in a
# list named args.
args = sys.argv[1].split(",")

# Call the student's function named certify.
Runner.certify()

print('Command-line args: ', sys.argv[1])

# Call the student's function named run passing one list and
# one two-dimensional array as parameters.
r1, r2 = Runner.run([int(args[0]), int(args[1]), int(args[2])],
                    np.array([[int(args[3]), int(args[4]), int(args[5])],
                              [int(args[6]), int(args[7]), int(args[8])]]))

print('NOTE: Your instructor will grade your assignment')
print('using command-line arguments having different values.')
print()
print("Output from student's run function begins here.")
print()

print('r1 =', r1)
print()
print('r2 type =', type(r2))

print('r2 shape=', r2.shape)
print('r2 contents =\n', r2)
