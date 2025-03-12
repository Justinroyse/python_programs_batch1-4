#import math module to access math.trunc to remove decimals
import math
#create list for 2 user input
program = [int(input(f"Enter number ({numbers+1}):  "))
           for numbers in range(2)]
#compute quotient and use math.trunc
result = math.trunc(program[0]/program[1])
#print result
print(result)