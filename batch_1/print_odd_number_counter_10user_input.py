#create list and counter to store numbers and count odd user input numbers
store = []
counter = 0

#create 10 iterations for user input
for numbers in range(10):
    program = int(input(f"Enter number ({numbers+1}):  "))
    store.append(program)

#count odd numbers
for number in store:
    if number % 2 != 0:
        counter += 1

#print result
print(counter)