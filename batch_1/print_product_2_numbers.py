#create list for 2 user input
program = [int(input(f"Enter a number ({numbers+1}):  "))
           for numbers in range(2)]

#compute product logic
result = program[0] * program[1]

#print result
print(result)