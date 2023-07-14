#DO NOT MODIFY THE CODE IN THIS FILE
#File: Proj15.py
#Rev 12/05/22
'''
This assignment requires the student to write a program
demonstrating knowledge of the material covered under 
"Multiplication by a scalar" in the Study Guide
as well as material leading up to that topic.

Revised 02/19/23 to terminate with an error message
if the user fails to enter one command-line
argument. 
'''

import numpy as np
from Proj15Runner import Runner
import sys

# Check if the user has entered one command-line argument
if len(sys.argv) != 2 or len(sys.argv[1].split(',')) != 1:
    print("Error: You must enter exactly one command-line")
    print("argument.")
    sys.exit()

#Call the student's certify function
Runner.certify()

print('Command-line arg: ',sys.argv[1])

#Get the command-line argument and save it
multiplier = int(sys.argv[1])

#Call the student's function named run passing one list and
#one two-dimensional array as parameters.
r1,r2 = Runner.run(multiplier,[1,2,3],
                   np.array([[0,1,2],
                             [3,4,5]]))

print('NOTE: Your instructor will grade your assignment')
print('using a command-line argument with a different value.') 
print()
print("Output from student's run function begins here.")
print()

print('r1 =',r1)
print()
print('r2 type =',type(r2))

print('r2 shape=',r2.shape)
print('r2 contents =\n',r2)




