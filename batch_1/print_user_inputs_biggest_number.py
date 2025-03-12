#create list for 2 user input
program = [int(input(f"Enter a number({numbers+1}):  "))
           for numbers in range(2)]

#print biggest number with built-in max() function
print(max(program))
