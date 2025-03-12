#create list for 10 user input
program = [int(input(f"Enter a number ({numbers+1}):  "))
           for numbers in range(10)]
#print result with built-in sum() function
print(sum(program))