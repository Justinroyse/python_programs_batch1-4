#create list for 2 user input
program = [int(input(f"Enter a number ({numbers+1}):  "))
           for numbers in range(2)]
#create if else logic to compare user input if equal using list
if program[0] != program[1]:
    print("Not equal")
else:
    print("Equal")