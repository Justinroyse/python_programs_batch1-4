#Create variable for list to store numbers
stored_numbers = []
#Create while loop for the logic and iterating
while True:
    user_input = int(input("Enter number: "))

    if user_input in stored_numbers:
        print("Duplicate")
    else:
        stored_numbers.append(user_input)
        print("Unique")