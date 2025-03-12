#Create list variable to store user input and reference the lowest number
stored_numbers = []

#Create while loop for user input until invalid and print the lowest number
while True:
    try:
        user_input = int(input("Enter number: "))
        stored_numbers.append(user_input)
    except ValueError:
        print("Finished Loop: Printing the Lowest Number")
        break

if stored_numbers:
    print(f"Lowest number: {min(stored_numbers)}")
else:
    print("No valid input detected")
