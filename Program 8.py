counter = 0

for i in range(10):
    given = int(input(f"Enter a number {i+1}: "))
    if given % 2 != 0:
        counter += 1

print("Odd Counter: ", counter)



