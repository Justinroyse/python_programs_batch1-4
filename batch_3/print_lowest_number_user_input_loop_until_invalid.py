#Create variable for list to store numbers
stored_numbers = []
#Create while loop for the logic and iterating
while True:
    user_input = int(input("Enter number: "))
    stored_numbers.append(user_input)
    if stored_numbers[0:] != stored_numbers[1:]:
        print("Unique")
    else:
        print("Duplicate")