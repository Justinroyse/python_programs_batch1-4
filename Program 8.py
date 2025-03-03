store = []
counter = 0
for i in range(10):
    program = int(input(f"Enter number {i+1}: "))
    store.append(program)
    if program % 2 != 0:
        counter += 1
    else:
        pass
print(counter)