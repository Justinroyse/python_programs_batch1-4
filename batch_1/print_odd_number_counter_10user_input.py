store = []
counter = 0

for i in range(10):
    program = int(input(f"Enter number ({i+1}):  "))
    store.append(program)

for item in store:
    if item % 2 != 0:
        counter += 1

print(counter)