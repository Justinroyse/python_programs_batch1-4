#create function store list, identify highest number
def highest(program):
    return max(program)
#create while loop for input until invalid
user_input_collection = []
while True:
    try:
        user_input = int(input("Enter number: "))
        user_input_collection.append(user_input)
    except ValueError:
        print("Invalid input, printing highest number...")
        break
#print result
print(highest(user_input_collection))