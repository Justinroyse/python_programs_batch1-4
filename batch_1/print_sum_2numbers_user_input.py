#create list for 2 user input
program = [int(input(f"Enter a number ({numbers+1}):  "))
           for numbers in range(2)]
#print result using built-in sum() function
print(sum(program))