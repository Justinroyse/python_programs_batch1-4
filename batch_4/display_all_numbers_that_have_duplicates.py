#create function to check for duplicates
def duplicate_checker(given):
    duplicates_numbers = []
    seen = set()

    for numbers in given:
        if numbers in seen and numbers not in duplicates_numbers:
            duplicates_numbers.append(numbers)
        else:
            seen.add(numbers)
    return duplicates_numbers

#create user input for loop 10 numbers
program = [int(input(f"Enter number ({user_inputs+1}): "))
           for user_inputs in range(10)]

#print result
print("With Duplicates: ", duplicate_checker(program))
