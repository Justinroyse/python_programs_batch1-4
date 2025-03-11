#create function to check for duplicates
def duplicate_checker(given):
    checker = given[0]
    for items in given[1:]:
        if checker != given[1:]:
            print(items)
    return given
#create user input for loop 10 numbers
program = [int(input(f"Enter number ({user_inputs+1}): "))
           for user_inputs in range(10)]
#print result
print(duplicate_checker(program))
