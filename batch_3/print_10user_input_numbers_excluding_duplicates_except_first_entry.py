#Create a function that checks for duplicates and only prints the first entry
def duplicate_checker(given):
    seen = set()
    unique_numbers = []
    for number in given:
        if number not in seen:
            unique_numbers.append(number)
            seen.add(number)
    return unique_numbers

#Create a list for loop variable that will be used for user_inputs
program = [int(input(f"Enter number ({inputs+1}): "))
           for inputs in range(10)]

print(duplicate_checker(program))

