#create list for 2 user input
program = [int(input(f"Enter number ({numbers+1}):  "))
           for numbers in range(2)]

#create if else logic to determine if the numbers is Not equal from referencing to list
if program[0] != program[1]:
    print("Not equal")
else:
    print("Equal")
    