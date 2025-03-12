#Create a list variable to store numbers
stored_numbers = []

#Create while loop for user inputs numbers and implement sort function
while True:
    try:
        user_input = int(input("Enter number: "))
        stored_numbers.append(user_input)
    except ValueError:
        print("Invalid input: Finishing the Loop and Sorting the Numbers...")
        break

if stored_numbers:
    stored_numbers.sort(reverse=False)
    print(stored_numbers)
else:
    print("No valid input detected")

