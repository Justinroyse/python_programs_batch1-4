#create function to check for duplicates, display number with most duplicate
def duplicate_checker(program):
    duplicates = []
    seen = []
    most_duplicate_number = None
    max_duplicate = 0

    for numbers in program:
        if numbers in seen and numbers not in duplicates:
            duplicates.append(numbers)
        else:
            seen.append(numbers)

    for numbers in seen:
        counter = program.count(numbers)
        if counter > 1 and counter > max_duplicate:
            most_duplicate_number = numbers
            max_duplicate = counter

    return most_duplicate_number
#create while loop user input until invalid
user_input = []
while True:
    try:
        given = int(input("Enter number: "))
        user_input.append(given)
    except ValueError:
        print("Invalid input, printing most duplicate number...")
        break
#print result
result = duplicate_checker(user_input)
if result is None:
    print("No duplicates are found")
else:
    print(result)