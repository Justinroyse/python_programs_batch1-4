#create list for 2 user input
numbers = [int(input(f"Enter a number ({number+1}):  "))
           for number in range(2)]

#create if else logic to compare user input if equal using list
if numbers[0] != numbers[1]:
    print("Not equal")
else:
    print("Equal")