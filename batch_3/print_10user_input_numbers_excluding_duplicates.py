#function that checks for duplicates and displays numbers that don't have duplicates
def duplicate_checker(given):
    stored_items = given[0]
    for items in given[0:]:
        if stored_items != items:
            print(items)
    return " "
#for loop inside a list used for user number inputs
program = [int(input(f"Enter number ({i+1}): "))
           for i in range(0,10)]
print(duplicate_checker(program))