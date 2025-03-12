#create list input for 2 user input
program = [int(input(f"Enter number ({numbers+1}):  "))
           for numbers in range(2)]

#compute remainder of 2 user inputs
result = program[0] % program[1]

#print result
print(result)