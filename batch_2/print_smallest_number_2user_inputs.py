#create list for 2 user input
program = [int(input(f"Enter number ({numbers+1}):  "))
           for numbers in range(2)]

#use built-in function min() to determine the smallest number from 2 user input
result = min(program)

#print result
print(result)