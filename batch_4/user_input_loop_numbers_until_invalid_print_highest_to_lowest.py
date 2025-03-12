#initialize list for user inputs
user_input_collection = []

#while loop for user input until invalid
while True:
    try:
        user_input = int(input("Enter number: "))
        user_input_collection.append(user_input)
    except ValueError:
        print("Invalid input, sorting numbers... (Highest to lowest)")
        break

#implement sort function for list of user input
user_input_collection.sort(reverse=True)

#print result
print(user_input_collection)

