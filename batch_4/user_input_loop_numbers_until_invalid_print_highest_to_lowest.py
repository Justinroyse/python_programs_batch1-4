#create while loop for user input until invalid number
user_input_collection = []

while True:
    try:
        user_input = int(input("Enter number: "))
        user_input_collection.append(user_input)
    except ValueError:
        print("Invalid input, sorting numbers... (Highest to lowest)")
        break

#print result
user_input_collection.sort(reverse=True)
print(user_input_collection)

