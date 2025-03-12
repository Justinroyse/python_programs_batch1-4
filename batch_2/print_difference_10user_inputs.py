#create difference function
def difference(given):
    operation = given[0]
    for items in given[1:]:
        operation -= items
    return operation
#create list for 10 user input
program = [int(input(f"Enter number ({numbers+1}):  "))
           for numbers in range(10)]
#use difference function to print program
print(difference(program))
