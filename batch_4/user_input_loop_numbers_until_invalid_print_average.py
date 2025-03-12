#create function store list, display average
def average(program):
    collection_numbers = []

    for numbers in program:
        collection_numbers.append(numbers)

    result = sum(collection_numbers)/len(collection_numbers)

    return result

#create user input while loop until input is invalid
user_input_collection = []
while True:
    try:
        user_input = int(input("Enter number: "))
        user_input_collection.append(user_input)
    except ValueError:
        print("Invalid input, printing average...")
        break

#print result
print(average(user_input_collection))