#create list for 2 user input
program = [int(input(f"Enter number ({number+1}):  "))
           for number in range(2)]

#compute logic for difference of two number by referencing the list
result = (program[0] - program[1])

#print result
print(result)